"""
vector_store.py

Builds an in-memory vector store using
chunked documents.
"""

from rag.loader import DOCUMENTS
from rag.embeddings import create_embedding
from rag.chunking import chunk_text

VECTOR_STORE = []


def build_vector_store():
    """
    Build the vector store from all
    knowledge documents.
    """

    VECTOR_STORE.clear()

    for document_name, document_text in DOCUMENTS.items():

        chunks = chunk_text(document_text)

        for chunk_id, chunk in enumerate(chunks):

            embedding = create_embedding(chunk)

            VECTOR_STORE.append(
                {
                    "document": document_name,
                    "chunk_id": chunk_id,
                    "text": chunk,
                    "embedding": embedding
                }
            )

    print(f"Loaded {len(VECTOR_STORE)} chunks.")