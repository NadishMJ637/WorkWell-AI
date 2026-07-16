"""
embeddings.py

Embedding service for WorkWell AI.

Uses Ollama's embedding model to generate
vector embeddings for documents and queries.
"""

from ollama import embeddings

from config import EMBED_MODEL


class EmbeddingService:
    """
    Generates embeddings using Ollama.
    """

    def __init__(self):

        self.model = EMBED_MODEL

    # =====================================================

    def create_embedding(self, text: str):
        """
        Generate embedding for a single text.

        Parameters:
            text (str)

        Returns:
            list
        """

        if not text.strip():

            return []

        response = embeddings(

            model=self.model,

            prompt=text

        )

        return response["embedding"]

    # =====================================================

    def create_embeddings(self, texts):
        """
        Generate embeddings for multiple texts.

        Parameters:
            texts (list)

        Returns:
            list
        """

        vectors = []

        for text in texts:

            vectors.append(

                self.create_embedding(text)

            )

        return vectors

    # =====================================================

    def embedding_dimension(self):
        """
        Return embedding dimension.
        """

        sample = self.create_embedding("Hello")

        return len(sample)

    # =====================================================

    def similarity(self, embedding1, embedding2):
        """
        Compute cosine similarity between two embeddings.

        Parameters:
            embedding1 (list)
            embedding2 (list)

        Returns:
            float
        """

        dot = sum(

            a * b

            for a, b in zip(embedding1, embedding2)

        )

        norm1 = sum(

            a * a

            for a in embedding1

        ) ** 0.5

        norm2 = sum(

            b * b

            for b in embedding2

        ) ** 0.5

        if norm1 == 0 or norm2 == 0:

            return 0

        return dot / (norm1 * norm2)

    # =====================================================

    def information(self):
        """
        Print embedding model information.
        """

        print()

        print("=" * 60)

        print("Embedding Service")

        print("=" * 60)

        print("Model :", self.model)

        print("Dimension :", self.embedding_dimension())

        print("=" * 60)