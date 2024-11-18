import pytest
from collections import defaultdict
from student_code import MaxFlowGraph  # Ensure this imports your actual MaxFlowGraph implementation

def test_max_flow():
    graph = MaxFlowGraph()
    nodes = ["A", "B", "C", "D", "E", "F"]
    for nd in nodes:
        graph.add_node(nd)
    graph.add_edge("A", "B", edge_weight=16)
    graph.add_edge("A", "C", edge_weight=13)
    graph.add_edge("B", "C", edge_weight=10)
    graph.add_edge("B", "D", edge_weight=12)
    graph.add_edge("C", "B", edge_weight=4)
    graph.add_edge("C", "E", edge_weight=14)
    graph.add_edge("D", "C", edge_weight=9)
    graph.add_edge("D", "F", edge_weight=20)
    graph.add_edge("E", "D", edge_weight=7)
    graph.add_edge("E", "F", edge_weight=4)

    max_flow_value, _ = graph.max_flow("A", "F")
    assert max_flow_value == 23
