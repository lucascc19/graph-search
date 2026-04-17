# Exercicios de Grafos com BFS, DFS e UCS

Este projeto resolve tres exercicios classicos de teoria dos grafos usando Python:
- busca em largura (BFS)
- busca em profundidade (DFS)
- busca de custo uniforme (UCS)

A organizacao dos arquivos ficou assim:
- `graphs.py`: define os grafos usados nos exercicios
- `bfs.py`: implementa a busca em largura
- `dfs.py`: implementa a busca em profundidade com deteccao de ciclo
- `ucs.py`: implementa a busca de custo uniforme
- `main.py`: executa os tres exercicios e imprime os resultados

## Questao 1 - Busca em largura (BFS)

### Enunciado

Considere o grafo nao ponderado abaixo, com arestas nao direcionadas:

`A-B, A-C, B-D, C-D, C-E, D-F, E-F`

### Representacao visual do Grafo 1

![Grafo 1](./assets/graph_bfs.png)

### Como a BFS funciona neste exercicio

A BFS visita os vertices por niveis. Isso significa que ela explora primeiro todos os vertices a 1 aresta de distancia do ponto inicial, depois os vertices a 2 arestas, e assim por diante.

Comecando em `A`:

1. Visitamos `A`
2. Descobrimos seus vizinhos: `B` e `C`
3. Depois exploramos `B`, descobrindo `D`
4. Depois exploramos `C`, descobrindo `E`
5. Depois exploramos `D`, descobrindo `F`

Como a BFS encontra o destino `F` pelo menor numero de arestas, o caminho minimo encontrado foi:

`A -> B -> D -> F`

### Resposta da questao 1

#### (a) Caminho com menor numero de arestas de A ate F

`A -> B -> D -> F`

#### (b) Ordem de visita dos vertices

`A, B, C, D, E, F`

## Questao 2 - Busca em profundidade (DFS)

### Enunciado

Considere o grafo direcionado com arestas:

`A -> B, B -> C, C -> D, D -> B, C -> E`

### Representacao visual do Grafo 2

![Grafo 2](./assets/graph_dfs.png)

### Como a DFS funciona neste exercicio

A DFS tenta seguir o mais fundo possivel em cada caminho antes de voltar.

Comecando em `A`:

1. Visitamos `A`
2. Seguimos para `B`
3. De `B`, seguimos para `C`
4. De `C`, seguimos para `D`
5. Em `D`, existe uma aresta voltando para `B`

Como `B` ainda faz parte do caminho ativo da recursao, isso indica a existencia de um ciclo.

O ciclo encontrado e:

`B -> C -> D -> B`

### Resposta da questao 2

#### (a) Ordem de exploracao a partir de A

`A, B, C, D`

#### (b) Ha ciclo no grafo?

Sim. O ciclo e:

`B -> C -> D -> B`

## Questao 3 - Busca de custo uniforme (UCS)

### Enunciado

Considere o grafo ponderado com arestas nao direcionadas:

`A-B (2), A-C (5), B-D (4), C-D (1), B-E (7), D-E (1)`

### Como a UCS funciona neste exercicio

A UCS expande sempre o vertice com menor custo acumulado a partir da origem, usando uma fila de prioridade. Diferente da BFS, ela leva em conta os pesos das arestas — por isso garante o caminho de menor custo total, nao o de menor numero de arestas.

Comecando em `A`:

1. Expandimos `A` (custo 0). Inserimos na fila: `B(2)`, `C(5)`
2. Expandimos `B` (custo 2, o menor). Inserimos: `D(6)`, `E(9)`
3. Expandimos `C` (custo 5). Geraria `D` com custo 6, igual ao ja existente — sem alteracao
4. Expandimos `D` (custo 6). Descobrimos `E` com custo 7, menor que o `E(9)` atual — **atualizamos**
5. Expandimos `E` (custo 7) — destino alcancado

O caminho de menor custo encontrado foi:

`A -> B -> D -> E` com custo total `7`

### Resposta da questao 3

#### Caminho de menor custo de A ate E

`A -> B -> D -> E`

#### Custo total

`7`

#### Ordem de expansao dos vertices

`A, B, C, D, E`

## Relacao com o codigo

Os grafos usados no codigo estao definidos em `graphs.py`.

- `GRAPH_BFS` representa o Grafo 1
- `GRAPH_DFS` representa o Grafo 2
- `GRAPH_UCS` representa o Grafo 3, com estrutura `{vertice: [(vizinho, peso), ...]}` para suportar os pesos das arestas

A implementacao da BFS esta em `bfs.py`, a implementacao da DFS com deteccao de ciclo esta em `dfs.py`, e a implementacao da UCS com fila de prioridade esta em `ucs.py`.

## Como executar

Para executar tudo de uma vez:

```bash
python main.py
```

Se o comando `python` nao estiver configurado no ambiente, pode ser necessario instalar o Python ou ajustar o PATH.