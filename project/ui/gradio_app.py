import gradio as gr
from core.chat_interface import ChatInterface
from core.document_manager import DocumentManager
from core.rag_system import RAGSystem
import os
from db.mongo_manager import MongoManager

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

head_html = r"""
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        const observer = new MutationObserver(() => {
            const links = document.querySelectorAll('#chat-window a, .chatbot a, .message a');
            links.forEach(link => {
                const text = link.textContent;
                if (text && (text.includes('\\') || text.includes('/')) && 
                    (text.toLowerCase().endsWith('.pdf') || 
                     text.toLowerCase().endsWith('.md') || 
                     text.toLowerCase().endsWith('.txt') ||
                     text.includes('Temp') ||
                     text.includes('gradio'))) {
                    const filename = text.split(/[\\/]/).pop();
                    link.textContent = '📄 ' + filename;
                }
            });
        });
        observer.observe(document.body, { childList: true, subtree: true });
    });
    </script>
"""

def create_gradio_ui():
    rag_system = RAGSystem()
    rag_system.initialize()
    
    doc_manager = DocumentManager(rag_system)
    chat_interface = ChatInterface(rag_system)
    mongo = MongoManager()
    
    def chat_handler(message, history, current_user, session_id, progress=gr.Progress()):
        text_msg = message["text"]
        files = message.get("files", [])
        
        if files:
            added, skipped = doc_manager.add_documents(
                files, 
                progress_callback=lambda p, desc: progress(p, desc=desc)
            )
            gr.Info(f"✅ Added {added} document(s) from chat context")
            
        user_id = current_user.get("id") if (current_user and isinstance(current_user, dict)) else None
        for chunk in chat_interface.chat(text_msg, history, user_id=user_id, session_id=session_id):
            yield chunk
            
    def toggle_sidebar(state):
        return not state, gr.update(visible=not state)

    # Auth logic
    def handle_auth(auth_mode, username, password):
        if not mongo.enabled:
            gr.Warning("❌ MongoDB Database not connected. Check MONGODB_URI in .env")
            return (
                gr.update(), gr.update(), None, None, gr.update(), [], "", []
            )

        if auth_mode == "Login":
            user, msg = mongo.login_user(username, password)
            if user:
                # Login success! Create/load active session
                session_id = mongo.create_session(user["id"])
                sessions = mongo.get_user_sessions(user["id"])
                files = doc_manager.get_markdown_files()
                gr.Info(f"Welcome back, {user['username']}!")
                
                return (
                    gr.update(visible=False),              # Hide Auth Container
                    gr.update(visible=True),               # Show App Container
                    user,                                  # Set current_user_state
                    session_id,                            # Set session_id_state
                    gr.update(value=[]),                   # Reset chatbot
                    sessions,                              # Set session_list_state
                    f"🟢 Logged in as: {user['username']}",# Set user_info text
                    files                                  # Set file_state
                )
            else:
                gr.Warning(msg)
                return gr.update(), gr.update(), None, None, gr.update(), [], "", []
        else:
            success, msg = mongo.register_user(username, password)
            if success:
                gr.Info(msg + " Please switch to Login mode.")
            else:
                gr.Warning(msg)
            return gr.update(), gr.update(), None, None, gr.update(), [], "", []

    def handle_logout():
        chat_interface.clear_session()
        return (
            gr.update(visible=True),   # Show Auth Container
            gr.update(visible=False),  # Hide App Container
            None,                      # Reset current_user_state
            None,                      # Reset session_id_state
            gr.update(value=[]),       # Reset chatbot
            [],                        # Reset session_list_state
            ""                         # Reset user_info text
        )

    def handle_new_chat(current_user):
        if not current_user:
            return None, gr.update(value=[]), []
        user_id = current_user["id"]
        session_id = mongo.create_session(user_id)
        sessions = mongo.get_user_sessions(user_id)
        chat_interface.clear_session()
        return session_id, gr.update(value=[]), sessions

    def handle_load_session(session_id, current_user):
        if not current_user or not session_id:
            return gr.update(value=[]), session_id
        messages = mongo.get_session_messages(session_id)
        
        # Load state
        chat_interface.clear_session()
        
        # Format messages for gr.Chatbot
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({
                "role": msg.get("role"),
                "content": msg.get("content"),
                "metadata": msg.get("metadata")
            })
        return gr.update(value=formatted_messages), session_id

    def handle_delete_session(session_id_to_delete, active_session_id, current_user):
        if not current_user:
            return active_session_id, [], gr.update()
        user_id = current_user["id"]
        mongo.delete_session(session_id_to_delete)
        sessions = mongo.get_user_sessions(user_id)
        
        if session_id_to_delete == active_session_id:
            # Recreate session if we deleted the active one
            new_session_id = mongo.create_session(user_id)
            sessions = mongo.get_user_sessions(user_id)
            chat_interface.clear_session()
            return new_session_id, sessions, gr.update(value=[])
            
        return active_session_id, sessions, gr.update()

    with gr.Blocks(title="Aura RAG") as demo:
        # --- State variables ---
        current_user_state = gr.State(None)
        session_id_state = gr.State(None)
        left_sidebar_state = gr.State(False)
        right_sidebar_state = gr.State(False)
        
        # --- AUTHENTICATION SCREEN ---
        with gr.Column(visible=True, elem_classes=["auth-container"]) as auth_container:
            gr.HTML("""
                <div class="auth-logo-wrapper">
                    <div class="logo-container">
                        <i class="fa-solid fa-bolt logo-icon"></i>
                        <h1 class="app-title">AURA RAG</h1>
                    </div>
                </div>
                <p class='auth-subtitle'>Sign in or create an account to access the AI assistant</p>
            """)
            
            auth_mode = gr.Radio(["Login", "Signup"], value="Login", show_label=False)
            username_input = gr.Textbox(placeholder="Username", show_label=False)
            password_input = gr.Textbox(placeholder="Password", type="password", show_label=False)
            auth_submit_btn = gr.Button("Submit", variant="primary")
            
        # --- MAIN APP SCREEN ---
        with gr.Column(visible=False) as app_container:
            with gr.Row(elem_classes=["header-row"]):
                # Left side: Logo only
                gr.HTML("""
                    <div class="logo-container">
                        <i class="fa-solid fa-bolt logo-icon"></i>
                        <h1 class="app-title">AURA RAG</h1>
                    </div>
                """)
                # Right side: User Info, Logout, History & Documents buttons
                with gr.Row(elem_classes=["header-right"]):
                    user_info_text = gr.HTML("", elem_classes=["user-info-text"])
                    logout_btn = gr.Button("Logout", elem_classes=["logout-btn"], size="sm")
                    toggle_history_btn = gr.Button("View History", elem_classes=["toggle-btn"], size="sm")
                    toggle_doc_btn = gr.Button("View Documents", elem_classes=["toggle-btn"], size="sm")
            
            with gr.Row():
                # LEFT SIDEBAR: Chat History
                with gr.Column(scale=0, min_width=350, visible=False, elem_classes=["sidebar-col"]) as history_sidebar:
                    gr.HTML('<div class="sidebar-header"><i class="fa-solid fa-history"></i> Chat History</div>')
                    new_chat_btn = gr.Button("＋ New Chat", variant="primary", size="sm")
                    gr.Markdown("---")
                    
                    session_list_state = gr.State([])
                    
                    @gr.render(inputs=session_list_state)
                    def render_session_list(sessions):
                        if not sessions:
                            gr.Markdown("📭 No past chats available")
                            return
                        for sess in sessions:
                            with gr.Row(elem_classes=["doc-row"]):
                                load_btn = gr.Button(sess["title"], size="sm", elem_classes=["session-title-btn"])
                                del_btn = gr.Button("✖", size="sm", elem_classes=["delete-btn"])
                                
                                # Set load session handler
                                load_btn.click(
                                    handle_load_session,
                                    inputs=[gr.State(sess["id"]), current_user_state],
                                    outputs=[chatbot, session_id_state]
                                )
                                
                                # Set delete session handler
                                del_btn.click(
                                    handle_delete_session,
                                    inputs=[gr.State(sess["id"]), session_id_state, current_user_state],
                                    outputs=[session_id_state, session_list_state, chatbot]
                                )
                
                # CENTER COLUMN: Chat Interface
                with gr.Column(scale=3):
                    chatbot = gr.Chatbot(
                        height=720, 
                        placeholder="<strong>Ask me anything!</strong><br><em>Upload documents contextually and I'll adapt dynamically.</em>",
                        show_label=False,
                        layout="bubble",
                        elem_id="chat-window"
                    )
                    chatbot.clear(chat_interface.clear_session)
                    
                    def scrape_url_handler(url):
                        if not url or not url.strip():
                            gr.Warning("Please enter a valid URL")
                            return doc_manager.get_markdown_files(), ""
                        url = url.strip()
                        if not (url.startswith("http://") or url.startswith("https://")):
                            url = "https://" + url
                        success = doc_manager.add_url(url)
                        if success:
                            gr.Info(f"✅ Scraped and added URL context: {url}")
                        else:
                            gr.Error(f"❌ Failed to scrape URL: {url}")
                        return doc_manager.get_markdown_files(), ""

                    chat_iface = gr.ChatInterface(
                        fn=chat_handler, 
                        chatbot=chatbot,
                        multimodal=True,
                        textbox=gr.MultimodalTextbox(
                            file_count="multiple",
                            file_types=[".pdf", ".md", ".txt", ".docx", ".csv"],
                            placeholder="Type a message or upload files...",
                            elem_id="chat-input"
                        ),
                        additional_inputs=[current_user_state, session_id_state]
                    )

                # RIGHT SIDEBAR: Knowledge Base
                with gr.Column(scale=0, min_width=350, visible=False, elem_classes=["sidebar-col"]) as doc_sidebar:
                    gr.HTML('<div class="sidebar-header"><i class="fa-solid fa-server"></i> Knowledge Base</div>')
                    gr.Markdown("Manage your project context.")
                    
                    # URL Scraper Input
                    with gr.Group():
                        url_input = gr.Textbox(
                            placeholder="Enter URL (e.g. https://example.com)...",
                            show_label=False,
                            container=False
                        )
                        scrape_btn = gr.Button("Scrape & Add URL", size="sm", variant="primary")
                    
                    gr.Markdown("---")
                    
                    # Dynamic list using Gradio State and gr.render
                    file_state = gr.State([])
                    
                    @gr.render(inputs=file_state)
                    def render_file_list(files):
                        if not files:
                            gr.Markdown("📭 No documents available in the knowledge base")
                            return
                        for f in files:
                            with gr.Row(elem_classes=["doc-row"]):
                                gr.Markdown(f"📄 {f}")
                                del_btn = gr.Button("✖", size="sm", elem_classes=["delete-btn"])
                                
                                def remove_doc(item_to_remove=f):
                                    doc_manager.remove_document(item_to_remove)
                                    return doc_manager.get_markdown_files()
                                    
                                del_btn.click(remove_doc, None, file_state)
                    
                    with gr.Row():
                        refresh_btn = gr.Button("Refresh", size="sm")
                        clear_btn = gr.Button("Clear All", variant="stop", size="sm")
                    
                    def force_refresh():
                        return doc_manager.get_markdown_files()
                        
                    def force_clear():
                        doc_manager.clear_all()
                        gr.Info("🗑️ Removed all documents")
                        return []
                        
                    refresh_btn.click(force_refresh, None, file_state)
                    clear_btn.click(force_clear, None, file_state)
                    scrape_btn.click(scrape_url_handler, inputs=[url_input], outputs=[file_state, url_input])
        
        # --- Click Actions & Handlers bindings ---
        auth_submit_btn.click(
            handle_auth,
            inputs=[auth_mode, username_input, password_input],
            outputs=[
                auth_container, 
                app_container, 
                current_user_state, 
                session_id_state, 
                chatbot, 
                session_list_state, 
                user_info_text,
                file_state
            ]
        )
        
        logout_btn.click(
            handle_logout,
            outputs=[
                auth_container,
                app_container,
                current_user_state,
                session_id_state,
                chatbot,
                session_list_state,
                user_info_text
            ]
        )
        
        new_chat_btn.click(
            handle_new_chat,
            inputs=[current_user_state],
            outputs=[session_id_state, chatbot, session_list_state]
        )
        
        # Sidebar Toggles
        toggle_history_btn.click(toggle_sidebar, inputs=[left_sidebar_state], outputs=[left_sidebar_state, history_sidebar])
        toggle_doc_btn.click(toggle_sidebar, inputs=[right_sidebar_state], outputs=[right_sidebar_state, doc_sidebar])
        
        # Refresh lists on toggle
        toggle_doc_btn.click(force_refresh, None, file_state)
        
    return demo