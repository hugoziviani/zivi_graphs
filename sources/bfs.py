"""
Breadth First Search - BFS

Entrada: Grafo(vertices, arestas)
Cria uma fila vazia Q
Vertice inicial v, marca-lo como visitado.

enquanto Q != vazia faça
    v  = Q.pop (tiro um elemento para analise)
    para todo vertice w vizinho de v faça
        se w nao foi vizitado entao
            visite a aresta {v,w}
            insira w em Q
            Marque w como visitado
        fim
        senao
            se {v, w} nao foi vizitada ainda entao
                visite {v, w}
            fim
        fim
    fim
fim
"""

import sys
from itertools import chain
from collections import defaultdict

MODE_READ = 'r'
MODE_WRITE = 'w'

def read_input_and_insert_graph(file_input_path):
    file1 = open(file_input_path, MODE_READ)
    count = 0
    line = file1.readline()
    info = line.split()

    ######## Information graph #########
    vertex_quantity = int(info[0])
    links = int(info[1])
    if info[2] == "0":
        directed = False
    else:
        directed = True
    start_search_vertex = int(info[3])
    ######## Information graph #########

    adjacences_list = defaultdict(list)
    adjacences_list_updated = defaultdict(list)

    if directed: # se é direcionado, nao adiciona o correspondente invertido
        
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
            
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])

            actual_itens = {source :(destiny, weight)}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            
            count += 1

    else: # adiciona o correspondente
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
            
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])
            
            actual_itens = {source: (destiny, weight), destiny: (source, weight)}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            
            count += 1
        
    file1.close()
    return adjacences_list_updated, vertex_quantity, links, directed, start_search_vertex

def bfs(graph, initial_vertex):
    initial_vertex = initial_vertex-1
    queue = []
    visited = []
    queue.append(initial_vertex)
    visited.append(initial_vertex)
    
    while queue:
        vertex = queue.pop(0)
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor[0] not in visited:
                queue.append(neighbor[0])
                visited.append(neighbor[0])

    return visited

def main(argv):
    file_input_path = argv[0]
    file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed, start_search_vertex = read_input_and_insert_graph(file_input_path)
        visited_list = bfs(adjacences_list, start_search_vertex)
        
        size_list = len(visited_list)
        for x in range(size_list): 
            writer.write(str(visited_list[x]+1))
            if x < size_list-1:
                writer.write(" ")
        
if __name__ == "__main__":
    main(sys.argv[1:])