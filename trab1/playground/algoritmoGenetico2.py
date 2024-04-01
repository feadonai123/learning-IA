# Algoritmo Genético para problema do caixeiro viajante


import math
import random


###################### FUNÇÃO DO AGENTE ######################

def formularProblema(estado, distancias, qtdGeracoes):
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

  def funcaoAdaptativa(estado):
    return 1 / (pow(custo(estado), 8) + 1);

  def cruzamento(pai1, pai2):
    pontoCrossOverInicio = random.randint(0, len(pai1) // 2)
    pontoCrossOverFim = pontoCrossOverInicio + len(pai1) // 2

    filho1 = [None] * len(pai1)
    for i in range(pontoCrossOverInicio, pontoCrossOverFim):
      filho1[i] = pai1[i]

    for i in range(len(filho1)):
      if filho1[i] is None:
        for j in range(len(pai2)):
          if pai2[j] not in filho1:
            filho1[i] = pai2[j]
            break

    filho2 = [None] * len(pai2)
    for i in range(pontoCrossOverInicio, pontoCrossOverFim):
      filho2[i] = pai2[i]

    for i in range(len(filho2)):
      if filho2[i] is None:
        for j in range(len(pai1)):
          if pai1[j] not in filho2:
            filho2[i] = pai1[j]
            break

    return filho1, filho2

  def mutacao(filho):
    random.shuffle(filho)
    return filho.copy()

    # i,j = random.sample(range(1, len(filho) - 1), 2)
    # filho[i], filho[j] = filho[j], filho[i]
    # return filho.copy()

  def selecaoRoletaViciada(populacao, numPares):    
    individuosInicial = [{ 'estado': individuo, 'adaptacao': funcaoAdaptativa(individuo) } for individuo in populacao]

    def getProbabilidade(individuos):
      somaAptidoes = sum([individuo['adaptacao'] for individuo in individuos])
      return [individuo['adaptacao'] / somaAptidoes for individuo in individuos]

    pares = []

    for _ in range(numPares):
      individuos = list(individuosInicial)
      # print('Probabilidade pai1:', getProbabilidade(individuos))
      pai1 = random.choices(individuos, weights=getProbabilidade(individuos))[0]
      individuos.remove(pai1)

      for par in pares:
        if par[0] == pai1 and par[1] in individuos:
          individuos.remove(par[1])
        if par[1] == pai1 and par[0] in individuos:
          individuos.remove(par[0])

      # print('Probabilidade pai2:', getProbabilidade(individuos))
      pai2 = random.choices(individuos, weights=getProbabilidade(individuos))[0]
      pares.append((pai1, pai2))

    paresFormatados = [(par[0]['estado'],par[1]['estado']) for par in pares]
    return paresFormatados
  
  def escalonador(t, start = qtdGeracoes / 2, end = qtdGeracoes):
    # linear decay: ax + b
    # b = start
    # a = -b / end
    # value = a * t + b
    # normalized = round(value / start)
    # return normalized
  
    # exponential decay: a^x + b
    b = start
    a = start / pow(end, 2)
    value = -a * pow(t, 2) + b
    normalized = round(value / start, 2)
    return normalized
  
    # return 0.2
    
  
  return {
    'estadoInicial': estadoInicial,
    'vizinhos': vizinhos,
    'custo': custo,
    'funcaoAdaptativa': funcaoAdaptativa,
    'cruzamento': cruzamento,
    'mutacao': mutacao,
    'selecao': selecaoRoletaViciada,
    'escalonador': escalonador
    # 'modeloTransicao',
    # 'acoes',
    # 'testeObjetivo'
  }

###################### AG ######################

def algoritmoGenetico(problema, qtdGeracoes):
  estadoInicial = problema['estadoInicial']
  custo = problema['custo']
  cruzamento = problema['cruzamento']
  mutacao = problema['mutacao']
  selecao = problema['selecao']
  escalonador = problema['escalonador']

  populacao = estadoInicial
  melhorEstado = {
    'estado': min(populacao, key=custo),
    'custo': custo(min(populacao, key=custo))
  }

  for geracao in range(qtdGeracoes):

    t = escalonador(geracao)

    # print("\nGERACAO", geracao, t)
    # for individuo in populacao:
    #   print('Individuo:', individuo, 'Custo:', custo(individuo))

    melhorEstadoGeracao = {
      'estado': None,
      'custo': math.inf
    }
    novaPopulacao = []
    pares = selecao(populacao, len(populacao) // 2)

    for par in pares:
      pai1, pai2 = par

      filho1, filho2 = cruzamento(pai1, pai2)

      # print('Pais:', pai1, pai2)
      # print('Filhos:', filho1, filho2)

      if random.random() < t:
        filho1 = mutacao(filho1)

      if random.random() < t:
        filho2 = mutacao(filho2)

      # if random.random() < PROBABILIDADE_MUTACAO:
      #   filho1 = mutacao(filho1)

      # if random.random() < PROBABILIDADE_MUTACAO:
      #   filho2 = mutacao(filho2)

      # print('Filhos pós mutacao:', filho1, filho2)


      novaPopulacao.append(filho1)
      novaPopulacao.append(filho2)
     
      if custo(filho1) < melhorEstadoGeracao['custo']:
        melhorEstadoGeracao = {
          'estado': filho1,
          'custo': custo(filho1)
        }

      if custo(filho2) < melhorEstadoGeracao['custo']:
        melhorEstadoGeracao = {
          'estado': filho2,
          'custo': custo(filho2)
        }

    populacao = novaPopulacao

    if melhorEstadoGeracao['custo'] < melhorEstado['custo']:
      melhorEstado = melhorEstadoGeracao

    # print('Melhor estado geração:', melhorEstadoGeracao['estado'], 'Custo:', melhorEstadoGeracao['custo'])
    # print('Melhor estado geral:', melhorEstado['estado'], 'Custo:', melhorEstado['custo'])

  print("\n FIM")
  print('Melhor estado:', melhorEstado['estado'])
  print('Custo melhor estado:', melhorEstado['custo'])
  return melhorEstado['estado']
     
###################### PROGRAMA DO AGENTE ######################

estado = None

def atualizarEstado(percepcao, estado):
  return percepcao

def programaAgente(percepcao, distancias, qtdGeracoes):
  global estado

  # fase atualização do estado
  estado = atualizarEstado(percepcao, estado)

  # fase formulação do problema
  problema = formularProblema(estado, distancias, qtdGeracoes)

  # fase busca da solução
  solucao = algoritmoGenetico(problema, qtdGeracoes)

  # fase execução da solução: Aqui o ideal seria o agente retornar cada ação individualmente que levará a solução encontrada. Para facilitar, estou retornando a solução completa
  return solucao


###################### TESTE DO AGENTE ######################


QUANTIDADE_CIDADES = 10
QUANTIDADE_GENERACOES = 100
TAMANHO_POPULACAO = 50
PROBABILIDADE_MUTACAO = 0.2


def estadosAleatorios(n = TAMANHO_POPULACAO):
  cidades = [i for i in range(QUANTIDADE_CIDADES)]
  
  estados = []
  for _ in range(n):
    cidadesCopia = list(cidades)
    random.shuffle(cidadesCopia)
    estados.append(cidadesCopia)

  return estados

def cidadesAleatorias(qtdCidades):
  cidades = []
  for _ in range(qtdCidades):
    cidades.append((random.randint(1, 100), random.randint(1, 100)))

  return cidades

def matrixDistancias(cidades):
  def dist(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx * dx + dy * dy)
  
  distancias = []
  for i in range(len(cidades)):
    distancias.append([])
    for j in range(len(cidades)):
      distancias[i].append(dist(cidades[i][0], cidades[i][1], cidades[j][0], cidades[j][1]))

  return distancias

estadoInicial = estadosAleatorios(TAMANHO_POPULACAO)
cidades = cidadesAleatorias(QUANTIDADE_CIDADES)
distancias = matrixDistancias(cidades)

# estadoInicial = [[2, 4, 8, 3, 9, 0, 5, 7, 1, 6], [7, 3, 4, 0, 8, 5, 2, 9, 6, 1], [5, 3, 9, 8, 7, 2, 6, 4, 0, 1], [0, 1, 6, 9, 8, 5, 2, 7, 3, 4], [8, 7, 4, 9, 1, 6, 3, 2, 5, 0], [9, 3, 5, 0, 6, 2, 1, 7, 8, 4], [5, 8, 6, 9, 1, 7, 0, 3, 2, 4], [7, 8, 0, 1, 2, 5, 6, 3, 4, 9], [3, 4, 8, 5, 6, 0, 9, 1, 7, 2], [3, 0, 8, 4, 1, 6, 2, 7, 5, 9]]
cidades =  [(82, 3), (88, 16), (29, 55), (84, 86), (57, 29), (10, 85), (35, 30), (54, 10), (80, 52), (78, 60)]
distancias = [[0.0, 14.317821063276353, 74.24957912338628, 83.02409288875127, 36.069377593742864, 109.12378292562992, 54.20332093147061, 28.861739379323623, 49.040799340956916, 57.14017850864661], [14.317821063276353, 0.0, 70.7248188403477, 70.11419257183242, 33.61547262794322, 104.1393297462587, 54.817880294662984, 34.52535300326414, 36.87817782917155, 45.12205669071391], [74.24957912338628, 70.7248188403477, 0.0, 63.13477647065839, 38.2099463490856, 35.510561809129406, 25.709920264364882, 51.478150704935004, 51.088159097779204, 49.25444142409901], [83.02409288875127, 70.11419257183242, 63.13477647065839, 0.0, 63.071388124885914, 74.00675644831355, 74.41102068914255, 81.70679286326198, 34.23448553724738, 26.68332812825267], [36.069377593742864, 33.61547262794322, 38.2099463490856, 63.071388124885914, 0.0, 73.10950690573696, 22.02271554554524, 19.235384061671343, 32.526911934581186, 37.44329045369811], [109.12378292562992, 104.1393297462587, 35.510561809129406, 74.00675644831355, 73.10950690573696, 0.0, 60.41522986797286, 86.95401083331349, 77.38862965578342, 72.44998274671983], [54.20332093147061, 54.817880294662984, 25.709920264364882, 74.41102068914255, 22.02271554554524, 60.41522986797286, 0.0, 27.586228448267445, 50.08991914547278, 52.43090691567332], [28.861739379323623, 34.52535300326414, 51.478150704935004, 81.70679286326198, 19.235384061671343, 86.95401083331349, 27.586228448267445, 0.0, 49.39635614091387, 55.46169849544819], [49.040799340956916, 36.87817782917155, 51.088159097779204, 34.23448553724738, 32.526911934581186, 77.38862965578342, 50.08991914547278, 49.39635614091387, 0.0, 8.246211251235321], [57.14017850864661, 45.12205669071391, 49.25444142409901, 26.68332812825267, 37.44329045369811, 72.44998274671983, 52.43090691567332, 55.46169849544819, 8.246211251235321, 0.0]]

# Melhor estado: [4, 7, 0, 1, 8, 9, 3, 5, 2, 6]
# Custo melhor estado: 291.47261578028395

print("Estado inicial: ", estadoInicial)
print("Cidades: ", cidades)
print("Distâncias: ", distancias)
programaAgente(estadoInicial, distancias, QUANTIDADE_GENERACOES)