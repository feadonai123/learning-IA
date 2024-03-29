# exemplo tempera simulada para problema das 8 rainhas

# ESTADO: será representado por uma lista de 8 elementos, onde cada elemento é um número de 0 a 7. cada número representa a coluna em que a rainha está naquela linha
# HEURÍSTICA: será o número de pares de rainhas se atacando direta ou indiretamente. Quanto menor, melhor
# AÇÕES: mover uma rainha para uma linha na mesma coluna
# AÇÕES PARA CADA ESTADO: Todos os estados possuem as mesmas ações possiveis, que são mover qualquer rainha para uma linha na mesma coluna

import math
import random


def estadosAleatorios(n):
  return [[random.randint(0, 7) for _ in range(8)] for _ in range(n)]

def heuristica(estado):
  def atacando(rainha1, rainha2):
    rainha1_linha, rainha1_coluna = rainha1
    rainha2_linha, rainha2_coluna = rainha2

    if rainha1_linha == rainha2_linha:
      return True

    if rainha1_coluna == rainha2_coluna:
      return True
    
    if abs(rainha1_linha - rainha2_linha) == abs(rainha1_coluna - rainha2_coluna):
      return True
    
    return False

  qtdAtaques = 0
  for i, rainha1 in enumerate(estado):
    for j, rainha2 in enumerate(estado[i+1:], start=i+1):
      if atacando((i, rainha1), (j, rainha2)):
        qtdAtaques += 1

  return qtdAtaques

def vizinhos(estado):
  vizinhos = []
  for i, rainha in enumerate(estado):
    for j in range(8):
      if j != rainha:
        vizinho = list(estado)
        vizinho[i] = j
        vizinhos.append(tuple(vizinho))

  return vizinhos

def escalonador(t):
  return round(1000 * math.exp(-0.01 * t), 2)

def temperaSimulada():
  estadoInicial = estadosAleatorios(1)[0]

  print('estado inicial', estadoInicial)
  no = {
    'estado': estadoInicial,
    'heuristica': heuristica(estadoInicial)
  }

  contador = 0

  while True:
    t = escalonador(contador)

    print(no, t)

    if t <= 0:
      return no['estado']

    vizinhosEstado = vizinhos(no['estado'])

    vizinhoAleatorio = random.choice(vizinhosEstado)
    heuristicaVizinho = heuristica(vizinhoAleatorio)

    if heuristicaVizinho == 0:
      return vizinhoAleatorio
    
    deltaE = heuristicaVizinho - no['heuristica']

    if deltaE < 0:
      no = {
        'estado': vizinhoAleatorio,
        'heuristica': heuristicaVizinho
      }
    elif random.random() < math.exp(deltaE / t):
      no = {
        'estado': vizinhoAleatorio,
        'heuristica': heuristicaVizinho
      }

    contador += 1

estadoFinal = temperaSimulada()
print('estado final', estadoFinal, 'heuristica', heuristica(estadoFinal))