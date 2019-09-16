# Controle de Vôos e Taxiamento

**Número da Lista**: 2<br>
**Conteúdo da Disciplina**: Grafos<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 16/0006872  |  Gabriela Chaves de Moraes |
| 16/0012961  |  Lucas Arthur Lermen |

## Sobre 
<p align="justify">Essa lista consiste de dois projetos. O <b>GrafoVoos</b> trata-se da geração da árvore geradora mínima (MST) utilizando o algoritmo de Prim para os aeroportos do mundo a partir do Dataset disponível em  <a href="https://www.kaggle.com/freddejn/flights">https://www.kaggle.com/freddejn/flights</a>  e o <b>GrafoTaxiways</b> aborda a montagem de um grafo a partir do diagrama do <b>Aeroporto Internacional de Brownsville South Padre Island (BRO)</b> e é possível realizar uma busca que resulta o menor caminho com menor custo entre pontos do aeroporto utilizando o algoritmo de Dijkstra.</p>

## Instalação 

**Linguagem**: Python v3.6 ou superior <br>

### Executando o projeto GrafoVoos

#### Pré-requisitos

``` console
$ pip3 install matplotlib

$ pip3 install pandas

$ pip3 install networkx

$ pip3 install pqdict

```

#### Comandos para executar

``` console
$ python3 controleVoos.py

```

### Executando o projeto GrafoTaxiways

#### Pré-requisitos
``` console
$ pip3 install matplotlib

$ pip3 install networkx

```

#### Comandos para executar

``` console
$ python3 taxiways.py 

```

## Uso 

#### GrafoVoos

Ao executar o comando será criada a árvore geradora mínima, utilizando o algoritmo de Prim, a partir do dataset de voos internacionais dos Estados Unidos.

#### GrafoTaxiways

Ao executar o comando será inicializado um menu com 3 opções
- 1 - Mostrar Diagrama do Aeroporto
- 2 - Perguntar ao Dijkstra (Controlador de solo) o menor caminho com menor custo entre lugares do aeroporto
- 0 - Sair

Caso deseje vizualizar a disposição do aeroporto, selecione a opção 1. Ao selecionar a opção 2, lhe será pedido para inserir o local atual que o avião se encontra e o local para onde ele deseja seguir. Lhe será retornado uma figura de uma seção do aeroporto, com pontos vermelhos indicando o traçado.



