# Ollama AI ChatBot

## Overview

Ollama AI ChatBot is a simple chatbot application built using Streamlit and the Ollama API. It provides an interactive chat interface where users can communicate with an AI assistant powered by the "tinyllama" model.

## Features

- Chat-based interface with a user-friendly design
- Streamed responses for a smooth conversation experience
- Persistent chat history during the session
- Uses Ollama's "tinyllama" model for AI responses

## Installation

To run this chatbot locally, follow these steps:

1. **Clone the repository**

   ```sh
   git clone https://github.com/mujtabachandio/ollama_streamlit_python.git
   cd ollama_streamlit_python
   ```

2. **Install dependencies**
   Ensure you have Python installed, then install the required packages:

   ```sh
   uv pip install streamlit ollama
             or
   pip install streamlit ollama
   ```

3. **Run the chatbot**

   ```sh
   streamlit run app_name.py
   ```

## Usage

- Start the chatbot by running the above command.
- Type your message in the chat input field.
- The chatbot will respond using the Ollama API.
- Chat history is maintained during the session but resets upon refresh.

## Code Structure

- **Initialize Chat History**: Stores past messages in `st.session_state`.
- **Display Chat Messages**: Shows messages with user and assistant avatars.
- **Generate Responses**: Calls Ollama's API to generate AI responses.
- **Streamed Output**: Messages are displayed in real-time for better user experience.

## Requirements

- Python 3.x
- Streamlit
- Ollama API access

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests.

## License

This project is licensed under the MIT License.

---

Developed with ❤️ using Streamlit and Ollama
