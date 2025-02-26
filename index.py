import streamlit as st
import ollama 

st.set_page_config(page_title="Ollama AI ChatBot", layout="centered")

st.header("💬 Ollama AI ChatBot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I am Ollama, your AI ChatBot. How can I help you today?"}]

# Display messages in a chat-like format
for msg in st.session_state.messages:
    avatar = "🙍‍♂️" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

def generate_response(user_input):
    """Generate chatbot response using Ollama API"""
    st.session_state["full_message"] = ""  # Initialize full message storage
    response = ollama.chat(model="tinyllama", stream=True, messages=st.session_state.messages + [{"role": "user", "content": user_input}])
    
    for partial_resp in response:
        token = partial_resp["message"]["content"]
        st.session_state["full_message"] += token
        yield token

# Text input at the bottom of the screen
if prompt := st.chat_input("Type a message..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user", avatar="🙍‍♂️"):
        st.write(prompt)

    # Generate AI response
    with st.chat_message("assistant", avatar="🤖"):
        response_text = st.write_stream(generate_response(prompt))

    # Store AI response in session state
    st.session_state.messages.append({"role": "assistant", "content": st.session_state["full_message"]})
