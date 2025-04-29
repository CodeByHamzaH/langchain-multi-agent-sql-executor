#!/bin/bash

# Create folders
mkdir -p agents
mkdir -p workflow

# Create empty Python files
touch main.py config.py requirements.txt
touch agents/__init__.py
touch agents/agent_1_sql_generator.py
touch agents/agent_2_executor.py
touch agents/agent_3_validator.py
touch workflow/__init__.py
touch workflow/graph.py

# Populate requirements.txt
cat > requirements.txt <<EOL
langchain
langgraph
ollama
mysql-connector-python
EOL