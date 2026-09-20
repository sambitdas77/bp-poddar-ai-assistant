import time
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Load PDF
loader = PyPDFLoader("documents/makaut_syllabus.pdf")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# Gemini embedding model
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    task_type="RETRIEVAL_DOCUMENT",
    output_dimensionality=768
)
 
# Create empty Chroma database
vector_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

BATCH_SIZE = 50   


for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i+BATCH_SIZE]

    print(f"\nEmbedding batch {i//BATCH_SIZE + 1} ({len(batch)} chunks)...")

    vector_db.add_documents(batch)

    # Don't sleep after the last batch
    if i + BATCH_SIZE < len(chunks):
        print("Waiting 65 seconds....\n")
        time.sleep(65)

print("\n✅ All chunks stored successfully!")
print(f"Total chunks stored: {len(chunks)}")

print("✅ Chroma Vector Database Created!")
print(f"Stored {len(chunks)} chunks.")