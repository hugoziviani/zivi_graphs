'''
    referencias: 
        https://www.python-course.eu/networkx.php
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

            actual_itens = {source :{(destiny, weight)}}

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
            
            actual_itens = {source :{(destiny, weight)}, destiny :{(source, weight)}}

            for k, v in chain(adjacences_list.items(), actual_itens.items()):
                adjacences_list_updated[k].append(v)
            
            count += 1
        
    file1.close()
    return adjacences_list_updated, vertex_quantity, links, directed

def show_list_and_weights(adjacences_list, vertex_quantity, writer):
    for key, elements in adjacences_list.items():
        for adjacents in elements:
            for item, weight in adjacents:
                print(key+1, item+1, weight)
                writer.write(f"{key+1} {item+1} {weight}\n")


def main(argv):
    file_input_path = argv[0]
    file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed = read_input_and_insert_graph(file_input_path)
        
        if directed:
            print(f"{vertex_quantity} {links} DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} DIRECIONADO\n")
        else:
            print(f"{vertex_quantity} {links} NAO DIRECIONADO")
            writer.write(f"{vertex_quantity} {links} NAO DIRECIONADO\n")
        show_list_and_weights(adjacences_list, vertex_quantity, writer)

if __name__ == "__main__":
    main(sys.argv[1:])