"""
test_indexer.py

Tests the indexing process for WorkWell AI.
"""

from rag.indexer import DocumentIndexer

print("=" * 70)
print("WORKWELL AI - INDEXER TEST")
print("=" * 70)

indexer = DocumentIndexer()

try:
    # Build the index
    indexer.build_index()

    print("\n" + "=" * 70)
    print("INDEXING SUCCESSFUL")
    print("=" * 70)

    # Print statistics
    indexer.statistics()

    print("\nIndexed Documents:")
    print(indexer.store.list_documents())

    print("\nTotal Chunks:")
    print(indexer.store.count())

except Exception as e:
    print("\n❌ INDEXING FAILED")
    print(type(e).__name__)
    print(e)