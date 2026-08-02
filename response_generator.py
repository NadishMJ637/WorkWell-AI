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
        rag_context="",
        user_message=""
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

        if not user_message and conversation_history:
            user_lines = [line for line in conversation_history.splitlines() if line.startswith("User:")]
            if user_lines:
                user_message = user_lines[-1].replace("User:", "").strip()
            else:
                user_message = conversation_history.splitlines()[-1]

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

1. Be empathetic and supportive.

2. Keep answers concise, clear, and direct.

3. If recommendations are available, include them naturally in a friendly bulleted format.

4. If knowledge base information is available, use it accurately.

5. Never invent company policies.

6. Answer naturally as an assistant without echoing prompt headings or internal instructions.

==============================
User Message
==============================

{user_message}
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
    rag_context="",
    user_message=""
):
    """
    Backward compatible wrapper.
    """

    return _generator.build_prompt(

        parsed,

        recommendations,

        conversation_history,

        rag_context,

        user_message

    )