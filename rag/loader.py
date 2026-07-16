"""
loader.py

Loads all knowledge documents recursively.
"""

from pathlib import Path

from config import KNOWLEDGE_FOLDER
from constants import SUPPORTED_DOCUMENTS


class DocumentLoader:
    """
    Loads knowledge documents from the knowledge folder.
    """

    def __init__(self):

        self.knowledge_path = Path(KNOWLEDGE_FOLDER)

        self.documents = {}

    # =====================================================

    def load(self):
        """
        Load all supported knowledge documents.

        Returns:
            dict
        """

        self.documents.clear()

        if not self.knowledge_path.exists():

            print("[ERROR] Knowledge folder not found.")

            return self.documents

        files_loaded = 0

        for extension in SUPPORTED_DOCUMENTS:

            for file in self.knowledge_path.rglob(f"*{extension}"):

                try:

                    with open(
                        file,
                        "r",
                        encoding="utf-8"
                    ) as f:

                        relative = file.relative_to(
                            self.knowledge_path
                        )

                        category = (
                            relative.parent.as_posix()
                        )

                        if category == ".":

                            category = "general"

                        self.documents[str(relative)] = {

                            "name": file.stem,

                            "category": category,

                            "path": str(relative),

                            "text": f.read()

                        }

                        files_loaded += 1

                except Exception as error:

                    print(
                        f"[ERROR] Failed to load {file}: {error}"
                    )

        print(
            f"[INFO] Loaded {files_loaded} knowledge documents."
        )

        return self.documents

    # =====================================================

    def get_document(self, name: str):
        """
        Retrieve a document by name.
        """

        for document in self.documents.values():

            if document["name"] == name:

                return document

        return None

    # =====================================================

    def count(self):
        """
        Return number of loaded documents.
        """

        return len(self.documents)

    # =====================================================

    def list_documents(self):
        """
        Print loaded documents.
        """

        print()

        print("=" * 60)

        print("Knowledge Documents")

        print("=" * 60)

        for document in self.documents.values():

            print(
                f"{document['category']} -> {document['name']}"
            )

        print("=" * 60)