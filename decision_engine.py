"""
decision_engine.py

Determines what action WorkWell AI should perform.
"""

from dataclasses import dataclass

from parser import ParsedResponse

from constants import (
    ACTION_GENERAL,
    ACTION_RECOMMENDATION,
    ACTION_RAG,
    ACTION_EMERGENCY,
    ACTION_GREETING,
    ACTION_GOODBYE,
    ACTION_HELP,

    PRIORITY_CRITICAL,
    PRIORITY_HIGH,

    SENTIMENT_NEGATIVE,

    INTENT_LEAVE,
    INTENT_POLICY,
    INTENT_WORK_FROM_HOME,
    INTENT_EMPLOYEE_BENEFITS
)


# =====================================================
# Decision
# =====================================================

@dataclass
class Decision:

    action: str

    reason: str


# =====================================================
# Decision Engine
# =====================================================

def decide_action(parsed: ParsedResponse):
    """
    Decide which engine should respond.
    """

    # --------------------------------------------
    # Greetings
    # --------------------------------------------

    if parsed.action == ACTION_GREETING:

        return Decision(

            action=ACTION_GENERAL,

            reason="Greeting detected."

        )

    # --------------------------------------------

    if parsed.action == ACTION_GOODBYE:

        return Decision(

            action=ACTION_GENERAL,

            reason="Goodbye detected."

        )

    # --------------------------------------------

    if parsed.action == ACTION_HELP:

        return Decision(

            action=ACTION_GENERAL,

            reason="Help requested."

        )

    # --------------------------------------------
    # Company Policy → RAG
    # --------------------------------------------

    if parsed.intent in {

        INTENT_LEAVE,

        INTENT_POLICY,

        INTENT_WORK_FROM_HOME,

        INTENT_EMPLOYEE_BENEFITS

    }:

        return Decision(

            action=ACTION_RAG,

            reason="Company policy detected."

        )

    # --------------------------------------------
    # Critical Mental Health
    # --------------------------------------------

    if (

        parsed.priority == PRIORITY_CRITICAL

    ):

        return Decision(

            action=ACTION_EMERGENCY,

            reason="Critical priority."

        )

    # --------------------------------------------

    if (

        parsed.priority == PRIORITY_HIGH

        and

        parsed.sentiment == SENTIMENT_NEGATIVE

    ):

        return Decision(

            action=ACTION_RECOMMENDATION,

            reason="High priority negative sentiment."

        )

    # --------------------------------------------
    # LLM Recommendation
    # --------------------------------------------

    if parsed.action == ACTION_RECOMMENDATION:

        return Decision(

            action=ACTION_RECOMMENDATION,

            reason="Recommendation requested."

        )

    # --------------------------------------------
    # LLM RAG
    # --------------------------------------------

    if parsed.action == ACTION_RAG:

        return Decision(

            action=ACTION_RAG,

            reason="RAG requested."

        )

    # --------------------------------------------
    # Default
    # --------------------------------------------

    return Decision(

        action=ACTION_GENERAL,

        reason="General conversation."

    )


# =====================================================
# Debug
# =====================================================

def print_decision(decision):

    print()

    print("=" * 60)

    print("Decision")

    print("=" * 60)

    print("Action :", decision.action)

    print("Reason :", decision.reason)

    print("=" * 60)