#Dicionário com cada nodo e seus visinhos
grafo = {
    'A' : ['B','D','G'],
    'B' : ['A'],
    'D' : ['H','G', 'A'],
    'G' : ['A','D','T'],
    'H' : ['P','D'],
    'T' : ['G'],
    'P' : ['H']
}

def busca(grafo, inicio, alvo): #Busca usando BrFS
    visitados = [] #Armazena os nodos vizitados
    fila = [[inicio]] #Armazena os camihos que forem testados
     
    #No caso do ponto de partida ser o pŕoprio destino
    if inicio == alvo:
        return "O ponto de partida é o mesmo de destino!"
 
    #Fica me loop até todas as possibilidades serem checadas
    while fila:
        #Pega o primeiro nodo da fila
        caminho = fila.pop(0)
        #Pega o último nodo da fila
        nodo_atual = caminho[-1]
        if nodo_atual not in visitados:
            #print(caminho)
            vizinhos = grafo[nodo_atual]
            # Vai em todos os zinhos do nodo atual e constrói um novo caminho para adicionar na fila
            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
                # retorno novo caminho se o vizinho for igual ao alvo
                if vizinho == alvo:
                    return novo_caminho
            # classifica o nodo como 'visitado'
            visitados.append(nodo_atual)
 
    # No caso de não existir caminho entre o início e o alvo
    return "Não há caminho válido entre o ponto de partida e o destino!"
 

ini = input('Digite a origem: ').upper()
alvo = input('Digite o destino: ').upper()

if (ini in grafo) and (alvo in grafo):
    try:
        print(busca(grafo, ini, alvo))
    except:
        print('Entrada de dados inválida!')
else:
    print('Os dados de entrada não estão no grafo cadastrado!')

