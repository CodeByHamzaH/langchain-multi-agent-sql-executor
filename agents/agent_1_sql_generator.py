from config import llm

def agent_1_generate_sql(state):
    instruction = state["instruction"]
    prompt = f"Generate an SQL INSERT or UPDATE query based on this instruction:\n{instruction}"
    sql_query = llm(prompt)
    state["sql_query"] = sql_query
    return state