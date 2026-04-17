import heapq

def ucs_caminho_minimo(grafo, inicio, destino):
    """Busca de custo uniforme (UCS) em grafo ponderado.

    Retorna o caminho de menor custo entre inicio e destino,
    o custo total desse caminho e a ordem de expansao dos vertices.

    Args:
        grafo: dicionario {vertice: [(vizinho, peso), ...]}
        inicio: vertice de partida
        destino: vertice de chegada

    Returns:
        (caminho, custo_total, ordem_expansao)
        caminho e None se destino for inalcancavel.
    """
    # Fila de prioridade: (custo_acumulado, vertice)
    fila = [(0, inicio)]
    custo_ate = {inicio: 0}
    pai = {inicio: None}
    expandidos = []

    while fila:
        custo_atual, vertice_atual = heapq.heappop(fila)

        # Ignora entradas desatualizadas na fila
        if custo_atual > custo_ate.get(vertice_atual, float("inf")):
            continue

        expandidos.append(vertice_atual)

        if vertice_atual == destino:
            break

        for vizinho, peso in grafo.get(vertice_atual, []):
            novo_custo = custo_atual + peso

            if novo_custo < custo_ate.get(vizinho, float("inf")):
                custo_ate[vizinho] = novo_custo
                pai[vizinho] = vertice_atual
                heapq.heappush(fila, (novo_custo, vizinho))

    if destino not in pai:
        return None, float("inf"), expandidos

    caminho = []
    vertice = destino
    while vertice is not None:
        caminho.append(vertice)
        vertice = pai[vertice]
    caminho.reverse()

    return caminho, custo_ate[destino], expandidos