from bfs import bfs_caminho_minimo
from dfs import dfs_com_ciclo
from ucs import ucs_caminho_minimo
from graphs import GRAPH_BFS, GRAPH_DFS, GRAPH_UCS


def main():
    """Executa os dois exercicios e imprime os resultados.

    Organizacao:
    - graphs.py: define os grafos usados
    - bfs.py: resolve o exercicio de BFS
    - dfs.py: resolve o exercicio de DFS
    - ucs.py: resolve o exercicio de custo uniforme
    - main.py: junta tudo e mostra a resposta final
    """

    path, bfs_order = bfs_caminho_minimo(GRAPH_BFS, "A", "F")
    dfs_order, cycle = dfs_com_ciclo(GRAPH_DFS, "A")
    ucs_path, ucs_cost, ucs_order = ucs_caminho_minimo(GRAPH_UCS, "A", "E")

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

    print()
    print("EXERCICIO 3 - UCS")
    print(f"Caminho de menor custo de A ate E: {' -> '.join(ucs_path)}")
    print(f"Custo total: {ucs_cost}")
    print(f"Ordem de expansao: {', '.join(ucs_order)}")

if __name__ == "__main__":
    main()
