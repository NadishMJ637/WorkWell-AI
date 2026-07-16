"""
semantic_search.py

Semantic Search for WorkWell AI.
"""

from config import TOP_K

from rag.embeddings import EmbeddingService
from rag.chroma_store import ChromaStore


class SemanticSearch:

    def __init__(self):

        self.embedder = EmbeddingService()
        self.store = ChromaStore()

    # =====================================================

    def search(self, query: str, top_k: int = TOP_K):

        if not query.strip():

            return []

        query_embedding = self.embedder.create_embedding(query)

        results = self.store.search(
            query_embedding,
            top_k
        )

        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])

        if distances:
            distances = distances[0]
        else:
            distances = [0] * len(documents)

        retrieved = []

        print("\n" + "=" * 70)
        print("SEMANTIC SEARCH DEBUG")
        print("=" * 70)

        for doc, meta, distance in zip(
            documents,
            metadatas,
            distances
        ):

            print(f"Document : {meta.get('document')}")
            print(f"Distance : {distance}")
            print()

            retrieved.append({

                "text": doc,

                "document": meta.get("document"),

                "category": meta.get("category"),

                "chunk_id": meta.get("chunk_id"),

                "distance": distance

            })

        # Sort by smallest distance (best match)
        retrieved.sort(key=lambda x: x["distance"])

        return retrieved

    # =====================================================

    def retrieve_context(self, query: str):

        results = self.search(query)

        if not results:

            return ""

        context = ""

        for result in results:

            context += result["text"] + "\n\n"

        return context.strip()

    # =====================================================

    def print_results(self, query: str):

        results = self.search(query)

        print("\n" + "=" * 70)
        print("SEARCH RESULTS")
        print("=" * 70)

        if not results:

            print("No results found.")
            return

        for i, result in enumerate(results, start=1):

            print(f"\nResult {i}")
            print("-" * 60)

            print("Document :", result["document"])
            print("Category :", result["category"])
            print("Chunk ID :", result["chunk_id"])
            print("Distance :", result["distance"])

            print()
            print(result["text"])

            print("-" * 60)