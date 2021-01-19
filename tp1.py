'''
    referencias: 
        https://www.python-course.eu/networkx.php
'''



import networkx as nx
import matplotlib.pyplot as plt

FILE_PATH = './input.txt'
MODE_READ = 'r'
MODE_WRITE = 'w'


vertex_quantity = 0
links = 0
directed = 0

def read_input():
    file1 = open(FILE_PATH, MODE_READ)
    count = 0
    
    while True: 
        
        line = file1.readline() 
        if not line: 
            break
        print("Line{}: {}".format(count, line.strip())) 
        count += 1
    
    file1.close() 

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


read_input()


# networkx
