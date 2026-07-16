"""
response_generator.py

Builds prompts for the response generation model.
"""

from parser import ParsedResponse


class ResponseGenerator:
    """
    Generates prompts for the conversational model.
    """

    # =====================================================

    def build_prompt(
        self,
        parsed: ParsedResponse,
        recommendations=None,
        conversation_history="",
        rag_context=""
    ):
        """
        Build prompt for Llama.
        """

        if recommendations is None:

            recommendations = []

        recommendation_text = ""

        if recommendations:

            recommendation_text = "\n".join(

                f"- {item}"

                for item in recommendations

            )

        prompt = f"""
You are WorkWell AI.

You are a professional mental wellness assistant
for IT employees.

==============================
Conversation History
==============================

{conversation_history}

==============================
User Analysis
==============================

Intent:
{parsed.intent}

Sentiment:
{parsed.sentiment}

Priority:
{parsed.priority}

Reason:
{parsed.reason}

==============================
Knowledge Base
==============================

{rag_context}

==============================
Recommendations
==============================

{recommendation_text}

==============================
Instructions
==============================

1. Be empathetic.

2. Keep answers concise.

3. If recommendations are available,
include them naturally.

4. If knowledge base information is available,
use it accurately.

5. Never invent company policies.

6. Answer naturally.

==============================
User Message
==============================

{conversation_history.splitlines()[-1] if conversation_history else ""}
"""

        return prompt


# ==========================================================
# Singleton
# ==========================================================

_generator = ResponseGenerator()


def generate_response(
    parsed,
    recommendations=None,
    conversation_history="",
    rag_context=""
):
    """
    Backward compatible wrapper.
    """

    return _generator.build_prompt(

        parsed,

        recommendations,

        conversation_history,

        rag_context

    )