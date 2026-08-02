"""
constants.py

Global constants used throughout WorkWell AI.
"""

# =====================================================
# ACTIONS
# =====================================================

ACTION_GREETING = "greeting"

ACTION_GOODBYE = "goodbye"

ACTION_HELP = "help"

ACTION_GENERAL = "general"

ACTION_RECOMMENDATION = "recommendation"

ACTION_RAG = "rag"

ACTION_EMERGENCY = "emergency"

ACTION_UNKNOWN = "unknown"

# =====================================================
# PRIORITY
# =====================================================

PRIORITY_LOW = "low"

PRIORITY_NORMAL = "normal"

PRIORITY_HIGH = "high"

PRIORITY_CRITICAL = "critical"

# =====================================================
# SENTIMENT
# =====================================================

SENTIMENT_POSITIVE = "positive"

SENTIMENT_NEUTRAL = "neutral"

SENTIMENT_NEGATIVE = "negative"

# =====================================================
# USER INTENTS
# =====================================================

INTENT_STRESS = "stress"

INTENT_ANXIETY = "anxiety"

INTENT_SLEEP = "sleep"

INTENT_BURNOUT = "burnout"

INTENT_WORK_LIFE_BALANCE = "work_life_balance"

INTENT_MOTIVATION = "motivation"

INTENT_PRODUCTIVITY = "productivity"

INTENT_CAREER = "career"

INTENT_POLICY = "policy"

INTENT_LEAVE = "leave"

INTENT_LEAVE_POLICY = "leave_policy"

INTENT_COMPANY_POLICY = "company_policy"

INTENT_WORK_FROM_HOME = "work_from_home"

INTENT_EMPLOYEE_BENEFITS = "employee_benefits"

INTENT_GREETING = "greeting"

INTENT_GOODBYE = "goodbye"

INTENT_GRATITUDE = "gratitude"

INTENT_HELP = "help"

INTENT_GENERAL = "general"

INTENT_GENERAL_QUESTION = "general_question"

INTENT_EMERGENCY = "emergency"

INTENT_UNKNOWN = "unknown"

# =====================================================
# RESPONSE TYPES
# =====================================================

RESPONSE_GENERAL = "general"

RESPONSE_RECOMMENDATION = "recommendation"

RESPONSE_RAG = "rag"

RESPONSE_EMERGENCY = "emergency"

# =====================================================
# MEMORY ROLES
# =====================================================

ROLE_USER = "user"

ROLE_ASSISTANT = "assistant"

ROLE_SYSTEM = "system"

# =====================================================
# KNOWLEDGE CATEGORIES
# =====================================================

CATEGORY_HR = "hr"

CATEGORY_FAQ = "faq"

CATEGORY_WELLNESS = "wellness"

CATEGORY_GENERAL = "general"

# =====================================================
# SUPPORTED FILE TYPES
# =====================================================

SUPPORTED_DOCUMENTS = [
    ".txt"
]

# =====================================================
# DEFAULT MESSAGES
# =====================================================

DEFAULT_RAG_MESSAGE = (
    "I couldn't find that information in the company's knowledge base."
)

DEFAULT_ERROR_MESSAGE = (
    "I'm sorry, something went wrong while processing your request."
)

DEFAULT_GREETING = (
    "Hello! I'm WorkWell AI Assistant. How can I help you today?"
)

DEFAULT_GOODBYE = (
    "Take care! Have a wonderful day."
)