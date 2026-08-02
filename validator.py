"""
validator.py

Validates the parsed response from the analysis model.
"""

from parser import ParsedResponse

from constants import (
    ACTION_GREETING,
    ACTION_GOODBYE,
    ACTION_HELP,
    ACTION_GENERAL,
    ACTION_RECOMMENDATION,
    ACTION_RAG,
    ACTION_EMERGENCY,
    ACTION_UNKNOWN,

    PRIORITY_LOW,
    PRIORITY_NORMAL,
    PRIORITY_HIGH,
    PRIORITY_CRITICAL,

    SENTIMENT_POSITIVE,
    SENTIMENT_NEUTRAL,
    SENTIMENT_NEGATIVE,

    INTENT_STRESS,
    INTENT_ANXIETY,
    INTENT_SLEEP,
    INTENT_BURNOUT,
    INTENT_WORK_LIFE_BALANCE,
    INTENT_MOTIVATION,
    INTENT_PRODUCTIVITY,
    INTENT_CAREER,
    INTENT_POLICY,
    INTENT_LEAVE,
    INTENT_LEAVE_POLICY,
    INTENT_COMPANY_POLICY,
    INTENT_WORK_FROM_HOME,
    INTENT_EMPLOYEE_BENEFITS,
    INTENT_GREETING,
    INTENT_GOODBYE,
    INTENT_GRATITUDE,
    INTENT_HELP,
    INTENT_GENERAL,
    INTENT_GENERAL_QUESTION,
    INTENT_EMERGENCY,
    INTENT_UNKNOWN
)


VALID_ACTIONS = {

    ACTION_GREETING,
    ACTION_GOODBYE,
    ACTION_HELP,
    ACTION_GENERAL,
    ACTION_RECOMMENDATION,
    ACTION_RAG,
    ACTION_EMERGENCY,
    ACTION_UNKNOWN

}


VALID_PRIORITIES = {

    PRIORITY_LOW,
    PRIORITY_NORMAL,
    PRIORITY_HIGH,
    PRIORITY_CRITICAL

}


VALID_SENTIMENTS = {

    SENTIMENT_POSITIVE,
    SENTIMENT_NEUTRAL,
    SENTIMENT_NEGATIVE

}


VALID_INTENTS = {

    INTENT_STRESS,
    INTENT_ANXIETY,
    INTENT_SLEEP,
    INTENT_BURNOUT,
    INTENT_WORK_LIFE_BALANCE,
    INTENT_MOTIVATION,
    INTENT_PRODUCTIVITY,
    INTENT_CAREER,
    INTENT_POLICY,
    INTENT_LEAVE,
    INTENT_LEAVE_POLICY,
    INTENT_COMPANY_POLICY,
    INTENT_WORK_FROM_HOME,
    INTENT_EMPLOYEE_BENEFITS,
    INTENT_GREETING,
    INTENT_GOODBYE,
    INTENT_GRATITUDE,
    INTENT_HELP,
    INTENT_GENERAL,
    INTENT_GENERAL_QUESTION,
    INTENT_EMERGENCY,
    INTENT_UNKNOWN

}


# =====================================================

def validate_response(
    parsed: ParsedResponse
):
    """
    Validate ParsedResponse.
    """

    # -----------------------------
    # Action
    # -----------------------------

    if parsed.action not in VALID_ACTIONS:

        parsed.action = ACTION_UNKNOWN

    # -----------------------------
    # Intent
    # -----------------------------

    if parsed.intent not in VALID_INTENTS:

        parsed.intent = INTENT_UNKNOWN

    # -----------------------------
    # Sentiment
    # -----------------------------

    if parsed.sentiment not in VALID_SENTIMENTS:

        parsed.sentiment = SENTIMENT_NEUTRAL

    # -----------------------------
    # Priority
    # -----------------------------

    if parsed.priority not in VALID_PRIORITIES:

        parsed.priority = PRIORITY_NORMAL

    # -----------------------------
    # Confidence
    # -----------------------------

    if parsed.confidence < 0:

        parsed.confidence = 0

    if parsed.confidence > 1:

        parsed.confidence = 1

    return parsed


# =====================================================

def print_validation(parsed: ParsedResponse):
    """
    Debug helper.
    """

    print()

    print("=" * 60)

    print("Validated Response")

    print("=" * 60)

    print("Action      :", parsed.action)

    print("Intent      :", parsed.intent)

    print("Sentiment   :", parsed.sentiment)

    print("Priority    :", parsed.priority)

    print("Confidence  :", parsed.confidence)

    print("Reason      :", parsed.reason)

    print("=" * 60)