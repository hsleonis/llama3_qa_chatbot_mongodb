# llama2_qa_chatbot_mongodb
Llama2 in MongoDB: Conversational QA App

Features:

1. **Language Model Integration**:
        The app integrates the Ollama language model (LLM) for natural language processing. The model is initialized with a specified Ollama model and a callback manager for handling streaming standard output.

2. **User Interface**:
        The app's user interface is created using Streamlit. Users can input messages through the chat input interface. User messages are displayed in the chat, and the messages are added to the chat history.

3. **Chat Initialization**:
        The app starts with an initial prompt in the chat, displaying a greeting message. The chat history is initialized if it doesn't exist in the session state.

4. **MongoDB Integration**:
        The app connects to MongoDB Atlas server. It retrieves the collection name and displays chat messages from the database on app rerun. The messages are fetched and displayed in the chat history container.

5. **Response Processing**:
        The app processes user input by obtaining a response from the Ollama language model. The response is then displayed in the chat interface, and the messages are added to the chat history.

6. **Streaming Simulation**:
        The app simulates the streaming of the AI's response with a spinner to indicate processing. The simulate_response function adds a delay to simulate a more dynamic chat experience.

7. **MongoDB Logging**:
        All user and AI messages are inserted into the MongoDB collection for logging and retrieval.
