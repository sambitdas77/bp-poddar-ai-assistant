
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the PDF
loader = PyPDFLoader("documents/makaut_syllabus.pdf")
documents = loader.load()

# Create the text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

# Split into chunks
chunks = splitter.split_documents(documents)

# Print basic information
print(f"Original pages: {len(documents)}")
print(f"Chunks created: {len(chunks)}")

print("\nFirst chunk:\n")
print(chunks[0].page_content)

print("\nMetadata of first chunk:\n")
print(chunks[0].metadata)
print("\nSecond chunk:\n")
print(chunks[1].page_content)

print(chunks[1].metadata)