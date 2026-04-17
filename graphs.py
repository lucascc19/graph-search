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
