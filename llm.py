"""
llm.py

Centralized interface for all LLM interactions.

Architecture:

Qwen  -> Analysis
Llama -> Response Generation
"""

from ollama import chat

from config import (
    ANALYSIS_MODEL,
    CHAT_MODEL
)

from prompts.analysis_prompt import SYSTEM_PROMPT


class LLM:
    """
    Central LLM Service.
    """

    # =====================================================
    # Internal Chat Function
    # =====================================================

    @staticmethod
    def _chat(model: str, messages: list) -> str:
        """
        Send messages to Ollama.
        """

        response = chat(
            model=model,
            messages=messages
        )

        return response["message"]["content"]

    # =====================================================
    # Analysis
    # =====================================================

    @staticmethod
    def analyze(user_message: str) -> str:
        """
        Analyze the user message.

        Uses:
            Qwen
        """

        messages = [

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": user_message
            }

        ]

        return LLM._chat(
            ANALYSIS_MODEL,
            messages
        )

    # =====================================================
    # Response Generation
    # =====================================================

    @staticmethod
    def generate(prompt: str) -> str:
        """
        Generate natural language response.

        Uses:
            Llama
        """

        messages = [

            {
                "role": "user",
                "content": prompt
            }

        ]

        return LLM._chat(
            CHAT_MODEL,
            messages
        )

    # =====================================================
    # Summary (Future)
    # =====================================================

    @staticmethod
    def summarize(text: str) -> str:
        """
        Summarize long conversations.
        """

        prompt = f"""
Summarize the following conversation.

{text}
"""

        return LLM.generate(prompt)

    # =====================================================
    # Rewrite (Future)
    # =====================================================

    @staticmethod
    def rewrite(text: str) -> str:
        """
        Rewrite text professionally.
        """

        prompt = f"""
Rewrite professionally.

{text}
"""

        return LLM.generate(prompt)


# ==========================================================
# Backward Compatibility
# ==========================================================

def generate_json(user_message: str):
    """
    Legacy wrapper.

    Older files can still call:

    generate_json()
    """

    return LLM.analyze(user_message)


def generate_text(prompt: str):
    """
    Legacy wrapper.

    Older files can still call:

    generate_text()
    """

    return LLM.generate(prompt)