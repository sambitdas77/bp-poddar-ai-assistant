
from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load API key
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

# Create embedding model
from google.genai import types
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    task_type="RETRIEVAL_DOCUMENT",
    output_dimensionality=768
)
# Convert ONLY the first chunk into an embedding
vector = embeddings.embed_query(chunks[0].page_content)

print("Embedding created successfully!")
print(f"Vector length: {len(vector)}")

print("\nFirst 10 numbers:")
print(vector[:10])