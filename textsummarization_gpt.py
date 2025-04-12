import streamlit as st
import openai
import os

# Set OpenAI API Key (Replace with your actual key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App Title
st.title(" AI Text Summarization App (Powered by GPT-4)")

# User input for text to summarize
text = st.text_area("Enter text to summarize:", height=200)

# Summary length selection
summary_length = st.radio("Select Summary Length:", ["Short", "Medium", "Detailed"])

# Define token limits based on summary length
length_map = {
    "Short": 50,
    "Medium": 100,
    "Detailed": 200
}
# Generate summary function using GPT-4

def summarize_text(text, max_tokens):
    prompt = f"Summarize the following text in a concise and clear manner:\n\n{text}"
    client = openai.OpenAI()  # Create an OpenAI client instance
    response = client.chat.completions.create(
        model="gpt-4",  # Using GPT-4 model
        messages=[
            {"role": "system", "content": "You are an expert summarizer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content.strip()
 
# Summarization button
if st.button("Summarize"):
    if text:
        st.subheader(" Summarized Text:")
        summary = summarize_text(text, length_map[summary_length])
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
 