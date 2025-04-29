from langchain.llms import Ollama
from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv() 

# Ollama with LLaMA 3 (21B)
# llm = Ollama(model="llama3:latest")

# Load OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4",  # or "gpt-3.5-turbo"
    temperature=0,
)
from langchain.utilities.sql_database import SQLDatabase
# Replace with your actual MySQL connection string
db = SQLDatabase.from_uri("mysql+mysqlconnector://admin:password@localhost/user_management")