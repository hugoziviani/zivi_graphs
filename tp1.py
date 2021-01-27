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
    # print("vertex_quantity:", vertex_quantity) 
    # print("links:", type(links))
    # print("directed:", type(directed))

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
        matrix[source][destiny] = weight
        count += 1
    
    file1.close()
    return matrix

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
    matrix = np.zeros((columns, rows))
    return matrix


def main():
    # m = create_matrix(2)
    # m[1][1]=1
    m = read_input_and_insert_graph()
    print(m)


if __name__ == "__main__":
    main()
