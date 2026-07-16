from rag.rag_engine import RAGEngine

rag = RAGEngine()

while True:

    q = input("\nQuestion: ")

    if q.lower() == "exit":
        break

    try:

        result = rag.answer_question(q)

        print("\n" + "=" * 70)
        print("ANSWER")
        print("=" * 70)

        print(result["answer"])

        print("\n" + "=" * 70)
        print("SOURCES")
        print("=" * 70)

        for source in result["sources"]:
            print(source)

    except Exception as e:

        print("\nERROR")
        print(type(e).__name__)
        print(e)