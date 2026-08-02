"""
ai_engine.py

Main AI Engine for WorkWell AI.
"""

from llm import LLM

from parser import parse_response
from validator import validate_response

from decision_engine import decide_action

from recommendation_engine import get_recommendations

from response_generator import generate_response

from history import ConversationHistory

from rag.rag_engine import RAGEngine
from rag.indexer import DocumentIndexer

from constants import (
    ACTION_GENERAL,
    ACTION_RECOMMENDATION,
    ACTION_RAG,
    ACTION_EMERGENCY
)


class AIEngine:
    """
    Main orchestrator for WorkWell AI.
    """

    def __init__(self):

        print("=" * 60)
        print("Initializing WorkWell AI...")
        print("=" * 60)

        # Conversation Memory
        self.history = ConversationHistory()

        # RAG Engine
        self.rag = RAGEngine()

        # Build Knowledge Base
        try:

            self.indexer = DocumentIndexer()

            self.indexer.build_index()

        except Exception as error:

            print(f"[WARNING] Knowledge Base: {error}")

        print("=" * 60)
        print("WorkWell AI Ready")
        print("=" * 60)

    # =====================================================

    def process(self, user_message: str):
        """
        Complete AI pipeline.
        """

        # ------------------------------------------
        # Save user message
        # ------------------------------------------

        self.history.add_user_message(user_message)

        conversation_history = (
            self.history.get_formatted_history()
        )

        # ------------------------------------------
        # Analysis Model (Qwen)
        # ------------------------------------------

        llm_output = LLM.analyze(user_message)

        parsed = parse_response(llm_output)

        parsed = validate_response(parsed)

        decision = decide_action(parsed)

        # ------------------------------------------
        # RAG
        # ------------------------------------------

        if decision.action == ACTION_RAG:

            answer = self.rag.answer_question(

                question=user_message,

                conversation_history=conversation_history

            )

            response = answer["answer"]

        # ------------------------------------------
        # Recommendation Engine
        # ------------------------------------------

        elif decision.action == ACTION_RECOMMENDATION:

            recommendations = get_recommendations(

                parsed.intent,

                parsed.sentiment,

                parsed.priority

            )

            prompt = generate_response(

                parsed,

                recommendations,

                conversation_history,

                user_message=user_message

            )

            response = LLM.generate(prompt)

        # ------------------------------------------
        # Emergency
        # ------------------------------------------

        elif decision.action == ACTION_EMERGENCY:

            response = (
                "I'm really sorry you're going through this. "
                "Please consider reaching out to your manager, "
                "HR, or your Employee Assistance Program. "
                "If you're in immediate danger, contact your "
                "local emergency services or someone you trust."
            )

        # ------------------------------------------
        # General Chat
        # ------------------------------------------

        else:

            prompt = generate_response(

                parsed,

                [],

                conversation_history,

                user_message=user_message

            )

            response = LLM.generate(prompt)

        # ------------------------------------------
        # Save assistant response
        # ------------------------------------------

        self.history.add_assistant_message(response)

        return response

    # =====================================================

    def clear_memory(self):
        """
        Clear conversation history.
        """

        self.history.clear()

    # =====================================================

    def get_history(self):
        """
        Return conversation history.
        """

        return self.history.get_messages()