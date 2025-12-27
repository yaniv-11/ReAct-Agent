from app.graph import react_agent
import sys

def main():
    query = "What is the capital of the country where Messi was born?"

    # Initialize state with all required fields
    initial_state = {
        "input": query,
        "reasons": [],
        "iteration": 0,  
        "final": "",
        "thoughts": [],
        "action": "",
        "action_inputs": [],
        "observations": [],
        "actions": [],
    }

    print(f"\n{'='*60}")
    print(f"Starting ReAct Agent")
    print(f"Query: {query}")
    print(f"{'='*60}\n")

    # Invoke the graph
    try:
        state = react_agent.invoke(initial_state)
    except Exception as e:
        print(f"\n[ERROR] Graph execution failed: {e}")
        import traceback
        traceback.print_exc()
        return

    # Display the reasoning trace
    print(f"\n{'='*60}")
    print("REASONING TRACE")
    print(f"{'='*60}\n")
    
    for i, thought in enumerate(state["thoughts"], 1):
        print(f"┌─ Step {i}")
        print(f"│   Thought: {thought}")
        if i-1 < len(state["actions"]):
            print(f"│   Action: {state['actions'][i-1]}")
        if i-1 < len(state["action_inputs"]):
            action_input = state["action_inputs"][i-1] or ""
            print(f"│   Input: {action_input[:80]}{'...' if len(action_input) > 80 else ''}")
        if i-1 < len(state["reasons"]):
            print(f"│   Reason: {state['reasons'][i-1]}")
        if i-1 < len(state["observations"]):
            observation = state["observations"][i-1] or ""
            if observation:
                obs_preview = observation[:200]
                if len(observation) > 200:
                    obs_preview += f"... (+{len(observation)-200} more chars)"
                print(f"│   Observation: {obs_preview}")
        print(f"└{'─'*58}")
        print()

    # Display final answer
    print(f"\n{'='*60}")
    print(" FINAL ANSWER")
    print(f"{'='*60}")
    
    if state.get("final"):
        print(state["final"])
    else:
        print("❌ No final answer generated.")
        print("The agent may have encountered an error.")
    
    print(f"\n{'='*60}")
    print(f"Total iterations: {state['iteration']}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()