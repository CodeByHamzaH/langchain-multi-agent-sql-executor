from langchain.llms import Ollama
from langchain.utilities.sql_database import SQLDatabase

# Ollama with LLaMA 3 (21B)
llm = Ollama(model="llama3:21b")

# Replace with your actual MySQL connection string
db = SQLDatabase.from_uri("mysql+mysqlconnector://admin:password@localhost/user_management")