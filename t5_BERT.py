import streamlit as st
import PyPDF2
from transformers import T5Tokenizer, T5ForConditionalGeneration, pipeline

# Initialize models and tokenizers
t5_tokenizer = T5Tokenizer.from_pretrained('t5-small')
t5_model = T5ForConditionalGeneration.from_pretrained('t5-small')
qa_pipeline = pipeline('question-answering', model='bert-large-uncased', tokenizer='bert-large-uncased')

def extract_text_from_pdf(pdf_file):
    """Extract text from the uploaded PDF file."""
    text = ""
    with pdf_file as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text):
    """Summarize the given text using T5."""
    inputs = t5_tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    outputs = t5_model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = t5_tokenizer.decode(outputs[0], skip_special_tokens=True)
    return summary

def answer_question(question, context):
    """Answer a question based on the context using BERT."""
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Streamlit app
st.title("PDF Summarizer and Question Answering")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    text = extract_text_from_pdf(uploaded_file)
    
    # Limit the text displayed to 500 characters
    display_text = text[:500] + ('...' if len(text) > 500 else '')
    
    # Display the extracted text
    st.subheader("Extracted Text")
    st.text_area("Text from PDF", display_text, height=300)

    # Summarize text
    if st.button("Summarize"):
        summary = summarize_text(text)
        st.subheader("Summary")
        st.write(summary)
    
    # Answer questions
    question = st.text_input("Enter your question about the PDF:")
    if question:
        answer = answer_question(question, text)
        st.subheader("Answer")
        st.write(answer)