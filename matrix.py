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
    print(">>", info[2])
    if info[2] == 0:
        directed = False
    else:
        directed = True
    matrix = create_matrix(vertex_quantity)
    print("is directed", directed)
    ######## Information graph #########
    if directed:
        print("is directed", directed)
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
        
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

    else:
        while count <= vertex_quantity+1: # varre ate o fim do arquivo
            
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

def show_matrix_and_weights(vertex_quantity, matrix):
    element_idx = 0
    print(vertex_quantity)
    for x in range(vertex_quantity):
        for line in matrix[x]:
            if line != 0:
                print(x+1, element_idx+1, int(line))
            element_idx+=1
        element_idx=0

def main():
    
    matrix, vertex_quantity, links, directed = read_input_and_insert_graph()
    show_matrix_and_weights(vertex_quantity, matrix)
    # print(matrix)

if __name__ == "__main__":
    main()
