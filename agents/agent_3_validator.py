def agent_3_validate_result(state):
    if state["execution_success"]:
        state["final_response"] = f"✅ Query successful:\n{state['execution_result']}"
        state["retry"] = False
    else:
        state["final_response"] = f"❌ Query failed:\n{state['execution_result']}"
        state["retry"] = True
    return state