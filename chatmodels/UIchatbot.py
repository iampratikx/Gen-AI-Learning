
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 My AI Chatbot")
st.caption("Powered by Ollama + Qwen3 4B")

# Sidebar settings
with st.sidebar:
    st.header("⚙️ Chat Settings")

    mode = st.selectbox(
        "Choose your AI personality",
        ["Funny", "Sad", "Happy"],
    )

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=1.5,
        value=0.6,
        step=0.1,
    )

    num_predict = st.slider(
        "Maximum response tokens",
        min_value=64,
        max_value=1024,
        value=512,
        step=64,
    )

    num_ctx = st.selectbox(
        "Context length",
        [2048, 4096],
        index=1,
    )

    top_p = st.slider(
        "Top P",
        min_value=0.1,
        max_value=1.0,
        value=0.9,
        step=0.05,
    )

    top_k = st.slider(
        "Top K",
        min_value=1,
        max_value=100,
        value=40,
    )

    repeat_penalty = st.slider(
        "Repeat penalty",
        min_value=1.0,
        max_value=2.0,
        value=1.1,
        step=0.1,
    )

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Model: qwen3:4b-instruct-2507-q4_K_M")

# Personality instructions
personalities = {
    "Funny": (
        "You are a funny AI assistant. "
        "Use light humor and witty responses when appropriate. "
        "Still answer questions clearly and accurately."
    ),
    "Sad": (
        "You are a calm, melancholic AI assistant. "
        "Use a gentle and reflective tone while remaining helpful "
        "and accurate."
    ),
    "Happy": (
        "You are a cheerful and positive AI assistant. "
        "Be friendly, encouraging, and helpful while remaining accurate."
    ),
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your message here...")

if prompt:
    # Display and save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Create model with selected settings
    llm = ChatOllama(
        model="qwen3:4b-instruct-2507-q4_K_M",
        temperature=temperature,
        num_predict=num_predict,
        num_ctx=num_ctx,
        top_p=top_p,
        top_k=top_k,
        repeat_penalty=repeat_penalty,
    )

    # Build conversation history for LangChain
    chat_messages = [
        SystemMessage(content=personalities[mode])
    ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_messages.append(
                HumanMessage(content=msg["content"])
            )
        else:
            chat_messages.append(
                AIMessage(content=msg["content"])
            )

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                response = llm.invoke(chat_messages)
                answer = response.content.strip()

                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(
                    f"Error: {type(e).__name__}: {e}"
                )
                st.info(
                    "Check whether Ollama is running and "
                    "the selected model is installed."
                )
