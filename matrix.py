'''
    referencias: 
        https://www.python-course.eu/networkx.php
'''

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import sys

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
    matrix = create_matrix(vertex_quantity)
    
    ######## Information graph #########
    if directed:
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
        
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])

            matrix[source][destiny] = weight
            # matrix[destiny][source] = weight
            count += 1

    else:
        # print("Nao direcionado, tem aresta nos dois lados", directed)
        while count <= vertex_quantity+1:
            
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])
 
            matrix[source][destiny] = weight
            matrix[destiny][source] = weight
            count += 1
    
    file1.close()
    return matrix, vertex_quantity, links, directed

def plot_graph():
    G=nx.path_graph(4)
    G.add_edges_from([("a","c"),("c","d"), ("a",1), (1,"d"), ("a",2)])

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())

    nx.draw(G)
    plt.savefig("path_graph1.png")
    plt.show()

def create_matrix(rows):
    columns = rows
    shape = (columns, rows)
    matrix = np.zeros((columns, rows))
    return matrix

def show_matrix_and_weights(matrix, vertex_quantity, writer):
    element_idx = 0
    for x in range(vertex_quantity):
        for line in matrix[x]:
            if line != 0:
                print(x+1, element_idx+1, int(line))
                writer.write(f"{x+1} {element_idx+1} {int(line)}\n")
            element_idx+=1
        element_idx=0
    # aqui posso paralelizar algo...

def main(argv):
    print(len(argv))
    file_input_path = argv[0]
    file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        matrix, vertex_quantity, links, directed = read_input_and_insert_graph(file_input_path)
        # print(vertex_quantity, links)
        if directed:
            print(f"{vertex_quantity} {links} DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} DIRECIONADO\n")
        else:
            print(f"{vertex_quantity} {links} NAO DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} NAO DIRECIONADO\n")
        show_matrix_and_weights(matrix, vertex_quantity, writer)
    # print(matrix)

if __name__ == "__main__":
    main(sys.argv[1:])
