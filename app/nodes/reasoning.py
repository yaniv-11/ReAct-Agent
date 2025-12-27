from app.llm import llm,parser
from app.state import react_state
from app.prompts import reasoning_prompt
from app.schema import reasoning_output


MAX_ITER = 5

def reasoning(state: react_state) -> react_state:
    state['iteration'] += 1
    
    
    if state["iteration"] >= MAX_ITER:
        state["thoughts"].append(
            "Maximum iterations reached. Providing best-effort final answer."
        )
        state["reasons"].append(
            "Iteration limit exceeded to prevent infinite loop."
        )
        state["action"] = "none"
        state["actions"].append("none")
        state["action_inputs"].append("")

        if state["observations"]:
            state["final"] = state["observations"][-1]
        else:
            state["final"] = (
                "Unable to find sufficient information within the allowed steps."
            )

        return state
    
    
    llm_input = {
        "input": state['input'],
        "thoughts": state['thoughts'],
        "observations": state['observations']
    }
    prompt = reasoning_prompt + "\n\n" + str(llm_input)
    
    raw = llm.invoke(prompt)
    text = raw.content if hasattr(raw, "content") else raw
    decision: reasoning_output = parser.parse(text)
    
    
    state["thoughts"].append(decision.thoughts)
    state["action"] = decision.action
    state["actions"].append(decision.action)    
    state["reasons"].append(decision.reasons)
    state["action_inputs"].append(decision.action_inputs)

    if decision.action == "none":
        state["final"] = decision.final
        
    print("LLM Response:", decision)

    return state
    
    
      
    
    