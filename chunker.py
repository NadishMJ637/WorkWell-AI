from pathlib import Path


class DocumentChunker:
    """
    Splits text documents into chunks.
    """

    def __init__(self, chunk_size=500):
        self.chunk_size = chunk_size

    def chunk_text(self, text):
        """
        Split text into chunks based on paragraphs.
        """
        paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]

        chunks = []

        current_chunk = ""

        for paragraph in paragraphs:

            if len(current_chunk) + len(paragraph) <= self.chunk_size:
                current_chunk += paragraph + "\n\n"

            else:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n\n"

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def chunk_file(self, file_path):
        """
        Read a file and return chunks.
        """
        text = Path(file_path).read_text(encoding="utf-8")

        return self.chunk_text(text)