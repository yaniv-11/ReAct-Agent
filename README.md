🧠 ReAct Agent with LangGraph: A Stateful, Tool-Driven Reasoning Agent
This project implements a true ReAct (Reason → Act → Observe → Reason) agent using LangGraph, designed to perform multi-step reasoning, dynamic tool selection, and robust failure recovery.

Unlike single-prompt LLM demos, this agent explicitly models state, control flow, and tool execution, making it closer to how real-world agentic AI systems are built.


<img width="376" height="273" alt="image" src="https://github.com/user-attachments/assets/b5baf740-6718-400d-b5cc-cc5694cbe6ee" />



🎯 Why This Project Exists
Most LLM-based agents:

❌ Hide reasoning inside a single prompt

❌ Fail silently when tools return irrelevant results

❌ Loop indefinitely without safeguards

❌ Are hard to debug or extend

This project solves those issues by:

✅ Making reasoning explicit and traceable

✅ Separating decision-making from execution

✅ Using a graph-based control flow

✅ Enforcing iteration limits and schema validation

🏗️ Core Concepts Implemented
ReAct reasoning loop (Reason → Act → Observe)

Graph-based orchestration with LangGraph

Dynamic routing between tools and termination

Explicit agent state shared across iterations

Tool failure detection and recovery

Structured output parsing (HF-compatible)

Pretty iteration logs for full transparency


🧭 Design Principles
Reasoning ≠ Execution – LLM thinks, tools act

Tools produce observations – Results feed back into reasoning

State flows through every node – Full traceability

Termination is an explicit action (none) – Controlled stopping

📋 Agent State
The agent maintains a shared state across iterations:

python
{
    "input": str,
    "thoughts": List[str],
    "reasons": List[str],
    "actions": List[str],
    "action_inputs": List[str],
    "observations": List[str],
    "final_answer": Optional[str],
    "iteration": int
}
This enables:

✅ Step-by-step traceability

✅ Debugging and inspection

✅ Deterministic behavior

🔄 ReAct Execution Flow
For each iteration:

Reasoning Node

Consumes current state

Decides the next action (wikipedia, search, or none)

Outputs structured reasoning

Router

Routes execution based on the chosen action

Tool Node

Executes the external tool

Appends the observation to state

Loop

Control returns to reasoning

Stops when action is none or max iterations reached

🔧 Tools
Wikipedia – Encyclopedic factual queries

Search – Fallback for ambiguous or failed results

Tools are implemented as independent nodes, keeping execution isolated from reasoning logic.

🛡️ Structured Output & Validation
Since HuggingFace models do not support native function calling, the project uses:

PydanticOutputParser

Explicit schema validation

Normalization guard for non-strict model outputs

This ensures:

✅ Valid actions only

✅ Required fields are present

✅ Parsing failures are caught early

⚠️ Safety & Robustness
Max iteration guard prevents infinite loops

Schema-enforced reasoning outputs

Explicit termination condition

Graceful fallback when tools fail

📝 Example Execution (Excerpt)
Query: What is the capital of the country where Messi was born?

Agent Behavior:

text
Iteration 1 → wikipedia → irrelevant result
Iteration 2 → search → Rosario, Argentina
Iteration 3 → wikipedia → Buenos Aires
Iteration 4 → none → terminate
Final Answer:

Lionel Messi was born in Rosario, Argentina. The capital of Argentina is Buenos Aires.

The agent adapts its strategy when tools fail and stops only when sufficient information is obtained.


🚀 Installation & Usage
Prerequisites
Python 3.9+

Installation
bash
# Clone repository
git clone <repository-url>
cd react-agent-langgraph

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
Running the Agent
bash
# Basic usage
python main.py 





-- Yaniv
