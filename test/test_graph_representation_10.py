import pytest
from collections import defaultdict
from student_code import MaxFlowGraph  # Ensure this imports your actual MaxFlowGraph implementation


def test_out_degree(): #10
    graph = MaxFlowGraph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B", edge_weight=10)
    assert graph.out_degree("A") == 1
    assert graph.out_degree("B") == 0
