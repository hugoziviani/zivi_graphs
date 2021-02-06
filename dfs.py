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



def dfs(graph, initial_vertex, visited):
    #passar a lista de adjacencias(grafo)
    # print("graph:", graph)
    initial_vertex = initial_vertex-1
    visited.add(initial_vertex)
    to_be_visited = [initial_vertex]
    while to_be_visited:
        # print("tipo:",type(to_be_visited))
        actual_vertex = to_be_visited.pop()
        
        for neighbor in graph[actual_vertex]: #acessa a lista de vizinhos do vertice
            # print("actual:", actual_vertex)
            # print("Vizinho:", neighbor)
            # print("Vizinhos:", graph[actual_vertex])
            # # return
            if neighbor[0] not in visited:
                visited.add(neighbor[0])
                to_be_visited.append(neighbor[0])
                
                # print("visitou:",neighbor[0])
                

def depf_first_search(graph, vertex):
    visited = set() #lista vazia de arestas v, queue
    dfs(graph, vertex, visited)

    return visited

def main(argv):
    # file_input_path = argv[0]
    # file_output_path = argv[1]
    file_input_path = "input_search.txt"
    file_output_path = "out.txt"
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed, start_search_vertex = read_input_and_insert_graph(file_input_path)
        
        print("We gonna start from the vertex:", start_search_vertex)        
        if directed:
            print(f"{vertex_quantity} {links} DIRECIONADO")
            # writer.write(f"{vertex_quantity} {links} DIRECIONADO\n")
        else:
            print(f"{vertex_quantity} {links} NAO DIRECIONADO")
            # writer.write(f"{vertex_quantity} {links} NAO DIRECIONADO\n")
        # show_list_and_weights(adjacences_list, vertex_quantity, writer)

    visited = depf_first_search(adjacences_list, start_search_vertex)
    for element in visited:
        print(element+1)

if __name__ == "__main__":
    main(sys.argv[1:])