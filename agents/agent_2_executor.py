from config import db

def agent_2_execute_sql(state):
    sql = state["sql_query"]
    try:
        print(sql)
        result = db.run(sql)
        state["execution_result"] = result
        state["execution_success"] = True
    except Exception as e:
        state["execution_result"] = str(e)
        state["execution_success"] = False
    return state