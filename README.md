ReAct Agent with LangGraph
A Stateful, Tool-Driven Reasoning Agent

This project implements a true ReAct (Reason → Act → Observe → Reason) agent using LangGraph, designed to perform multi-step reasoning, dynamic tool selection, and robust failure recovery.

Unlike single-prompt LLM demos, this agent explicitly models state, control flow, and tool execution, making it closer to how real-world agentic AI systems are built.



 Why This Project Exists

Most LLM-based agents:

Hide reasoning inside a single prompt

Fail silently when tools return irrelevant results

Loop indefinitely without safeguards

Are hard to debug or extend

This project solves those issues by:

Making reasoning explicit and traceable

Separating decision-making from execution

Using a graph-based control flow

Enforcing iteration limits and schema validation

 Core Concepts Implemented

ReAct reasoning loop (Reason → Act → Observe)

Graph-based orchestration with LangGraph

Dynamic routing between tools and termination

Explicit agent state shared across iterations

Tool failure detection and recovery

Structured output parsing (HF-compatible)

Pretty iteration logs for full transparency

 Architecture Overview
┌──────────────┐
│  Reasoning   │  ← LLM decides next action
└──────┬───────┘
       │
       ▼
┌──────────────┐
│   Router     │  ← Routes based on action
└──────┬───────┘
       │
 ┌─────▼──────────┐
 │  Tool Nodes    │  ← Wikipedia / Search
 └─────┬──────────┘
       │
       └────────────► Back to Reasoning

Design Principles

Reasoning ≠ Execution

Tools produce observations

State flows through every node

Termination is an explicit action (none)

 Agent State

The agent maintains a shared state across iterations:

{
  input: str,
  thoughts: List[str],
  reasons: List[str],
  actions: List[str],
  action_inputs: List[str],
  observations: List[str],
  final_answer: Optional[str],
  iteration: int
}


This enables:

Step-by-step traceability

Debugging and inspection

Deterministic behavior

 ReAct Execution Flow

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

 Tools

Wikipedia – encyclopedic factual queries

Search – fallback for ambiguous or failed results

Tools are implemented as independent nodes, keeping execution isolated from reasoning logic.

 Structured Output & Validation

Since HuggingFace models do not support native function calling, the project uses:

PydanticOutputParser

Explicit schema validation

Normalization guard for non-strict model outputs

This ensures:

Valid actions only

Required fields are present

Parsing failures are caught early

 Safety & Robustness

Max iteration guard prevents infinite loops

Schema-enforced reasoning outputs

Explicit termination condition

Graceful fallback when tools fail

 Example Execution (Excerpt)

Query

What is the capital of the country where Messi was born?


Agent Behavior

Iteration 1 → wikipedia → irrelevant result
Iteration 2 → search → Rosario, Argentina
Iteration 3 → wikipedia → Buenos Aires
Iteration 4 → none → terminate


Final Answer

Lionel Messi was born in Rosario, Argentina.
The capital of Argentina is Buenos Aires.


The agent adapts its strategy when tools fail and stops only when sufficient information is obtained.

📁 Project Structure
app/
├── graph.py            # LangGraph definition
├── state.py            # Agent state schema
├── llm.py              # LLM + output parser
├── schema.py           # Pydantic reasoning schema
├── prompts.py          # ReAct prompt
├── nodes/
│   ├── reasoning.py    # LLM reasoning node
│   ├── tools.py        # Wikipedia & Search nodes
│   └── router.py       # Conditional routing
main.py            # Run the agent

▶️ Running the Agent
pip install -r requirements.txt
python main.py


--yaniv
