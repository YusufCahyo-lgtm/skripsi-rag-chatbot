# file: workflow.py
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from nodes import mengambil, hasilin

# Kertas cetakan / Blueprint database state
class State(TypedDict):
    question: str
    context: str
    answer: str

def build_app():
    workflow = StateGraph(State)
    
    # Mendaftarkan nama panggilan node dan fungsinya
    workflow.add_node("retriever", mengambil)
    workflow.add_node("generate", hasilin)

    # Mengatur aliran jalannya program
    workflow.add_edge(START, "retriever")
    workflow.add_edge("retriever", "generate")
    workflow.add_edge("generate", END)
    
    return workflow.compile()
