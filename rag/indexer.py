"""
indexer.py

Indexes all knowledge documents into ChromaDB.

Pipeline:

Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
ChromaDB
"""

import hashlib

from rag.loader import DocumentLoader
from rag.chunking import DocumentChunker
from rag.embeddings import EmbeddingService
from rag.chroma_store import ChromaStore


class DocumentIndexer:
    """
    Builds and updates the WorkWell knowledge index.
    """

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = DocumentChunker()

        self.embedder = EmbeddingService()

        self.store = ChromaStore()

    # =====================================================

    @staticmethod
    def calculate_hash(text: str):
        """
        Generate SHA256 hash.
        """

        return hashlib.sha256(
            text.encode("utf-8")
        ).hexdigest()

    # =====================================================

    def build_index(self):
        """
        Build or update the knowledge index.
        """

        print("\n" + "=" * 70)
        print("WORKWELL AI KNOWLEDGE INDEXER")
        print("=" * 70)

        documents = self.loader.load()

        indexed = 0

        skipped = 0

        total_chunks = 0

        for _, document in documents.items():

            print()

            print(f"Document : {document['name']}")

            new_hash = self.calculate_hash(
                document["text"]
            )

            old_hash = self.store.get_document_hash(
                document["name"]
            )

            # ------------------------------------------

            if old_hash == new_hash:

                print("Status   : Already Indexed")

                skipped += 1

                continue

            # ------------------------------------------

            self.store.delete_document(
                document["name"]
            )

            chunks = self.chunker.chunk_document(
                document["text"]
            )

            embeddings = self.embedder.create_embeddings(
                chunks
            )

            ids = []

            texts = []

            metas = []

            for chunk_id, (chunk, embedding) in enumerate(
                zip(chunks, embeddings)
            ):

                ids.append(
                    f"{document['name']}_{chunk_id}"
                )

                texts.append(chunk)

                metas.append({

                    "document": document["name"],

                    "category": document["category"],

                    "chunk_id": chunk_id,

                    "hash": new_hash

                })

            self.store.add_documents(

                ids=ids,

                texts=texts,

                embeddings=embeddings,

                metadatas=metas

            )

            indexed += 1

            total_chunks += len(chunks)

            print(f"Chunks   : {len(chunks)}")

        print()

        print("=" * 70)

        print("INDEX COMPLETED")

        print("=" * 70)

        print(f"Documents Loaded : {len(documents)}")

        print(f"Indexed          : {indexed}")

        print(f"Skipped          : {skipped}")

        print(f"Database Chunks  : {self.store.count()}")

        print("=" * 70)

    # =====================================================

    def rebuild_index(self):
        """
        Completely rebuild ChromaDB.
        """

        print()

        print("Resetting ChromaDB...")

        self.store.reset()

        self.build_index()

    # =====================================================

    def statistics(self):
        """
        Print database statistics.
        """

        print()

        print("=" * 50)

        print("Knowledge Base Statistics")

        print("=" * 50)

        print("Indexed Chunks :", self.store.count())

        print("Documents      :", len(self.store.list_documents()))

        print("=" * 50)

    # =====================================================

    def preview(self):

        """
        Preview stored chunks.
        """

        print()

        print(self.store.peek())