# IA: Problema caixeiro viajante com tempera simulada


# Matriz de distâncias entre as cidades
# distancias = [
#   [0, 29, 20, 21],
#   [29, 0, 15, 29],
#   [20, 15, 0, 26],
#   [21, 29, 26, 0]
# ]
# Cada linha da matriz representa uma cidade e cada coluna representa a distância para as outras cidades
# A cidade 0 tem distância 0 para si mesma, 29 para a cidade 1, 20 para a cidade 2 e 21 para a cidade 3

# ESTADOS: Um array do tamanho do número de cidades + 1, onde cada elemento é um número de 0 a n-1, representando a ordem em que as cidades serão visitadas
# Ex: [0, 1, 2, 3, 0] representa a ordem de visitação das cidades 0, 1, 2 e 3, voltando para a cidade 0

# HEURÍSTICA: A distância total percorrida no caminho. Quanto menor, melhor. Como não sabemos qual é o valor do menor caminho, teremos que percorrer o algoritmo inteiro até T acabar, e retornar o melhor estado, ou sejam n há um retorno rápido ao encontrar o melhor caminho



# como o caminho na qual encontramos a solução não importa, nossos estados já serão o percurso completo. Ou seja, não vamos nos preocupar em ficar construindo o nosso caminho, pois ele já estará completo. A preocupação será permutar as cidades de forma a encontrar o melhor caminho.

import math
import random

NUMERO_CIDADES = 10
distancias = []

def estadosAleatorios(n):
  estados = []
  for _ in range(n):
    cidades = list(range(NUMERO_CIDADES))
    random.shuffle(cidades)
    cidades.append(cidades[0])
    estados.append(cidades)
  
  return estados

def distanciaAleatoria(n):
  distancias = []
  for i in range(n):
    distancias.append([])
    for j in range(n):
      if i == j:
        distancias[i].append(0)
      else:
        distancias[i].append(random.randint(1, 30))

  return distancias

def distancia(cidade1, cidade2):
  return distancias[cidade1][cidade2]

def heuristica(estado):
  custo = 0
  for i in range(len(estado) - 1):
    custo += distancia(estado[i], estado[i+1])

  return custo

def escalonador(t):
  # linear decay
  return round(5000 - 0.01 * t, 2)

def vizinhos(estado):
  vizinhos = []
  for i in range(1, len(estado) - 1):
    for j in range(i + 1, len(estado) - 1):
      vizinho = list(estado)
      vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
      vizinhos.append(vizinho)

  return vizinhos

def temperaSimulada():
  global distancias

  # estadoInicial = estadosAleatorios(1)[0]
  estadoInicial = [4, 0, 2, 3, 1, 8, 9, 6, 5, 7, 4]
  # distancias = distanciaAleatoria(NUMERO_CIDADES)
  distancias =  [[0, 14, 29, 14, 6, 25, 2, 4, 6, 5], [8, 0, 28, 15, 29, 15, 1, 23, 28, 7], [12, 7, 0, 29, 17, 26, 11, 3, 4, 17], [23, 13, 19, 0, 11, 30, 29, 2, 22, 26], [4, 4, 23, 21, 0, 7, 25, 19, 25, 6], [20, 14, 24, 30, 27, 0, 7, 14, 22, 29], [17, 21, 23, 3, 3, 23, 0, 16, 26, 30], [4, 4, 16, 14, 29, 8, 22, 0, 22, 29], [14, 18, 12, 24, 19, 18, 12, 12, 0, 3], [14, 16, 1, 12, 15, 6, 9, 9, 19, 0]]

  print('estado inicial', estadoInicial)
  print('distancias', distancias)

  no = {
    'estado': estadoInicial,
    'heuristica': heuristica(estadoInicial)
  }

  melhorNo = {
    'estado': estadoInicial,
    'heuristica': heuristica(estadoInicial)
  }

  contador = 0
  seq = 0

  while True:
    t = escalonador(contador)

    # print(t, no)

    if t <= 0 or seq >= 10:
      return melhorNo['estado']

    vizinhosEstado = vizinhos(no['estado'])
    vizinhoAleatorio = random.choice(vizinhosEstado)
    heuristicaVizinho = heuristica(vizinhoAleatorio)

    deltaE = heuristicaVizinho - no['heuristica']
    # se deltaE for negativo, o vizinho é melhor que o estado atual, então devemos atualizar o estado atual

    if deltaE < 0 or random.random() < math.exp(-deltaE / t):
      if no['estado'] != vizinhoAleatorio:
        seq = 0
      else:
        seq += 1

      no = {
        'estado': vizinhoAleatorio,
        'heuristica': heuristicaVizinho
      }

      if no['heuristica'] < melhorNo['heuristica']:
        melhorNo = no

    contador += 1

estadoFinal = temperaSimulada()
print('estado final', estadoFinal, 'heuristica', heuristica(estadoFinal))


# estado inicial [1, 2, 3, 0, 1]
# distancias [[0, 4, 16, 23], [14, 0, 5, 13], [14, 25, 0, 23], [22, 6, 14, 0]]
# estado final [1, 3, 2, 0, 1] heuristica 45