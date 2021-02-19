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