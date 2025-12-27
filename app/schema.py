from typing import  Optional,Literal
from pydantic import BaseModel

class reasoning_output(BaseModel):
    thoughts: str
    action: Literal["wikipedia", "search", "none"]
    reasons: str
    action_inputs: Optional[str] 
    final: Optional[str] 