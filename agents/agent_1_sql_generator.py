from config import llm
from langchain.schema import HumanMessage

def agent_1_generate_sql(state):
    instruction = state["instruction"]
    messages = [HumanMessage(content=f"Generate an SQL INSERT or UPDATE query where 'user' schema contains (firstname, lastname, mobile, address):\n{instruction}")]
    sql_query = llm(messages).content
    state["sql_query"] = sql_query
    return state