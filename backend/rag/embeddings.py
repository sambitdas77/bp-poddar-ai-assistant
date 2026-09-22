
import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()


def get_embeddings(task_type="RETRIEVAL_DOCUMENT"):
    """
    Returns Gemini Embedding Model.
    """

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-2",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        task_type=task_type,
        output_dimensionality=768
    )

    return embeddings