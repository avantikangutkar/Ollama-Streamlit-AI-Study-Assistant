import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🤖",
    layout="centered"
)

# Title
st.title("🤖 AI Study Assistant")
st.write("Ask a question and get an answer from the local Llama 3.2 model.")

# User input
prompt = st.text_area(
    "Enter your question:",
    placeholder="Example: Explain artificial intelligence in simple words."
)

# Generate response
if st.button("Generate Answer"):
    if prompt.strip():
        with st.spinner("Generating response..."):
            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.subheader("AI Response")
        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a question first.")