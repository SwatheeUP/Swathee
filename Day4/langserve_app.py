import os
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
app=FastAPI()
llm=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key="api_key")
add_routes(app,llm,path="/chat")

