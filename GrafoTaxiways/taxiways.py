import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#24 nós
G.add_node('31L-ECHO', label = '31L-ECHO', color = 'black')
G.add_node('31L-KILO-GOLF', label = '31L-KILO-GOLF', color = 'black' )
G.add_node('31L-DELTA', label = '31L-DELTA', color = 'black')
G.add_node('31L-ECHO2', label = '31L-ECHO2', color = 'black')
G.add_node('31L-ALPHA', label = '31L-ALPHA', color = 'black')
G.add_node('31L-BRAVO-HOTEL', label = '31L-BRAVO-HOTEL', color = 'black')
G.add_node('35-BRAVO', label = '35-BRAVO', color = 'black')
G.add_node('35-FOXTROT', label = '35-FOXTROT', color = 'black')
G.add_node('35-DELTA', label = '35-DELTA', color = 'black')
G.add_node('35-ALPHA', label = '35-ALPHA', color = 'black')
G.add_node('35-HOTEL', label = '35-HOTEL', color = 'black')
G.add_node('35-BRAVO2', label = '35-BRAVO2', color = 'black')
G.add_node('BRAVO-FOXTROT', label = 'BRAVO-FOXTROT', color = 'gray')
G.add_node('BRAVO-DELTA', label = 'BRAVO-DELTA', color = 'gray')
G.add_node('BRAVO-ALPHA', label = 'BRAVO-ALPHA', color = 'gray')
G.add_node('ECHO-KILO', label = 'ECHO-KILO', color = 'gray')
G.add_node('ECHO-DELTA', label = 'ECHO-DELTA', color = 'gray')
G.add_node('ECHO-ALPHA-JULIET', label = 'ECHO-ALPHA-JULIET', color = 'gray')
G.add_node('GOLF-DELTA', label = 'GOLF-DELTA', color = 'gray')
G.add_node('GOLF-ALPHA', label = 'GOLF-ALPHA', color = 'gray')
G.add_node('GOLF-HOTEL', label = 'GOLF-HOTEL', color = 'gray')
G.add_node('HOTEL-JULIET', label = 'HOTEL-JULIET', color = 'gray')
G.add_node('TERMINAL PASSAGEIROS', label = 'TERMINAL PASSAGEIROS', color = 'black')
G.add_node('TERMINAL FRETE', label = 'TERMINAL FRETE', color = 'black')
G.add_node('T-HANGAR', label = 'T-HANGAR', color = 'black')


G.add_edge('31L-ECHO','31L-KILO-GOLF', weight = 2000 , label = '31L', color = 'black', width = 19)
G.add_edge('31L-KILO-GOLF','31L-DELTA', weight = 1000 , label = '31L', color = 'black', width = 19)
G.add_edge('31L-DELTA','31L-ECHO2', weight = 400 , label = '31L', color = 'black', width = 19)
G.add_edge('31L-ECHO2','31L-ALPHA', weight =  3000, label = '31L', color = 'black', width = 19)
G.add_edge('31L-ALPHA','31L-BRAVO-HOTEL', weight = 1000 , label = '31L', color = 'black', width = 19)
G.add_edge('35-BRAVO','35-FOXTROT', weight = 1000 , label = '35', color = 'black', width = 19)
G.add_edge('35-FOXTROT','35-DELTA', weight = 1000 , label = '35', color = 'black', width = 19)
G.add_edge('35-DELTA','35-ALPHA', weight = 3000 , label = '35', color = 'black', width = 19)
G.add_edge('35-ALPHA','35-HOTEL', weight = 500 , label = '35', color = 'black', width = 19)
G.add_edge('35-HOTEL','35-BRAVO2', weight = 500 , label = '35', color = 'black', width = 19)
G.add_edge('35-BRAVO','BRAVO-FOXTROT', weight = 1000 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('BRAVO-FOXTROT','BRAVO-DELTA', weight = 1000 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('BRAVO-DELTA','TERMINAL PASSAGEIROS', weight = 500 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('TERMINAL PASSAGEIROS','BRAVO-ALPHA', weight = 600 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('BRAVO-ALPHA','31L-BRAVO-HOTEL', weight = 500 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('31L-BRAVO-HOTEL','35-BRAVO2', weight = 500 , label = 'BRAVO', color = 'gray', width = 7)
G.add_edge('BRAVO-FOXTROT','35-FOXTROT', weight = 100 , label = 'FOXTROT', color = 'gray', width = 7)
G.add_edge('BRAVO-DELTA','35-DELTA', weight = 100 , label = 'DELTA', color = 'gray', width = 7)
G.add_edge('BRAVO-ALPHA','35-ALPHA', weight = 100 , label = 'ALPHA', color = 'gray', width = 7)
G.add_edge('31L-BRAVO-HOTEL','35-HOTEL', weight = 150 , label = 'HOTEL', color = 'gray', width = 7)
G.add_edge('31L-ECHO','ECHO-KILO', weight = 2050 , label = 'ECHO', color = 'gray', width = 7)
G.add_edge('ECHO-KILO','ECHO-DELTA', weight = 1050 , label = 'ECHO', color = 'gray', width = 7)
G.add_edge('ECHO-KILO','31L-KILO-GOLF', weight = 300 , label = 'KILO', color = 'gray', width = 7)
G.add_edge('ECHO-DELTA','31L-ECHO2', weight = 300 , label = 'ECHO', color = 'gray', width = 7)
G.add_edge('31L-ECHO2','ECHO-ALPHA-JULIET', weight = 450 , label = 'ECHO', color = 'gray', width = 7)
G.add_edge('ECHO-DELTA','35-DELTA', weight = 1000 , label = 'DELTA', color = 'gray', width = 7)
G.add_edge('ECHO-DELTA','31L-DELTA', weight = 300 , label = 'DELTA', color = 'gray', width = 7)
G.add_edge('35-ALPHA','31L-ALPHA', weight = 50 , label = 'ALPHA', color = 'gray', width = 7)
G.add_edge('31L-KILO-GOLF','GOLF-DELTA', weight = 500 , label = 'GOLF', color = 'gray', width = 7)
G.add_edge('GOLF-DELTA','GOLF-ALPHA', weight = 3000 , label = 'GOLF', color = 'gray', width = 7)
G.add_edge('GOLF-ALPHA','GOLF-HOTEL', weight = 500 , label = 'GOLF', color = 'gray', width = 7)
G.add_edge('GOLF-HOTEL','TERMINAL FRETE', weight = 300 , label = 'GOLF', color = 'gray', width = 7)
G.add_edge('GOLF-DELTA','31L-DELTA', weight = 250 , label = 'DELTA', color = 'gray', width = 7)
G.add_edge('GOLF-ALPHA','ECHO-ALPHA-JULIET', weight = 700 , label = 'ALPHA', color = 'gray', width = 7)
G.add_edge('ECHO-ALPHA-JULIET','31L-ALPHA', weight = 500 , label = 'ALPHA', color = 'gray', width = 7)
G.add_edge('ECHO-ALPHA-JULIET','HOTEL-JULIET', weight = 600 , label = 'JULIET', color = 'gray', width = 7)
G.add_edge('GOLF-HOTEL','HOTEL-JULIET', weight = 350 , label = 'HOTEL', color = 'gray', width = 7)
G.add_edge('HOTEL-JULIET','35-HOTEL', weight = 850 , label = 'HOTEL', color = 'gray', width = 7)
G.add_edge('HOTEL-JULIET','T-HANGAR', weight = 300 , label = 'JULIET', color = 'gray', width = 7)


dictLabelNo = nx.get_node_attributes(G,'label')
dictCorNo = nx.get_node_attributes(G,'color')
listaCorNo = []
for key, value in dictCorNo.items():
    temp = value
    listaCorNo.append(temp)



dictLabelAresta = nx.get_edge_attributes(G,'label')
dictCorAresta = nx.get_edge_attributes(G,'color')
listaCorAresta = []
for key, value in dictCorAresta.items():
    temp = value
    listaCorAresta.append(temp)

dictLarguraAresta = nx.get_edge_attributes(G,'width')
listaLarguraAresta = []
for key, value in dictLarguraAresta.items():
    temp = value
    listaLarguraAresta.append(temp)

pos = {}
x = 0
y = 0
for no in G.nodes():
    y += 1
    if y > 5:
        y = 1
        x += 4
    pos.update({no: (x, y)})


fig1 = plt.figure('Taxiways')
nx.draw(G, pos, labels = dictLabelNo, node_color = listaCorNo,\
    edge_color = listaCorAresta, width = listaLarguraAresta)

nx.draw_networkx_edge_labels(G, pos,edge_labels = dictLabelAresta, font_color='black')
plt.axis('off')
plt.show()
