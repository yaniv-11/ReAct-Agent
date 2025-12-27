from langgraph.graph import StateGraph,END

from app.state import react_state
from app.nodes.reasoning import reasoning
from app.nodes.router import router
from app.nodes.tools import wikipedia_node, search_node

graph=StateGraph(react_state)

graph.add_node("reasoning",reasoning)
graph.add_node("wikipedia",wikipedia_node)
graph.add_node("search",search_node)

graph.set_entry_point("reasoning")

graph.add_conditional_edges(
    "reasoning",
    router,   
    {
        "wikipedia": "wikipedia",
        "search": "search",
        "end": END
    }
)

graph.add_edge("wikipedia", "reasoning")
graph.add_edge("search", "reasoning")


react_agent = graph.compile()
