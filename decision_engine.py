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
    INTENT_LEAVE_POLICY,
    INTENT_COMPANY_POLICY,
    INTENT_WORK_FROM_HOME,
    INTENT_EMPLOYEE_BENEFITS,

    INTENT_STRESS,
    INTENT_BURNOUT,
    INTENT_ANXIETY,
    INTENT_SLEEP,
    INTENT_PRODUCTIVITY,
    INTENT_WORK_LIFE_BALANCE,
    INTENT_MOTIVATION,
    INTENT_CAREER,
    INTENT_EMERGENCY
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
    # Emergency / Critical Priority
    # --------------------------------------------

    if parsed.intent == INTENT_EMERGENCY or parsed.priority == PRIORITY_CRITICAL or parsed.action == ACTION_EMERGENCY:

        return Decision(

            action=ACTION_EMERGENCY,

            reason="Critical priority or emergency intent detected."

        )

    # --------------------------------------------
    # Company Policy → RAG
    # --------------------------------------------

    if parsed.intent in {

        INTENT_LEAVE,

        INTENT_POLICY,

        INTENT_LEAVE_POLICY,

        INTENT_COMPANY_POLICY,

        INTENT_WORK_FROM_HOME,

        INTENT_EMPLOYEE_BENEFITS

    } or parsed.action == ACTION_RAG:

        return Decision(

            action=ACTION_RAG,

            reason="Company policy / RAG intent detected."

        )

    # --------------------------------------------
    # Mental Wellness → Recommendations
    # --------------------------------------------

    if parsed.intent in {

        INTENT_STRESS,

        INTENT_BURNOUT,

        INTENT_ANXIETY,

        INTENT_SLEEP,

        INTENT_PRODUCTIVITY,

        INTENT_WORK_LIFE_BALANCE,

        INTENT_MOTIVATION,

        INTENT_CAREER

    } or parsed.action == ACTION_RECOMMENDATION:

        return Decision(

            action=ACTION_RECOMMENDATION,

            reason="Mental wellness recommendation intent detected."

        )

    # --------------------------------------------
    # Greetings / Goodbye / Help
    # --------------------------------------------

    if parsed.action in {ACTION_GREETING, ACTION_GOODBYE, ACTION_HELP}:

        return Decision(

            action=ACTION_GENERAL,

            reason=f"{parsed.action.capitalize()} detected."

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