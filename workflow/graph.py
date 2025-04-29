from langgraph.graph import StateGraph
from agents.agent_1_sql_generator import agent_1_generate_sql
from agents.agent_2_executor import agent_2_execute_sql
from agents.agent_3_validator import agent_3_validate_result
from typing import TypedDict, Optional

# Define state schema
class GraphState(TypedDict, total=False):
    instruction: str
    sql_query: str
    execution_result: str
    execution_success: bool
    final_response: str
    retry: bool

def build_graph():
    graph = StateGraph(state_schema=GraphState)

    graph.add_node("generate_sql", agent_1_generate_sql)
    graph.add_node("execute_sql", agent_2_execute_sql)
    graph.add_node("validate_result", agent_3_validate_result)

    graph.set_entry_point("generate_sql")
    graph.set_finish_point("validate_result")  # ✅ mark end of the graph

    graph.add_edge("generate_sql", "execute_sql")
    graph.add_edge("execute_sql", "validate_result")

    graph.add_conditional_edges(
        "validate_result",
        lambda state: "retry" if state.get("retry") else "done",
        {
            "retry": "generate_sql",
            "done": "validate_result",  # just loop to itself as finish
        }
    )

    return graph.compile()
