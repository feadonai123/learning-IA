# tempera simulada para problema do caixeiro viajante

import math
import random


###################### FUNÇÃO DO AGENTE ######################

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

###################### BUSCA ######################


def temperaSimulada(problema):
  estadoInicial, vizinhos, custo, escalonador = problema['estadoInicial'], problema['vizinhos'], problema['custo'], problema['escalonador']

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

    if t <= 0:
      print('Custo melhor solução:', melhorEstado['custo'])
      print('Melhor solução:', melhorEstado['estado'])
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

###################### PROGRAMA DO AGENTE ######################

def atualizarEstado(percepcao, estado):
  return percepcao

estado = None

def programaAgente(percepcao, distancias):
  global estado

  print(percepcao, distancias)

  # fase atualização do estado
  estado = atualizarEstado(percepcao, estado)

  # fase formulação do problema
  problema = formularProblema(estado, distancias)

  # fase busca da solução
  solucao = temperaSimulada(problema)

  # fase execução da solução: Aqui o ideal seria o agente retornar cada ação individualmente que levará a solução encontrada. Para facilitar, estou retornando a solução completa
  return solucao

###################### TESTE DO AGENTE ######################

QUANTIDADE_CIDADES = 10

def estadosAleatorios(n):
  cidades = [i for i in range(QUANTIDADE_CIDADES)]
  
  estados = []
  for _ in range(n):
    cidadesCopia = list(cidades)
    random.shuffle(cidadesCopia)
    estados.append(cidadesCopia)

  return estados

def distanciaAleatoria(n = QUANTIDADE_CIDADES):
  distancias = []
  for i in range(n):
    distancias.append([])
    for j in range(n):
      if i == j:
        distancias[i].append(0)
      else:
        distancias[i].append(random.randint(1, 30))

  return distancias

# estadoInicial = estadosAleatorios(1)[0]
# estadoInicial = [1, 2, 3, 0]
# distancias = distanciaAleatoria()
# distancias = [[0, 4, 16, 23], [14, 0, 5, 13], [14, 25, 0, 23], [22, 6, 14, 0]]

# estadoInicial = [2, 4, 8, 3, 9, 0, 5, 7, 1, 6]
estadoInicial = [1, 6, 9, 4, 8, 3, 5, 2, 0, 7]

distancias = [[0.0, 14.317821063276353, 74.24957912338628, 83.02409288875127, 36.069377593742864, 109.12378292562992, 54.20332093147061, 28.861739379323623, 49.040799340956916, 57.14017850864661], [14.317821063276353, 0.0, 70.7248188403477, 70.11419257183242, 33.61547262794322, 104.1393297462587, 54.817880294662984, 34.52535300326414, 36.87817782917155, 45.12205669071391], [74.24957912338628, 70.7248188403477, 0.0, 63.13477647065839, 38.2099463490856, 35.510561809129406, 25.709920264364882, 51.478150704935004, 51.088159097779204, 49.25444142409901], [83.02409288875127, 70.11419257183242, 63.13477647065839, 0.0, 63.071388124885914, 74.00675644831355, 74.41102068914255, 81.70679286326198, 34.23448553724738, 26.68332812825267], [36.069377593742864, 33.61547262794322, 38.2099463490856, 63.071388124885914, 0.0, 73.10950690573696, 22.02271554554524, 19.235384061671343, 32.526911934581186, 37.44329045369811], [109.12378292562992, 104.1393297462587, 35.510561809129406, 74.00675644831355, 73.10950690573696, 0.0, 60.41522986797286, 86.95401083331349, 77.38862965578342, 72.44998274671983], [54.20332093147061, 54.817880294662984, 25.709920264364882, 74.41102068914255, 22.02271554554524, 60.41522986797286, 0.0, 27.586228448267445, 50.08991914547278, 52.43090691567332], [28.861739379323623, 34.52535300326414, 51.478150704935004, 81.70679286326198, 19.235384061671343, 86.95401083331349, 27.586228448267445, 0.0, 49.39635614091387, 55.46169849544819], [49.040799340956916, 36.87817782917155, 51.088159097779204, 34.23448553724738, 32.526911934581186, 77.38862965578342, 50.08991914547278, 49.39635614091387, 0.0, 8.246211251235321], [57.14017850864661, 45.12205669071391, 49.25444142409901, 26.68332812825267, 37.44329045369811, 72.44998274671983, 52.43090691567332, 55.46169849544819, 8.246211251235321, 0.0]]
# Custo melhor solução: 291.4726157802839
# Melhor solução: [2, 5, 3, 9, 8, 1, 0, 7, 4, 6, 2]

programaAgente(estadoInicial, distancias)