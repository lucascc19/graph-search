from bfs import bfs_shortest_path
from dfs import dfs_with_cycle
from graphs import GRAPH_BFS, GRAPH_DFS


def main():
    """Executa os dois exercicios e imprime os resultados.

    Organizacao:
    - graphs.py: define os grafos usados
    - bfs.py: resolve o exercicio de BFS
    - dfs.py: resolve o exercicio de DFS
    - main.py: junta tudo e mostra a resposta final
    """

    path, bfs_order = bfs_shortest_path(GRAPH_BFS, "A", "F")
    dfs_order, cycle = dfs_with_cycle(GRAPH_DFS, "A")

    print("EXERCICIO 1 - BFS")
    print(f"Caminho com menor numero de arestas de A ate F: {' -> '.join(path)}")
    print(f"Ordem de visita: {', '.join(bfs_order)}")
    print()

    print("EXERCICIO 2 - DFS")
    print(f"Ordem de exploracao a partir de A: {', '.join(dfs_order)}")
    if cycle:
        print(f"Ha ciclo no grafo: {' -> '.join(cycle)}")
    else:
        print("Nao ha ciclo no grafo.")


if __name__ == "__main__":
    main()
