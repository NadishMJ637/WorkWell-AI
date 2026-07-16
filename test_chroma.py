from rag.chroma_store import ChromaStore

store = ChromaStore()

print("=" * 60)
print("CHROMA DATABASE")
print("=" * 60)

print("Total Chunks:", store.count())

print()

print("Documents:")

try:
    print(store.list_documents())
except Exception as e:
    print(e)