import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY","")
GROQ_MODEL=os.getenv("GROQ_MODEL","llama-3.3-70b-versatile")
BACKEND_URL=os.getenv("BACKEND_URL","http://localhost:8000")
MAX_FILE_SIZE_MB=int(os.getenv("MAX_FILE_SIZE_MB","5"))
RAG_ENABLED=os.getenv("RAG_ENABLED","true").lower()=="true"
CORS_ORIGINS=[x.strip() for x in os.getenv("CORS_ORIGINS","http://localhost:8501").split(",")]
