# LangChain Multi-Agent SQL Executor

This project demonstrates a multi-agent system built using LangChain, LangGraph, and OpenAI's GPT models.  
The system simulates a real-world task flow involving SQL generation, execution, and validation using three agents.

---

## 🧠 Project Structure

```
langchain-multi-agent-sql-executor/
│
├── agents/
│   ├── agent_1_sql_generator.py   # Agent 1: Generates SQL INSERT/UPDATE statements
│   ├── agent_2_executor.py        # Agent 2: Executes SQL statements on a real database
│   └── agent_3_validator.py       # Agent 3: Validates execution response and decides whether to retry
│
├── workflow/
│   └── graph.py                   # LangGraph workflow connecting the agents with conditional logic
│
├── config.py                      # LLM and database configuration
├── main.py                        # Entry point to run the multi-agent system
├── setup_project.sh               # Bash script to initialize project structure
└── README.md                      # Project documentation
```

---

## ⚙️ How It Works

1. **Agent 1** receives a high-level instruction and generates a corresponding SQL INSERT or UPDATE statement using OpenAI's GPT model.
2. **Agent 2** executes the generated SQL on a MySQL database.
3. **Agent 3** validates the execution result. If it fails, it triggers a retry loop by going back to Agent 1.
4. The process continues until the execution is successful.

---

## 🚀 Technologies Used

- **LangChain**: For LLM orchestration
- **LangGraph**: To define agent workflows and retry logic
- **OpenAI GPT-3.5/4**: For SQL generation and reasoning
- **MySQL**: Real database for executing SQL queries
- **Python 3.10+**

---

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/langchain-multi-agent-sql-executor.git
   cd langchain-multi-agent-sql-executor
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-api-key
   ```

5. Update your database connection string in `config.py`.

6. Run the system:
   ```bash
   python main.py
   ```

---

## ✅ Example Instruction

> "Insert a new user with id 101, name 'Alice', and email 'alice@example.com' into the users table."

---

## 📄 License

This project is licensed under the MIT License.
