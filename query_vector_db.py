
from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Same embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    task_type="RETRIEVAL_QUERY",
    output_dimensionality=768
)

# Load existing Chroma DB
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

# Ask a question
results = db.similarity_search(
    "What topics are covered in Machine Learning in Semester 7?",
    k=3
)

for i, doc in enumerate(results):
    print(f"\n========== Result {i+1} ==========")
    print("Page:", doc.metadata["page"] + 1)
    print(doc.page_content[:300])