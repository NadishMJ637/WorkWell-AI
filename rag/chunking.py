"""
chunking.py

Paragraph-aware document chunking for WorkWell AI.
"""

from typing import List

from config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


class DocumentChunker:
    """
    Splits documents into meaningful chunks.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP
    ):

        self.chunk_size = chunk_size
        self.overlap = overlap

    # =====================================================

    def chunk_document(self, text: str) -> List[str]:
        """
        Split an entire document into chunks.

        Strategy:
        1. Split into paragraphs.
        2. Keep paragraphs together.
        3. Split only oversized paragraphs.
        """

        if not text.strip():
            return []

        paragraphs = [
            p.strip()
            for p in text.split("\n\n")
            if p.strip()
        ]

        chunks = []

        current_chunk = ""

        for paragraph in paragraphs:

            # Paragraph fits into current chunk
            if (
                len(current_chunk)
                + len(paragraph)
                + 2
                <= self.chunk_size
            ):

                if current_chunk:

                    current_chunk += "\n\n"

                current_chunk += paragraph

            else:

                # Save previous chunk
                if current_chunk:

                    chunks.append(current_chunk)

                # Large paragraph
                if len(paragraph) > self.chunk_size:

                    large_chunks = self._split_large_paragraph(
                        paragraph
                    )

                    chunks.extend(large_chunks)

                    current_chunk = ""

                else:

                    current_chunk = paragraph

        if current_chunk:

            chunks.append(current_chunk)

        return chunks

    # =====================================================

    def _split_large_paragraph(
        self,
        paragraph: str
    ) -> List[str]:
        """
        Split a paragraph that exceeds the chunk size.
        """

        chunks = []

        start = 0

        while start < len(paragraph):

            end = start + self.chunk_size

            chunk = paragraph[start:end].strip()

            if chunk:

                chunks.append(chunk)

            start += (
                self.chunk_size
                - self.overlap
            )

        return chunks

    # =====================================================

    def statistics(self, chunks):
        """
        Display chunk statistics.
        """

        print()

        print("=" * 60)

        print("Chunk Statistics")

        print("=" * 60)

        print("Chunks :", len(chunks))

        for i, chunk in enumerate(chunks, start=1):

            print(

                f"Chunk {i} : {len(chunk)} characters"

            )

        print("=" * 60)