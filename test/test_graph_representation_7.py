import pytest
from collections import defaultdict
from student_code import MaxFlowGraph  # Ensure this imports your actual MaxFlowGraph implementation


def test_add_node(): #7
    graph = MaxFlowGraph()
    graph.add_node("A")
    assert "A" in graph.get_nodes()
