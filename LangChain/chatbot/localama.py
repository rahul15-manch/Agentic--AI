from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import os
import streamlit as st 
from dotenv import load_dotenv


llm = Ollama(
    model="llama3"
)

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to user queries."),
        ("human", "Question: {question}")
    ]
)

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Streamlit UI
st.title("Chat with llama3")

input_text = st.text_input("Search topic you want")

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)

