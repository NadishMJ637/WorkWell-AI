"""
config.py

Global configuration for WorkWell AI.
"""

# =====================================================
# APPLICATION
# =====================================================

APP_NAME = "WorkWell AI"
VERSION = "2.0"

# =====================================================
# MODELS
# =====================================================

# Analysis Model (Intent Detection)
ANALYSIS_MODEL = "qwen2.5:1.5b"

# Chat Model (Natural Response)
CHAT_MODEL = "llama3.2:3b"

# Embedding Model
EMBED_MODEL = "nomic-embed-text"

# =====================================================
# KNOWLEDGE BASE
# =====================================================

KNOWLEDGE_FOLDER = "knowledge"

# =====================================================
# RECOMMENDATIONS
# =====================================================

RECOMMENDATION_FILE = "data/recommendations.json"

# =====================================================
# RAG
# =====================================================

TOP_K = 1

# ChromaDB is using L2 distance.
# Currently we don't filter by similarity.
SIMILARITY_THRESHOLD = None

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# =====================================================
# CHROMADB
# =====================================================

CHROMA_DB_PATH = "rag_db"

CHROMA_COLLECTION = "workwell_knowledge"

# =====================================================
# MEMORY
# =====================================================

MAX_HISTORY = 6

# =====================================================
# RESPONSE
# =====================================================

MAX_RESPONSE_WORDS = 150

# =====================================================
# DEBUG
# =====================================================

DEBUG = True