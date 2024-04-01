import math
import random


def formularProblema(estado, distancias, probMutacao):
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
    i,j = random.sample(range(1, len(filho) - 1), 2)
    filho[i], filho[j] = filho[j], filho[i]
    return filho.copy()

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
  
  return {
    'estadoInicial': estadoInicial,
    'vizinhos': vizinhos,
    'custo': custo,
    'funcaoAdaptativa': funcaoAdaptativa,
    'cruzamento': cruzamento,
    'mutacao': mutacao,
    'selecao': selecaoRoletaViciada,
    'probMutacao': probMutacao
    # 'modeloTransicao',
    # 'acoes',
    # 'testeObjetivo'
  }

def exec(problema, qtdGeracoes, logs = False):
  estadoInicial = problema['estadoInicial']
  custo = problema['custo']
  cruzamento = problema['cruzamento']
  mutacao = problema['mutacao']
  selecao = problema['selecao']
  probMutacao = problema['probMutacao']

  populacao = estadoInicial
  melhorEstado = {
    'estado': min(populacao, key=custo),
    'custo': custo(min(populacao, key=custo))
  }

  for geracao in range(qtdGeracoes):

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

      if random.random() < probMutacao:
        filho1 = mutacao(filho1)

      if random.random() < probMutacao:
        filho2 = mutacao(filho2)

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

    if logs:
      print("\nGERACAO", geracao)
      print('Melhor estado geracao:', melhorEstadoGeracao['estado'], melhorEstadoGeracao['custo'])
      print('Melhor estado global:', melhorEstado['estado'], melhorEstado['custo'])
      # for individuo in populacao:
      #   print('Individuo:', individuo, 'Custo:', custo(individuo))

    # print('Melhor estado geração:', melhorEstadoGeracao['estado'], 'Custo:', melhorEstadoGeracao['custo'])
    # print('Melhor estado geral:', melhorEstado['estado'], 'Custo:', melhorEstado['custo'])

  print("\nFIM AG")
  print('Melhor estado:', melhorEstado['estado'])
  print('Custo melhor estado:', melhorEstado['custo'])
  return melhorEstado['estado']