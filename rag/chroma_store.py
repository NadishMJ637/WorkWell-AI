"""
chroma_store.py

Repository layer for ChromaDB.

Only this file communicates directly with ChromaDB.
"""

import chromadb

from config import (
    CHROMA_DB_PATH,
    CHROMA_COLLECTION,
    TOP_K
)


class ChromaStore:
    """
    Repository for WorkWell AI knowledge base.
    """

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=CHROMA_COLLECTION
        )

    # =====================================================

    def add_document(
        self,
        doc_id,
        text,
        embedding,
        metadata
    ):
        """
        Add a single chunk.
        """

        self.collection.add(

            ids=[doc_id],

            documents=[text],

            embeddings=[embedding],

            metadatas=[metadata]

        )

    # =====================================================

    def add_documents(
        self,
        ids,
        texts,
        embeddings,
        metadatas
    ):
        """
        Add multiple chunks.
        """

        self.collection.add(

            ids=ids,

            documents=texts,

            embeddings=embeddings,

            metadatas=metadatas

        )

    # =====================================================

    def search(
        self,
        embedding,
        top_k=TOP_K
    ):
        """
        Search similar chunks.
        """

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )

    # =====================================================

    def delete_document(
        self,
        document_name
    ):
        """
        Delete all chunks of one document.
        """

        try:

            self.collection.delete(

                where={
                    "document": document_name
                }

            )

        except:

            pass

    # =====================================================

    def get_document_hash(
        self,
        document_name
    ):
        """
        Return stored hash of a document.
        """

        result = self.collection.get(

            where={
                "document": document_name
            },

            limit=1

        )

        if not result["metadatas"]:

            return None

        return result["metadatas"][0]["hash"]

    # =====================================================

    def reset(self):
        """
        Delete the collection and recreate it.
        """

        try:

            self.client.delete_collection(
                CHROMA_COLLECTION
            )

        except:

            pass

        self.collection = self.client.get_or_create_collection(

            name=CHROMA_COLLECTION

        )

    # =====================================================

    def count(self):
        """
        Return total indexed chunks.
        """

        return self.collection.count()

    # =====================================================

    def peek(
        self,
        limit=5
    ):
        """
        Preview indexed chunks.
        """

        return self.collection.peek(limit)

    # =====================================================

    def list_documents(self):
        """
        Display indexed documents.
        """

        data = self.collection.get()

        docs = set()

        for meta in data["metadatas"]:

            docs.add(meta["document"])

        return sorted(list(docs))