'''
Entrada: Grafo (V, E), e matriz de pesos D{Dij}, para todas as arestas {i,j}
dt[0]<-0; //considerando o vertice 1 como inicial
rot[0]<-0; // não tem antecessor
para i de 2 até n faça: //para todos os vertices validos vamos inicializar
    dt[i] <- infinito; //muito pesado, distancia nao calculada ainda
    rot[i] <- 0; // antecessor, pai do vertice do tempo de exec.

A <- V; // recebe todos os vertices, pois eles estao abertos
F <- Null; // nenhum vertice foi fechado ainda.

enquanto F != V, faça: //enquanto o grupo de fechados for diferente dos vertices do grafo (tem que explorar todos)
    v <- elemento de A, tal que dt[v] é o mínimo dentre os elementos de A; na 1a exec. será o 0, pois ele é o que tem menor dt[0]

    F <- F U {v}; //adiciona nos fechados
    A <- A - {v}; // tira ele dos abertos
    N <- N - F; //conjunto de vizinhos do vertice v, menos os já fechados

    para u pertencente a N faça:
        // o q é melhor? o peso atual + o peso até o proximo ou a menor distancia já calculada 
        se dt[v]+dvu < dt[u] entao:
            dt[u] <- dt[v]+dvu; //se for, atualiza a soma de pesos para a menor distancia calculada
            rot[u] <-v; // guarda o antecessor

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


def dijkstra(graph): #retorna a menor distancia de um dado nó para todos os outros possíveis.

    weight_control = {}
    current_distance = {}
    actual_weight = {}
    to_be_visited = list(graph.keys())
    actual_vertex = 0
    actual_weight[actual_vertex] = 0

    for vertice in graph.keys():
        current_distance[vertice] = float('inf') #inicia os vertices como infinito

    current_distance[actual_vertex] = 0 #distancia até ele mesmo
    to_be_visited.remove(actual_vertex) #remove ele dos nao visitados
    way_to = []
    way_to.append(actual_vertex)
    while to_be_visited: #enquanto existir no a ser visitado
        
        neighborood = graph[actual_vertex]

        print(actual_vertex, " ",neighborood)
        for neighbor, weight in neighborood: # para cada visinho do nó atual, calcular a distancia para o proximo e atualizar se necessario
            
            current_weight = weight + actual_weight[actual_vertex]
            distance = current_distance.get(neighbor, float("inf"))
            if current_weight < distance:
            # if distance > current_weight: # se a distancia até o vizinho for maior que o que acabou de ser calculado, atualiza
                current_distance[neighbor] = current_weight
                weight_control[neighbor] = current_distance[neighbor]

        # if not weight_control: 
        #     break
        
        # next_vertex = min(weight_control.items())
        next_vertex = min(weight_control.items(), key=lambda x: x[1])
        actual_vertex = next_vertex[0] #proximo vertice do caminho
        actual_weight[actual_vertex] = next_vertex[1]
        to_be_visited.remove(actual_vertex)
        weight_control.pop(actual_vertex, None)
        way_to.append(actual_vertex)
        # print(way_to)
    
    # print(current_distance)
    return current_distance

    
def main(argv):
    file_input_path = "/home/hz/Documents/grafos/zivi_graphs/inputs/input_dijkstra.txt"
    file_output_path = "/home/hz/Documents/grafos/zivi_graphs/outputs/output_dijkstra.txt" 
    # file_input_path = argv[0]
    # file_output_path = argv[1]
    with open(file_output_path, MODE_WRITE) as writer:
        adjacences_list, vertex_quantity, links, directed = read_input_and_insert_graph(file_input_path)
        
        # if directed:
        #     print(f"{vertex_quantity} {links} DIRECIONADO")
            
        # else:
        #     print(f"{vertex_quantity} {links} NAO DIRECIONADO")
        distances = dijkstra(adjacences_list)
        for distance in distances.items():
            print(f"{distance[0]+1} ({distance[1]}) :")
        # show_list_and_weights(adjacences_list, vertex_quantity, writer)

if __name__ == "__main__":
    main(sys.argv[1:])
