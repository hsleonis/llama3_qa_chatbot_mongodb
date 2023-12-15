from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
from mongodb import EasyMongo
from llm_strings import LLMStrings
from utils import output_text, simulate_response, create_message

load_dotenv()


if __name__ == '__main__':
    # Get LLM model
    llm = Ollama(
        model=os.getenv("LLM_MODEL"), callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )

    # App title
    st.title(LLMStrings.APP_TITLE)

    # Initial prompt
    with st.chat_message(LLMStrings.AI_ROLE):
        st.write(LLMStrings.GREETINGS)

    # Initialize chat history
    if LLMStrings.SESSION_STATES not in st.session_state:
        st.session_state.messages = []

    # Connect MongoDB
    mongo_server = EasyMongo()
    collection_name = mongo_server.get_collection()

    # Display chat messages from history on app rerun
    messages = collection_name.find()
    for message in messages:
        with st.chat_message(message[LLMStrings.ROLE_ID]):
            st.markdown(message[LLMStrings.CONTENT])

    # React to user input
    if prompt := st.chat_input(LLMStrings.INPUT_PLACEHOLDER):

        # Display user message in chat message container
        with st.chat_message(LLMStrings.USER_ROLE):
            st.markdown(prompt)
            # Add user message to chat history
            user_content = create_message(LLMStrings.USER_ROLE, prompt)
            st.session_state.messages.append(user_content)

        with st.spinner(LLMStrings.WAIT_MESSAGE):
            with st.chat_message(LLMStrings.AI_ROLE):
                # Get response and display
                response = output_text(llm, prompt)

                # Add user message to chat history
                ai_content = create_message(LLMStrings.AI_ROLE, response)
                st.session_state.messages.append(ai_content)

                # Simulate stream of response with milliseconds delay
                simulate_response(response)

                # Insert messages to MongoDB
                mongo_server.insert_many([user_content, ai_content])
