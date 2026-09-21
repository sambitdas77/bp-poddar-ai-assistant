
import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

app = FastAPI(
    title="BP Poddar AI Assistant API",
    version="2.3.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    task_type="RETRIEVAL_QUERY",
    output_dimensionality=768
)

db = Chroma(
    persist_directory="../chroma_db",
    embedding_function=embeddings
)


class ChatRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "BP Poddar AI Assistant Backend Running 🚀"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    docs = db.similarity_search(
        request.question,
        k=5
    )

    context = "\n\n".join([
        f"Page {doc.metadata['page']+1}\n{doc.page_content}"
        for doc in docs
    ])

    prompt = f"""
You are BP Poddar AI Assistant.

Answer ONLY using the provided context.

If the answer is not present, reply:
'The uploaded documents do not contain this information.'

Context:
{context}

Question:
{request.question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return {
        "answer": response.text,
        "sources": [doc.metadata["page"] + 1 for doc in docs]
    }