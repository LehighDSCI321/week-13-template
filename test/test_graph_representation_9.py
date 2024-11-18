import pytest
from collections import defaultdict
from student_code import MaxFlowGraph  # Ensure this imports your actual MaxFlowGraph implementation

def test_in_degree(): #9 
    graph = MaxFlowGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", edge_weight=10)
    assert graph.in_degree("B") == 1
    assert graph.in_degree("A") == 0

