'''
Entrada: Grafo (V, E), e matriz de pesos D{Dij}, para todas as arestas {i,j}
dt[1]<-0; //considerando o vertice 1 como inicial
rot[i]<-0;
para i de 2 até n faça:
    dt[i] <- infinito; //muito pesado, qualquer coisa é melhor.
    rot[i] <- 0;

A <- V; // recebe todos os vertices, pois eles estao abertos
F <- Null; // nenhum vertice foi fechado ainda.

enquanto F != V, faça:
    v <- elemento de A, tal que dt[v] é o mínimo dentre os elementos de A;
    F <- F U {v}; //adiciona nos fechados
    A <- A - {v}; // tira ele dos abertos
    N <- N - F; //conjunto de vizinhos do vertice v, menos os já fechados

    para u pertencente a N faça:
        // o q é melhor?
        se dt[v]+dvu < dt[u] entao:
            dt[u] <- dt[v]+dvu;
            rot[u] <-v;



'''

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
    # start_search_vertex = int(info[3])
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
    return adjacences_list_updated, vertex_quantity, links, directed


def dijsktra(graph):
    print(graph)


def main(argv):
    file_input_path = "../inputs/input_dijkstra.txt"
    file_output_path = "../outputs/output_dijkstra.txt" 
    # file_input_path = argv[0]
    # file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed = read_input_and_insert_graph(file_input_path)
        
        if directed:
            print(f"{vertex_quantity} {links} DIRECIONADO")
            
        else:
            print(f"{vertex_quantity} {links} NAO DIRECIONADO")
        dijsktra(adjacences_list)
        # show_list_and_weights(adjacences_list, vertex_quantity, writer)

if __name__ == "__main__":
    main(sys.argv[1:])
