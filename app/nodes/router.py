from app.state import react_state

def router(state: react_state) -> react_state:
    action = state['action']
    if action == "wikipedia":
        return "wikipedia"
    elif action == "search":
        return "search"
    elif action == "none":
        return "end"
    else:
        raise ValueError(f"Unknown action: {action}")
    return state