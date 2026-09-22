
from langchain_chroma import Chroma

from rag.embeddings import get_embeddings


def get_retriever(collection_name: str):
    """
    Load a specific Chroma collection.
    """

    embeddings = get_embeddings("RETRIEVAL_QUERY")

    db = Chroma(
        persist_directory="../chroma_db",
        collection_name=collection_name,
        embedding_function=embeddings
    )

    return db


def search_collection(collection_name: str, question: str, k=5):
    """
    Search inside one collection.
    """

    db = get_retriever(collection_name)

    docs = db.similarity_search(question, k=k)

    return docs