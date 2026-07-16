"""
test_semantic_search.py
"""

from rag.semantic_search import SemanticSearch

search = SemanticSearch()

print("=" * 70)
print("WORKWELL AI - SEMANTIC SEARCH TEST")
print("=" * 70)

while True:

    query = input("\nEnter Question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    results = search.search(query)

    if not results:

        print("\n❌ No relevant documents found.")
        continue

    print(f"\nFound {len(results)} result(s)\n")

    for i, result in enumerate(results, start=1):

        print("=" * 70)
        print(f"Result {i}")
        print("=" * 70)

        print("Document :", result["document"])
        print("Category :", result["category"])
        print("Chunk ID :", result["chunk_id"])
        print("Distance :", round(result["distance"], 3))

        print()
        print(result["text"])
        print()