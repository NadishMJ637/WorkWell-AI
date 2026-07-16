"""
rag_prompt.py

Builds the prompt used for Retrieval-Augmented Generation (RAG).
"""


def build_rag_prompt(
    conversation_history: str,
    question: str,
    context: str
) -> str:
    """
    Build the RAG prompt.

    Parameters:
        conversation_history (str)
        question (str)
        context (str)

    Returns:
        str
    """

    prompt = f"""
You are WorkWell AI Assistant.

You answer questions using ONLY the provided company knowledge.

--------------------------------------------------

Conversation History

{conversation_history}

--------------------------------------------------

Company Knowledge

{context}

--------------------------------------------------

Current User Question

{question}

--------------------------------------------------

Instructions

1. Use the conversation history to understand follow-up questions.

2. Answer ONLY using the provided company knowledge.

3. Never invent company policies.

4. If the answer is not present in the company knowledge,
reply exactly:

"I couldn't find that information in the company's knowledge base."

5. Keep the response professional.

6. Keep the response under 150 words.
"""

    return prompt.strip()