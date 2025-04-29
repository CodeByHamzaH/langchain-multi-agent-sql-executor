# LangChain Multi-Agent SQL Executor

This project demonstrates a multi-agent system using LangChain and OpenAI API.  
The agents work together to:
- Generate SQL queries (Agent 1)
- Execute the queries on a real database (Agent 2)
- Validate the response and retry on failure (Agent 3)

## Features
- Uses LangGraph for multi-agent workflows
- ChatOpenAI (GPT-4 / GPT-3.5) as LLM
- Real SQL execution with MySQL
- Retry loop until successful execution

## Setup
Refer to the provided `setup_project.sh` to initialize project structure and dependencies.

## How to Run

```bash
python main.py
```

## License
MIT
