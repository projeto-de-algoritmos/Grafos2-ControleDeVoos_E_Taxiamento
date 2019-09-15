from pqdict import PQDict
from collections import defaultdict 

def get_posicoes():
    pos = {
        '31L-ECHO' : (60,0),
        '31L-KILO-GOLF' : (50,20),
        '31L-DELTA' : (40,40),
        '31L-ECHO2' : (30,60),
        '31L-ALPHA' : (20,80),
        '31L-BRAVO-HOTEL' : (10,100),
        '35-BRAVO' : (13,0),
        '35-FOXTROT' : (14,20),
        '35-DELTA' : (15,40),
        '35-ALPHA' : (17,80),
        '35-HOTEL' : (18,100),
        '35-BRAVO2' : (19,120),
        'BRAVO-FOXTROT' : (8,22),
        'BRAVO-DELTA' : (9,42),
        'BRAVO-ALPHA' : (11,82),
        'ECHO-KILO' : (40,20),
        'ECHO-DELTA' : (30,40),
        'ECHO-ALPHA-JULIET' : (29,80),
        'GOLF-DELTA' : (50,39),
        'GOLF-ALPHA' : (51,79),
        'GOLF-HOTEL' : (52,98),
        'HOTEL-JULIET' : (40,99),
        'TERMINAL PASSAGEIROS' : (10,62),
        'TERMINAL FRETE' : (53,110),
        'T-HANGAR' : (46,110)
        }
    return pos

def exibir_menu_principal():
    print('Bem vindo ao Aeroporto Internacional de Brownsville South Padre Island (BRO)')
    print('1 - Mostrar Diagrama do Aeroporto')
    print('2 - Perguntar ao Dijkstra (Controlador de solo) o menor caminho com menor custo entre lugares do aeroporto')
    print('0 - Sair')
    opcao = int(input('\n\nQual opção você deseja realizar? '))
    opcao = valida_opcao(opcao)

    return opcao

def valida_opcao(opcao):
    while (opcao < 0 or opcao > 2):
        print('Opção inválida! Por favor, digite novamente')
        opcao = int(input('\n\nQual opção você deseja realizar? '))
    return opcao

def captura_dados_menor_caminho():
    origem = str(input('Digite o ponto do aeroporto que o avião se encontra: '))
    destino = str(input('Digite o ponto do aeroporto que o avião deseja se deslocar: '))

    return origem, destino

def dijkstra(G, origem, destino, visitados = [], distancias = {}, predecessores = {}):
    # Verifica se os valores passados para origem e destino existem no Grafo
    if origem not in G:
        raise TypeError('Local de origem indicado não existe na carta do aerporto')
    if destino not in G:
        raise TypeError('Local de destino indicado não existe na carta do aerporto')    
    
    # Condição de parada da recursão, quando chega no nó destino
    if origem == destino:
        
        caminho = []
        pred = destino

        # Aqui realiza o backtracking para mostrar o caminho a partir da origem
        while pred != None:
            caminho.append(pred) # Append coloca no começo
            pred = predecessores.get(pred, None)
        
        # Inicializando a variável de caminho legível
        caminhoLegivel = caminho[0] # Coloca a origem no caminho legível que é uma maneira mais agradável visualmente de mostrar o caminho
        
        # Completa o caminho de forma legível
        for i in range(1, len(caminho)): 
            caminhoLegivel = caminho[i] + ' ---> ' + caminhoLegivel

        return caminho, caminhoLegivel, distancias[destino]
 
    else :     
        # Se a lista de visitados estiver vazia, significa que ele está no nó de origem e a distância é zero
        if not visitados: 
            distancias[origem] = 0

        # Percorre os vizinhos do nó de origem
        for vizinho in G[origem] :
            # Confere se o vizinho não foi visitado
            if vizinho not in visitados:
                # print(distancias[origem])
                # print(G[origem][vizinho])
                nova_distancia = distancias[origem] + G[origem][vizinho]['weight'] # Guarda a soma da distância armazenada no nó de origem mais a do novo nó
                # float('inf') -> funciona como se fosse um valor infinito
                if nova_distancia < distancias.get(vizinho, float('inf')):  # Atualiza as distâncias e os predecessores caso a nova distância
                                                                            # seja menor que as armazenadas... Expande a mancha
                    distancias[vizinho] = nova_distancia
                    predecessores[vizinho] = origem
                    
        visitados.append(origem) # Coloca o nó atual nos visitados

        naoVisitados = {} # Cria um dict para guardar os nós não visitados para chamar na recursão

        for no in G: # Percorre todos os nós do grafo
            if no not in visitados: # Se o nó não tiver nos visitados
                naoVisitados[no] = distancias.get(no, float('inf')) # 'no' é a key e o distancias.get é o value do dict        
        
        # Pega o nó não visitado que possui a menor distância
        novoNo = min(naoVisitados, key = naoVisitados.get)

        # chama recursivo pro novo nó
        return dijkstra(G, novoNo, destino, visitados, distancias, predecessores)
