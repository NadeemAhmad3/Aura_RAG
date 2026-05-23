import uuid
from langchain_google_genai import ChatGoogleGenerativeAI
import config
from db.vector_db_manager import VectorDbManager
from db.parent_store_manager import ParentStoreManager
from document_chunker import DocumentChuncker
from rag_agent.tools import ToolFactory
from rag_agent.graph import create_agent_graph
from core.observability import Observability

class RAGSystem:

    def __init__(self, collection_name=config.CHILD_COLLECTION):
        self.collection_name = collection_name
        self.vector_db = VectorDbManager()
        self.parent_store = ParentStoreManager()
        self.chunker = DocumentChuncker()
        self.observability = Observability()
        self.agent_graph = None
        self.thread_id = str(uuid.uuid4())
        self.recursion_limit = config.GRAPH_RECURSION_LIMIT

    def initialize(self):
        self.vector_db.create_collection(self.collection_name)
        collection = self.vector_db.get_collection(self.collection_name)

        if not config.GOOGLE_API_KEYS:
            print("⚠️ WARNING: No Google API keys found in .env files. Please add GOOGLE_API_KEY_1, GOOGLE_API_KEY_2, etc.")
            
        # Create a list of LLM instances, one for each API key
        llms = [
            ChatGoogleGenerativeAI(
                model=config.LLM_MODEL, 
                temperature=config.LLM_TEMPERATURE,
                google_api_key=api_key
            ) for api_key in config.GOOGLE_API_KEYS
        ]
        
        # Pull the primary LLM
        llm = llms[0] if llms else ChatGoogleGenerativeAI(model=config.LLM_MODEL)
        
        # Attach the rest as fallback models (LangChain natively cascades if API limits are hit)
        if len(llms) > 1:
            llm = llm.with_fallbacks(llms[1:])

        tools = ToolFactory(collection).create_tools()
        self.agent_graph = create_agent_graph(llm, tools)

    def get_config(self):
        cfg = {"configurable": {"thread_id": self.thread_id}, "recursion_limit": self.recursion_limit}
        handler = self.observability.get_handler()
        if handler:
            cfg["callbacks"] = [handler]
        return cfg

    def reset_thread(self):
        try:
            self.agent_graph.checkpointer.delete_thread(self.thread_id)
        except Exception as e:
            print(f"Warning: Could not delete thread {self.thread_id}: {e}")
        self.thread_id = str(uuid.uuid4())