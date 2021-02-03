"""
 Depth-First Search - DFS

Entrada: Grafo(vertices, arestas), vertice inicial v, marca-lo como visitado.

enquanto existir w vizinho de v, faça
    se w é marcado como não visitado então
        Visite a aresta {v,w}
        DFS(G, w) //chamada recursiva da função
    fim
    senão
        se{v, w} não foi visitada ainda então
            Visite{v, w}
        fim
    fim
fim
"""

import sys
    

def dfs(graph, initial_vertex, visited):
    visited.append(initial_vertex)
    to_be_visited = [initial_vertex]
    while to_be_visited:
        actual_vertex = to_be_visited.pop()
        for neighbor in graph[actual_vertex]: #acessa a lista de vizinhos do vertice
            if neighbor not in visited:
                visited.append(neighbor)
                to_be_visited.append(neighbor)
                print(neighbor)

def depf_first_search(graph, vertex):
    visited = [] #lista vazia de arestas v, queue
    dfs(graph, vertex, visited)



def main(argv):

    graph =[(4, 6),
            (1, 2),
            (1, 3),
            (1, 4),
            (2, 3),
            (2, 4),
            (3, 4)]

    depf_first_search(graph, 1)


if __name__ == "__main__":
    main(sys.argv[1:])