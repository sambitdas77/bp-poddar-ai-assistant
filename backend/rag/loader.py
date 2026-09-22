
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader


def load_documents(folder_path: str):
    """
    Load all PDF files from a folder.
    Returns a list of LangChain Documents.
    """

    folder = Path(folder_path)

    pdf_files = list(folder.glob("*.pdf"))

    documents = []

    for pdf in pdf_files:
        print(f"Loading: {pdf.name}")

        loader = PyPDFLoader(str(pdf))

        docs = loader.load()

        # Store PDF name in metadata
        for doc in docs:
            doc.metadata["source_file"] = pdf.name

        documents.extend(docs)

    print(f"Loaded {len(documents)} pages from {len(pdf_files)} PDFs.")

    return documents