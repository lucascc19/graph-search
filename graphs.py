"""Grafos usados nos exercicios.

GRAPH_BFS:
    Grafo nao direcionado do exercicio de busca em largura.

GRAPH_DFS:
    Grafo direcionado do exercicio de busca em profundidade.
"""

GRAPH_BFS = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "E"],
    "D": ["B", "C", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"],
}


GRAPH_DFS = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D", "E"],
    "D": ["B"],
    "E": [],
}

GRAPH_UCS = {
    "A": [("B", 2), ("C", 5)],
    "B": [("A", 2), ("D", 4), ("E", 7)],
    "C": [("A", 5), ("D", 1)],
    "D": [("B", 4), ("C", 1), ("E", 1)],
    "E": [("B", 7), ("D", 1)],
}