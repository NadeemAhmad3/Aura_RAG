import os
import datetime
import uuid
import bcrypt
from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        
        # Load URI from environment
        self.uri = os.environ.get("MONGODB_URI") or os.environ.get("MONGO_URI")
        self.client = None
        self.db = None
        self.enabled = False

        if not self.uri:
            print("[Mongo] WARNING: MONGODB_URI is not set in environment. MongoDB features will be disabled.")
            return

        try:
            self.client = MongoClient(self.uri)
            # Access AURA_RAG database safely without truth-value testing database object
            try:
                self.db = self.client.get_default_database()
            except Exception:
                self.db = None
            if self.db is None:
                self.db = self.client["AURA_RAG"]

            # Trigger a simple connection check
            self.client.admin.command('ping')
            self.enabled = True
            print("[Mongo] Successfully connected to MongoDB Atlas!")
            
            # Ensure index on username for unique logins
            self.db["users"].create_index("username", unique=True)
        except Exception as e:
            print(f"[Mongo] Failed to connect to MongoDB Atlas: {e}")
            self.enabled = False

        self._initialized = True

    # --- User Authentication ---

    def register_user(self, username, password):
        if not self.enabled:
            return False, "Database not connected"
            
        username = username.strip()
        if not username or not password:
            return False, "Username and password cannot be empty"

        # Check if user already exists
        existing = self.db["users"].find_one({"username": username})
        if existing:
            return False, f"Username '{username}' is already taken"

        try:
            # Hash password securely
            salt = bcrypt.gensalt()
            password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            user_doc = {
                "username": username,
                "password_hash": password_hash,
                "created_at": datetime.datetime.utcnow()
            }
            self.db["users"].insert_one(user_doc)
            return True, "Registration successful!"
        except Exception as e:
            return False, f"Registration failed: {str(e)}"

    def login_user(self, username, password):
        if not self.enabled:
            return None, "Database not connected"
            
        username = username.strip()
        if not username or not password:
            return None, "Username and password cannot be empty"

        user = self.db["users"].find_one({"username": username})
        if not user:
            return None, "Invalid username or password"

        try:
            # Verify password hash
            if bcrypt.checkpw(password.encode('utf-8'), user["password_hash"]):
                return {
                    "id": str(user["_id"]),
                    "username": user["username"]
                }, "Login successful!"
            else:
                return None, "Invalid username or password"
        except Exception as e:
            return None, f"Login error: {str(e)}"

    # --- Chat Session Management ---

    def create_session(self, user_id, title="New Chat"):
        if not self.enabled:
            return str(uuid.uuid4())
            
        session_id = str(uuid.uuid4())
        session_doc = {
            "_id": session_id,
            "user_id": user_id,
            "title": title,
            "messages": [],
            "created_at": datetime.datetime.utcnow(),
            "updated_at": datetime.datetime.utcnow()
        }
        self.db["chat_sessions"].insert_one(session_doc)
        return session_id

    def get_user_sessions(self, user_id):
        if not self.enabled:
            return []
            
        try:
            cursor = self.db["chat_sessions"].find(
                {"user_id": user_id},
                {"_id": 1, "title": 1, "updated_at": 1}
            ).sort("updated_at", -1)
            
            sessions = []
            for doc in cursor:
                sessions.append({
                    "id": doc["_id"],
                    "title": doc["title"]
                })
            return sessions
        except Exception as e:
            print(f"Error fetching user sessions: {e}")
            return []

    def get_session_messages(self, session_id):
        if not self.enabled:
            return []
            
        try:
            session = self.db["chat_sessions"].find_one({"_id": session_id})
            if session:
                return session.get("messages", [])
            return []
        except Exception as e:
            print(f"Error fetching session messages: {e}")
            return []

    def save_session_messages(self, session_id, user_id, messages, title=None):
        if not self.enabled:
            return False
            
        try:
            # Auto-generate title if not specified
            if not title and messages:
                # Find the first user message
                user_msg = next((m for m in messages if m.get("role") == "user"), None)
                if user_msg:
                    content = user_msg.get("content", "")
                    title = content[:35] + ("..." if len(content) > 35 else "")
                else:
                    title = "New Chat"

            update_data = {
                "messages": messages,
                "updated_at": datetime.datetime.utcnow()
            }
            if title:
                update_data["title"] = title

            self.db["chat_sessions"].update_one(
                {"_id": session_id, "user_id": user_id},
                {"$set": update_data},
                upsert=True
            )
            return True
        except Exception as e:
            print(f"Error saving session: {e}")
            return False

    def delete_session(self, session_id):
        if not self.enabled:
            return False
            
        try:
            self.db["chat_sessions"].delete_one({"_id": session_id})
            return True
        except Exception as e:
            print(f"Error deleting session: {e}")
            return False
