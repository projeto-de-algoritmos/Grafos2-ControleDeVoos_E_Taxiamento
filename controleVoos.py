import pandas as pd
import json
from networkx import nx
from funcoesGrafo import *

df = pd.read_csv('cleaned_and_sampled_flights_v2.csv')
df = df.drop_duplicates(subset=['ORIGIN_AIRPORT', 'DESTINATION_AIRPORT'], keep='first')
df.to_json('Voos.json')

with open('Voos.json') as json_file:
    data = json.load(json_file)

with open('VoosLinhaUnica.json') as json_file:
    searchData = json.load(json_file)


listaDeAdjacencia = {}
listaAeroportos = []

for (key, aeroportoOrigem) in data['ORIGIN_AIRPORT'].items():
    if not listaDeAdjacencia.get(aeroportoOrigem):
        listaDeAdjacencia[aeroportoOrigem] = []
        listaAeroportos.append(aeroportoOrigem)

    listaDeAdjacencia[aeroportoOrigem].append(data['DESTINATION_AIRPORT'][key])

with open('listaAdjacencia.json', 'w') as json_file:
    json.dump(listaDeAdjacencia, json_file)

G = nx.Graph()
labels = {}

for aeroporto, rotas in listaDeAdjacencia.items():
    labels[aeroporto] = aeroporto
    G.add_node(aeroporto)

    for rota in rotas:        
       G.add_edge(aeroporto, rota, weight = recupera_distancia(searchData, aeroporto, rota))


print("Nodes in G: ", G.nodes(data=True))
print("Edges in G: ", G.edges(data=True))