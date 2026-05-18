from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms import Ollama

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"

app=FastAPI(
    version="1.0.0",
    description="Simple API Server",
    title="Langchain Server"
)


llm=Ollama(model="llama3")

prompt1=ChatPromptTemplate.from_template("write essay about {topic}")

output=StrOutputParser()

add_routes(
    app,
    prompt1|llm|output,
    path="/essay"
)

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)