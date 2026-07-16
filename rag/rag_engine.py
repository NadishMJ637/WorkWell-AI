"""
rag_engine.py

Retrieval-Augmented Generation (RAG) engine
for WorkWell AI.
"""

from llm import LLM
from rag.semantic_search import SemanticSearch


class RAGEngine:
    """
    Handles retrieval and answer generation.
    """

    def __init__(self):

        self.search = SemanticSearch()

    # =====================================================

    def answer_question(
        self,
        question: str,
        conversation_history: str = ""
    ):
        """
        Answer a question using the company knowledge base.
        """

        results = self.search.search(question)

        if not results:

            return {
                "answer": "I couldn't find this information in the company knowledge base.",
                "sources": []
            }

        # --------------------------------------------------

        context = ""

        sources = []

        for result in results:

            context += result["text"] + "\n\n"

            sources.append({

                "document": result["document"],

                "category": result["category"],

                "distance": round(result["distance"], 3)

            })

        # --------------------------------------------------
        # Debug
        # --------------------------------------------------

        print("\n" + "=" * 70)
        print("RAG CONTEXT")
        print("=" * 70)
        print(context)
        print("=" * 70)

        # --------------------------------------------------

        prompt = f"""
You are WorkWell AI, an internal AI assistant for employees.

Your ONLY source of truth is the COMPANY KNOWLEDGE below.

========================================================
COMPANY KNOWLEDGE
========================================================

{context}

========================================================
EMPLOYEE QUESTION
========================================================

{question}

========================================================
STRICT RULES
========================================================

1. Use ONLY the COMPANY KNOWLEDGE above.
2. Never use your own knowledge.
3. Never assume or infer information.
4. Never mention "most companies" or general HR practices.
5. Answer ONLY the user's question.
6. If the answer is not found in the COMPANY KNOWLEDGE, reply exactly:

I couldn't find this information in the company knowledge base.

7. Keep the answer under 80 words.
8. Quote numbers, policies, and dates exactly as written.
9. Do not mention information unrelated to the question.
10. Do not explain your reasoning.

========================================================
ANSWER
========================================================
"""

        print("\nSending prompt to Llama...")
        answer = LLM.generate(prompt)
        print("Llama finished.\n")

        return {

            "answer": answer,

            "sources": sources

        }


# =========================================================

rag = RAGEngine()


def answer_question(
    question,
    conversation_history=""
):
    """
    Compatibility wrapper.
    """

    return rag.answer_question(
        question,
        conversation_history
    )["answer"]