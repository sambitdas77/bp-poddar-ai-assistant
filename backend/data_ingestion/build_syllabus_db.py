import sys
from pathlib import Path
import time

# Make backend/ the project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from langchain_chroma import Chroma

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embeddings

print("\n🚀 Building Syllabus Vector Database...\n")

# Load syllabus PDFs
documents = load_documents("../data/documents/syllabus")

# Split into chunks
chunks = split_documents(documents)

# Gemini embeddings
embeddings = get_embeddings()

# Chroma collection
db = Chroma(
    persist_directory="../chroma_db",
    collection_name="syllabus",
    embedding_function=embeddings,
)

BATCH_SIZE = 80

for i in range(0, len(chunks), BATCH_SIZE):
    batch = chunks[i:i + BATCH_SIZE]

    print(f"Embedding batch {i // BATCH_SIZE + 1} ({len(batch)} chunks)...")

    db.add_documents(batch)

    if i + BATCH_SIZE < len(chunks):
        print("⏳ Waiting 60 seconds for Gemini free-tier quota...\n")
        time.sleep(60)

print("\n✅ Syllabus Collection Created Successfully!")
print(f"📚 Total chunks stored: {len(chunks)}")