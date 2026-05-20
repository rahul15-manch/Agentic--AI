from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("human", "Question: {question}")
    ]
)


output_parser = StrOutputParser()


chain = prompt | llm | output_parser


st.title("Chat with Gemini")

input_text = st.text_input("Search topic you want")

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)