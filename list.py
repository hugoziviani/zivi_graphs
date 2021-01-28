'''
    referencias: 
        https://www.python-course.eu/networkx.php
'''



import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


FILE_PATH = './input.txt'
MODE_READ = 'r'
MODE_WRITE = 'w'


def read_input_and_insert_graph():
    file1 = open(FILE_PATH, MODE_READ)
    count = 0
    line = file1.readline()
    info = line.split()

    ######## Information graph #########
    vertex_quantity = int(info[0])
    links = int(info[1])
    directed = bool(info[2])
    matrix = create_matrix(vertex_quantity)
    pair_list = []
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
        pair_list.append((source, destiny, weight))
        matrix[source][destiny] = weight
        count += 1
    
    file1.close()
    return matrix, vertex_quantity, links, directed, pair_list

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

def create_matrix(rows):
    columns = rows
    matrix = np.zeros((columns, rows))
    return matrix

def main(argv):
    print(len(argv)
    matrix, vertex_quantity, links, directed, pair_list = read_input_and_insert_graph()
    print(pair_list)
    plot_graph(vertex_quantity, pair_list)
    # print(matrix)


if __name__ == "__main__":
    main()


# na lista voce vai adicionando os vertices adjacentes

# se nao for direcionado, vá ate a posicao de cada um e adiciona o correspondente.


# vou imprimir para todos os vertices 