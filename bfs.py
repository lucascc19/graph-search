from collections import deque


def bfs_caminho_minimo(grafo, inicio, destino):
    fila = deque([inicio])
    visitados = {inicio}
    pai = {inicio: None}
    ordem_visita = []

    while fila:
        vertice_atual = fila.popleft()
        ordem_visita.append(vertice_atual)

        if vertice_atual == destino:
            break

        for vizinho in grafo[vertice_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                pai[vizinho] = vertice_atual
                fila.append(vizinho)

    if destino not in pai:
        return None, ordem_visita

    caminho = []
    vertice = destino
    while vertice is not None:
        caminho.append(vertice)
        vertice = pai[vertice]
    caminho.reverse()

    return caminho, ordem_visita
