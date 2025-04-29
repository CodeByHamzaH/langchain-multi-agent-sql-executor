from workflow.graph import build_graph

if __name__ == "__main__":
    instruction = input("Enter a task (e.g., 'Insert a new user into users table'):\n")

    graph = build_graph()
    final_state = graph.invoke({"instruction": instruction})

    print("\n===== Final Output =====")
    print(final_state["final_response"])

