"""
history.py

Conversation memory for WorkWell AI.
"""

from config import MAX_HISTORY

from constants import (
    ROLE_USER,
    ROLE_ASSISTANT,
    ROLE_SYSTEM
)


class ConversationHistory:
    """
    Stores conversation history.
    """

    def __init__(self):

        self.messages = []

    # =====================================================

    def add_user_message(
        self,
        message: str
    ):
        """
        Add user message.
        """

        self.messages.append({

            "role": ROLE_USER,

            "content": message

        })

        self._trim()

    # =====================================================

    def add_assistant_message(
        self,
        message: str
    ):
        """
        Add assistant message.
        """

        self.messages.append({

            "role": ROLE_ASSISTANT,

            "content": message

        })

        self._trim()

    # =====================================================

    def add_system_message(
        self,
        message: str
    ):
        """
        Add system message.
        """

        self.messages.append({

            "role": ROLE_SYSTEM,

            "content": message

        })

        self._trim()

    # =====================================================

    def get_messages(self):
        """
        Return complete history.
        """

        return self.messages

    # =====================================================

    def get_formatted_history(self):
        """
        Convert conversation into text.
        """

        if not self.messages:

            return ""

        history = []

        for message in self.messages:

            role = message["role"].capitalize()

            history.append(

                f"{role}: {message['content']}"

            )

        return "\n".join(history)

    # =====================================================

    def last_user_message(self):
        """
        Return latest user message.
        """

        for message in reversed(self.messages):

            if message["role"] == ROLE_USER:

                return message["content"]

        return ""

    # =====================================================

    def last_assistant_message(self):
        """
        Return latest assistant message.
        """

        for message in reversed(self.messages):

            if message["role"] == ROLE_ASSISTANT:

                return message["content"]

        return ""

    # =====================================================

    def clear(self):
        """
        Clear conversation history.
        """

        self.messages.clear()

    # =====================================================

    def size(self):
        """
        Number of stored messages.
        """

        return len(self.messages)

    # =====================================================

    def _trim(self):
        """
        Keep only recent conversation.
        """

        if len(self.messages) > MAX_HISTORY:

            self.messages = self.messages[-MAX_HISTORY:]

    # =====================================================

    def print_history(self):
        """
        Debug helper.
        """

        print()

        print("=" * 60)

        print("Conversation History")

        print("=" * 60)

        if not self.messages:

            print("No messages.")

        else:

            for message in self.messages:

                print(

                    f"{message['role'].capitalize()}: "

                    f"{message['content']}"

                )

        print("=" * 60)