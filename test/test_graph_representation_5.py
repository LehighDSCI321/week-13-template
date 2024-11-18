import pytest
from collections import defaultdict
from student_code import MaxFlowGraph  # Ensure this imports your actual MaxFlowGraph implementation


def test_residual_graph_after_flow():
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

    _, f = graph.max_flow('A', 'F')
    rg = graph.res_graph(f)
    assert rg.get_edge_weight('A', 'B') == 4
