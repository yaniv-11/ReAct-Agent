# app/nodes/tools.py
from app.state import react_state
from app.tools import wikipedia
from app.tools import search

def wikipedia_node(state: react_state) -> react_state:
    """
    Executes Wikipedia tool and appends observation.
    """

    query = state["action_inputs"][-1]

    if not query:
        state["observations"].append("Wikipedia tool called with empty query.")
        return state

    try:
        result = wikipedia(query)
        state["observations"].append(result)
    except Exception as e:
        state["observations"].append(f"Wikipedia error: {str(e)}")

    return state


def search_node(state: react_state) -> react_state:
    """
    Executes Search tool and appends observation.
    """

    query = state["action_inputs"][-1]

    if not query:
        state["observations"].append("Search tool called with empty query.")
        return state

    try:
        result = search(query)
        state["observations"].append(result)
    except Exception as e:
        state["observations"].append(f"Search error: {str(e)}")

    return state
