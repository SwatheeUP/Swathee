import streamlit as st
from groq import Groq

# Initialize Groq client
client = Groq(api_key="api_key")

st.title("🤖 Groq LLM Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Add user message to history
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Show user message
    with st.chat_message("user"):
        st.write(user_input)

    # Send conversation to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    # Add assistant reply to history
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

    # Show assistant reply
    with st.chat_message("assistant"):
        st.write(reply)
