
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai

from rag.retriever import search_collection
from rag.prompt import build_prompt

load_dotenv()

# -------------------------------
# FastAPI App
# -------------------------------

app = FastAPI(
    title="BP Poddar AI Assistant API",
    version="2.5.0"
)

# -------------------------------
# CORS
# -------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Gemini Client
# -------------------------------

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -------------------------------
# Request Model
# -------------------------------

class ChatRequest(BaseModel):
    question: str


# -------------------------------
# Home Route
# -------------------------------

@app.get("/")
def home():
    return {
        "message": "BP Poddar AI Assistant Backend Running 🚀",
        "version": "2.5.0"
    }


# -------------------------------
# Chat Route
# -------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    # Search syllabus collection
    docs = search_collection(
        collection_name="syllabus",
        question=request.question,
        k=5
    )

    prompt = build_prompt(
        request.question,
        docs
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return {
        "answer": response.text,
        "sources": [
            {
                "page": doc.metadata["page"] + 1,
                "document": doc.metadata["source_file"]
            }
            for doc in docs
        ]
    }