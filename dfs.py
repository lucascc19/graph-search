def dfs_com_ciclo(grafo, inicio):
    visitados = set()
    pilha_recursao = set()
    ordem_exploracao = []
    ciclo = []

    def visitar(vertice, caminho_atual):
        nonlocal ciclo

        visitados.add(vertice)
        pilha_recursao.add(vertice)
        ordem_exploracao.append(vertice)
        caminho_atual.append(vertice)

        for vizinho in grafo.get(vertice, []):
            if ciclo:
                return

            if vizinho not in visitados:
                visitar(vizinho, caminho_atual)
            elif vizinho in pilha_recursao:
                inicio_ciclo = caminho_atual.index(vizinho)
                ciclo = caminho_atual[inicio_ciclo:] + [vizinho]
                return

        pilha_recursao.remove(vertice)
        caminho_atual.pop()

    visitar(inicio, [])
    return ordem_exploracao, ciclo
