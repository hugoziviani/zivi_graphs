'''
    referencias: 
        https://www.python-course.eu/networkx.php
'''

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
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

    adjacences_list = defaultdict(list)
    adjacences_list_updated = defaultdict(list)

    if directed: # se é direcionado, nao adiciona o correspondente invertido
        ######## Information graph #########
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
            
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])
            # print("source:", source)
            # print("destiny:", destiny)
            # print("weight:", weight)
            
            if source in adjacences_list: # se ja existe o vertice, acrescenta na lista de vizinho
                # print("OK>>>>", adjacences_list)
                
                temporary = adjacences_list[source]["adjacents"]
                temporary.append((source, weight))
                # print("node existent:", type(temporary))
            else: # nao existe, cria a lista de vizinhos
                adjacences_list[source] = {
                    "adjacents" : [(destiny, weight)]
                }

            
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
            
            actual_itens = {source :{(destiny, weight)}, destiny :{(source, weight)}}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            
            count += 1
        
    file1.close()
    return adjacences_list_updated, vertex_quantity, links, directed

def plot_graph(n_vertex, pair_list):
    # G=nx.path_graph(4)
    # G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

    G=nx.path_graph(n_vertex)
    for node in pair_list:
        G.add
        #G.add_edges_from(pair_list)

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())

    nx.draw(G)
    plt.savefig("path_graph1.png")
    plt.show()

def show_list_and_weights(adjacences_list, vertex_quantity, writer):
    for key, elements in adjacences_list.items():
        for adjacents in elements:
            for item, weight in adjacents:
                print(key+1,item+1, weight)


def main(argv):
    # print(len(argv))
    file_input_path = argv[0]
    file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed = read_input_and_insert_graph(file_input_path)
        
        # print("LISTA COMPLETA:",adjacences_list)

        if directed:
            print(f"{vertex_quantity} {links} DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} DIRECIONADO\n")
        else:
            print(f"{vertex_quantity} {links} NAO DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} NAO DIRECIONADO\n")
        show_list_and_weights(adjacences_list, vertex_quantity, writer)

if __name__ == "__main__":
    main(sys.argv[1:])


# na lista voce vai adicionando os vertices adjacentes

# se nao for direcionado, vá ate a posicao de cada um e adiciona o correspondente.

# vou imprimir para todos os vertices 