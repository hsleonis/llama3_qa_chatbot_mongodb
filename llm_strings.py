"""
Module: llm_strings.py
Description: A class that contains various strings for use for the LLM Chatbot.
"""


class LLMStrings:
    """
    A brief description of the MyClass class.
    """

    # Q&A strings
    PROMPT_TEMPLATE = "You are a question-answer chatbot named: Yollama. Answer this:"
    GREETINGS = "Greetings, esteemed visitor. Welcome to the realm of sagacity and charm. " \
                "I am Yollama! The venerable guardian of this meadow. " \
                "What brings you to my domain on this splendid day?"
    WAIT_MESSAGE = "Sit back, relax and prepare for a llama-zing experience as you wait for Yollama's responses!"
    INPUT_PLACEHOLDER = "Ask, and Yollama shall llama-swer!"

    # Streamlit strings
    APP_TITLE = "Llamagination Station"
    SESSION_STATES = "messages"

    # MongoDB strings
    USER_ROLE = "user"
    AI_ROLE = "assistant"
    ROLE_ID = "role"
    CONTENT = "content"

    @staticmethod
    def get_application_version():
        """
        Return the current version of the application.

        :return: The version string.
        :rtype: str
        """
        return "1.0.0"
