import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("Gemini AI Q/A App")

# Input box for Gemini AI API key
gemini_api_key = st.sidebar.text_input("Gemini AI API Key", type="password")

def validate_api_key(api_key):
    # Simple validation, adjust as needed
    return api_key is not None and api_key!= ""

def generate_response(input_text, api_key):
    if not validate_api_key(api_key):
        st.warning("Please enter your Gemini AI API key!", icon="⚠")
        return
    
    model = ChatGoogleGenerativeAI(model="gemini-pro", api_key=api_key)
    response = model.invoke(input_text)
    return response.content

with st.form("my_form"):
    question = st.text_area("Enter your question:", "")
    submitted = st.form_submit_button("Submit")

if submitted and validate_api_key(gemini_api_key):
    response = generate_response(question, gemini_api_key)
    st.write(response)