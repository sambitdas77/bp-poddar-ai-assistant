
import os
from dotenv import load_dotenv

from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# Load API key
load_dotenv()

# Gemini client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Embedding model for queries
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    task_type="RETRIEVAL_QUERY",
    output_dimensionality=768
)

# Load Chroma database
db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

print("="*60)
print("📘 BP Poddar AI Assistant is Ready!")
print("Type 'exit' anytime to quit.")
print("="*60)

while True:
    question = input("\n❓ Ask a question: ")

    if question.lower() == "exit":
        print("Goodbye Sambit! 👋")
        break

    # Retrieve relevant chunks
    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        [f"Page {doc.metadata['page']+1}:\n{doc.page_content}" for doc in docs]
    )

    prompt = f"""
You are a helpful AI assistant for MAKAUT Semester 7 syllabus.

Answer ONLY using the context below.
If the answer is not present, say "The PDF does not contain that information."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    print("\n🤖 Answer:\n")
    print(response.text)

    print("\n📄 Sources:")
    for doc in docs:
        print(f"Page {doc.metadata['page']+1}")