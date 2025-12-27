# test_agent.py
from app.graph import react_agent
from app.state_init import create_initial_state

state = create_initial_state(
    "What is the capital of the country where Messi was born?"
)

final_state = react_agent.invoke(state)

print("\nFINAL ANSWER:")
print(final_state["final"])

print("\nTRACE:")
for i, thought in enumerate(final_state["thoughts"], 1):
    print(f"Step {i}:")
    print(" Thought:", thought)
    print(" Action:", final_state["actions"][i-1])
    print(" Reason:", final_state["reasons"][i-1])
    if i-1 < len(final_state["observations"]):
        print(" Observation:", final_state["observations"][i-1])
    print()
