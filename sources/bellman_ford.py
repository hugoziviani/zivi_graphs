'''
Entrada: Grafo G = (V, E) e matriz de pesos D={dij} para todos os arcos (i, j)
dt[1] <- 0
rot[1] <- inf

para i <- 2 ate n, faça:
    se existe aresta (1, i), então rot[i]<-1; dt[i]<-{dij}
    senão rot[i]<-0; dt[i]<-inf
fim
para k<-1 ate n-1 faça:
    altera <- falso
    para i<-2 ate n faça:
        para j pertencente ao conjunto de antecessores de i faça:
            se dt[i] > dt[j]+dji
                dt[i] <- d[j]+dji
                rot[i]<-j
                altera <-verdadeiro
        fim
    fim
fim
se altera = false, então k<-n
fim
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
    matrix = create_matrix(vertex_quantity)
    
    adjacences_list = defaultdict(list)
    adjacences_list_updated = defaultdict(list)
    
    ######## Information graph #########
    if directed:
        while True: # varre ate o fim do arquivo
        
            line = file1.readline() 
            if not line:
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])

            matrix[source][destiny] = weight

            
            actual_itens = {source :(destiny, weight)}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            

            
            count += 1

    else:
        # print("Nao direcionado, tem aresta nos dois lados", directed)
        while True:
            line = file1.readline() 
            if not line: 
                break
            info = line.split()

            source = int(info[0])-1
            destiny = int(info[1])-1
            weight = int(info[2])
 
            matrix[source][destiny] = weight
            matrix[destiny][source] = weight

            actual_itens = {source :(destiny, weight), destiny :(source, weight)}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            
            count += 1
    
    file1.close()
    return adjacences_list_updated, matrix, vertex_quantity, links, directed

def create_matrix(rows):
    columns = rows
    mat = []
    for i in range(rows):
        row_list = []
        for j in range(columns):
            row_list.append(0)
        mat.append(row_list)

    return mat

def show_matrix_and_weights(matrix, vertex_quantity, writer):
    element_idx = 0
    for x in range(vertex_quantity):
        for line in matrix[x]:
            if line != 0:
                print(x+1, element_idx+1, int(line))
                # writer.write(f"{x+1} {element_idx+1} {int(line)}\n")
            element_idx+=1
        element_idx=0

def bellman_ford(graph, matrix, vertex_quantity):
    dt = [None] * vertex_quantity #distancia
    root = [None] * vertex_quantity #anterior
    
    dt[0] = 0
    root[0] = float('inf')

    for x in range(1, vertex_quantity):
        print()



def main(argv):
    # file_input_path = argv[0]
    # file_output_path = argv[1]
    file_input_path = "/home/hz/Documents/grafos/zivi_graphs/inputs/input_bellman_ford.txt"
    file_output_path = "/home/hz/Documents/grafos/zivi_graphs/outputs/output_bellman_ford.txt"
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, matrix, vertex_quantity, links, directed = read_input_and_insert_graph("/home/hz/Documents/grafos/zivi_graphs/inputs/input_bellman_ford.txt")
        
        bellman_ford(graph, matrix, vertex_quantity)

if __name__ == "__main__":
    main(sys.argv[1:])
