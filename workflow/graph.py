from langgraph.graph import StateGraph
from agents.agent_1_sql_generator import agent_1_generate_sql
from agents.agent_2_executor import agent_2_execute_sql
from agents.agent_3_validator import agent_3_validate_result

def build_graph():
    graph = StateGraph()

    # Add nodes
    graph.add_node("generate_sql", agent_1_generate_sql)
    graph.add_node("execute_sql", agent_2_execute_sql)
    graph.add_node("validate_result", agent_3_validate_result)

    # Workflow edges
    graph.set_entry_point("generate_sql")
    graph.add_edge("generate_sql", "execute_sql")
    graph.add_edge("execute_sql", "validate_result")

    # Loop back to regenerate if validation fails
    graph.add_conditional_edges(
        "validate_result",
        lambda state: "retry" if state.get("retry") else "done",
        {
            "retry": "generate_sql",
            "done": None,
        }
    )

    return graph.compile()

