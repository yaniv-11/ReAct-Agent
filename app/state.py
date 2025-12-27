from typing import TypedDict, List, Optional, Literal

class react_state(TypedDict):
    input: str
    thoughts: List[str]
    reasons: List[str]
    action: Literal["search", "wikipedia", "none"]
    actions: List[str]  # History of actions for tracing
    action_inputs: List[str]
    observations: List[str]
    final: Optional[str]
    iteration: int
