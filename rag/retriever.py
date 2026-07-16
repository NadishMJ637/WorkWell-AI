"""
retriever.py

Retrieves the most relevant document
from the knowledge base.
"""

from rag.loader import DOCUMENTS


def retrieve_context(question: str) -> str:
    """
    Retrieve the most relevant document.

    Parameters:
        question (str)

    Returns:
        str
    """

    question_words = question.lower().split()

    best_score = 0

    best_document = ""

    for document_name, document_text in DOCUMENTS.items():

        score = 0

        text = document_text.lower()

        for word in question_words:

            if word in text:

                score += 1

        if score > best_score:

            best_score = score

            best_document = document_text

    return best_document