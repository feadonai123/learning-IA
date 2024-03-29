# exemplo algoritmo genético para problema das 8 rainhas

# ESTADO: será representado por uma lista de 8 elementos, onde cada elemento é um número de 0 a 7. cada número representa a coluna em que a rainha está naquela linha
# FUNCAO ADAPTATIVA: o número de pares de rainhas não atacantes, que têm o valor 28 para uma solução. Quanto maior (até 28), mais adaptado é o individuo


import random

def funcaoAdaptatica(estado):
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

  return 28 - qtdAtaques

def selecionarPais(populacao, probabilidades):
  return random.choices(populacao, weights=probabilidades, k=2)

def getProbabilidades(populacao):
  valorAdaptacaoIndividuos = [funcaoAdaptatica(individuo) for individuo in populacao]
  somaAdaptacao = sum(valorAdaptacaoIndividuos)
  return [valor / somaAdaptacao for valor in valorAdaptacaoIndividuos]

def reproduzir(x, y):
  randomCorte = random.randint(1, len(x) - 1)

  filho1 = x[:randomCorte] + y[randomCorte:]
  filho2 = y[:randomCorte] + x[randomCorte:]

  return [filho1, filho2]

def mutacao(filho):
  posicao = random.randint(0, len(filho) - 1)
  valor = random.randint(0, len(filho) - 1)

  filho[posicao] = valor
  return filho

def estadosAleatorios(n):
  return [[random.randint(0, 7) for _ in range(8)] for _ in range(n)]

def algoritmoGenetico(tamanhoPopulacao, numeroGeracoes, probabilidadeMutacao):
  populacao = estadosAleatorios(tamanhoPopulacao)
  geracoes = numeroGeracoes

  for _ in range(geracoes):
    probabilidades = getProbabilidades(populacao)
    novaPopulacao = []

    for _ in range(tamanhoPopulacao // 2):
      pai1, pai2 = selecionarPais(populacao, probabilidades)
      filhos = reproduzir(pai1, pai2)

      for filho in filhos:
        if random.random() < probabilidadeMutacao:
          filho = mutacao(filho)

      novaPopulacao.extend(filhos)

    populacao = novaPopulacao

    for individuo in populacao:
      if funcaoAdaptatica(individuo) == 28:
        return individuo
      
  return max(populacao, key=funcaoAdaptatica)

TAMANHO_POPULACAO = 100
NUMERO_GERACOES = 1000
PROBABILIDADE_MUTACAO = 0.2

estadoFinal = algoritmoGenetico(TAMANHO_POPULACAO, NUMERO_GERACOES, PROBABILIDADE_MUTACAO)
print('estado final', estadoFinal, 'funcaoAdaptativa', funcaoAdaptatica(estadoFinal))