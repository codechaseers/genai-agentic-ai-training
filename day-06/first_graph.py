from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    name: str
    account_type: str
    message: str


state = {
    "name": "Asha",
    "account_type": "",
    "message": ""
}

def greet(state):
    state["message"] = f"Hello {state['name']}!"
    return state


def set_account_type(state):
    state["account_type"] = "savings"
    return state

def compose(state):
    state["message"] = (
        f"{state['message']} "
        f"Your account type is {state['account_type']}."
    )
    return state


graph = StateGraph(State)


graph.add_node("greet", greet)
graph.add_node("set_account_type", set_account_type)
graph.add_node("compose", compose)


graph.add_edge(START, "greet")
graph.add_edge("greet", "set_account_type")
graph.add_edge("set_account_type", "compose")
graph.add_edge("compose", END)

app = graph.compile()

result = app.invoke({
    "name": "Asha",
    "account_type": "",
    "message": ""
})

print(result)