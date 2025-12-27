from typing import List, Literal
from app.state import react_state

def create_initial_state(user_query: str) -> react_state:
    return {
        "input": user_query,
        "thoughts": [],
        "reasons": [],
        "action": "none",
        "actions": [],
        "action_inputs": [],
        "observations": [],
        "final": None,
        "iteration": 0
    }