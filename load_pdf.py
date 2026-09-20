
from langchain_community.document_loaders import PyPDFLoader

# Load the PDF
loader = PyPDFLoader("documents/makaut_syllabus.pdf")

# Convert PDF into Document objects
documents = loader.load()

# Total number of pages
print(f"Total pages in PDF: {len(documents)}")

# Metadata of first page
print("\nFirst page metadata:")
print(documents[0].metadata)

# First 500 characters of first page
print("\nFirst page content:")
print(documents[0].page_content[:500])