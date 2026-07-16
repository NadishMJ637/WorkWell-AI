"""
app.py

Entry point for the WorkWell AI Assistant.
"""

from ai_engine import AIEngine


def main():

    engine = AIEngine()

    print("=" * 60)
    print("      WorkWell AI Assistant")
    print("=" * 60)
    print("Type 'exit' to quit.\n")

    while True:

        user_message = input("You : ")

        if user_message.strip().lower() == "exit":
            break

        try:

            response = engine.process(user_message)

            print(f"\nAssistant : {response}\n")

            engine.show_history()

            print("=" * 60)

        except Exception as error:

            print("\nError:")
            print(error)


if __name__ == "__main__":
    main()