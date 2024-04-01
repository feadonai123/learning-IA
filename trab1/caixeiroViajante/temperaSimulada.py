import math
import random

def formularProblema(estado, distancias):
  estadoInicial = estado

  def vizinhos(estado):
    vizinhos = []
    for i in range(1, len(estado) - 1):
      for j in range(i + 1, len(estado) - 1):
        vizinho = list(estado)
        vizinho[i] = estado[j]
        vizinho[j] = estado[i]
        vizinhos.append(vizinho)

    return vizinhos
  
  def custo(estado):
    custo = 0
    for i in range(len(estado) - 1):
      custo += distancias[estado[i]][estado[i+1]]

    custo += distancias[estado[-1]][estado[0]]

    return custo
  
  def escalonador(t):
    return round(5000 - 0.01 * t, 2)
  
    # start = 5000
    # end = 5000000

    # # linear decay: ax + b
    # # b = start
    # # a = -b / end
    # # value = a * t + b
    # # return round(value)

    # # exponential decay: a^x + b
    # b = start
    # a = start / pow(end, 2)
    # value = -a * pow(t, 2) + b
    # return round(value)
  
  return {
    'estadoInicial': estadoInicial,
    'vizinhos': vizinhos,
    'custo': custo,
    'escalonador': escalonador
    # 'modeloTransicao',
    # 'acoes',
    # 'testeObjetivo'
  }

def exec(problema, logs = False):
  estadoInicial = problema['estadoInicial']
  vizinhos = problema['vizinhos']
  custo = problema['custo']
  escalonador = problema['escalonador']

  current = {
    'estado': estadoInicial,
    'custo': custo(estadoInicial)
  }

  melhorEstado = {
    'estado': estadoInicial,
    'custo': custo(estadoInicial)
  }

  count = 0
  while True:
    t = escalonador(count)

    if logs:
      print("\n", t, current['estado'], current['custo'])

    if t <= 0:
      print("\nFIM TÊMPERA SIMULADA")
      print('Melhor estado:', melhorEstado['estado'])
      print('Custo melhor estado:', melhorEstado['custo'])
      return melhorEstado['estado']
    
    vizinho = random.choice(vizinhos(current['estado']))
    custoVizinho = custo(vizinho)

    delta = custoVizinho - current['custo']
    if delta < 0 or random.random() < math.exp(-delta / t):
      current['estado'] = vizinho
      current['custo'] = custoVizinho
     
      if current['custo'] < melhorEstado['custo']:
        melhorEstado['estado'] = current['estado']
        melhorEstado['custo'] = current['custo']

    count += 1