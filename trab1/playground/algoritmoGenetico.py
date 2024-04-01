# Algoritmo genético para Caixeiro Viajante


# PROBLEMAS ENCONTRADOS:
# 1: Na etapa de cruxamento, pode acabar repetindo cidades. Ex:
# pai1 = [0, 1, 2, 3, 0]
# pai2 = [0, 3, 2, 1, 0]
# filho1 = [0, 3, 2, 3, 0]

# 2: Na etapa de mutação, pode acabar repetindo cidades. Ex:
# filho = [0, 1, 2, 3, 0]
# filho pos mutação = [0, 1, 2, 1, 0]

import random

QUANTIDADE_CIDADES = 4
QUANTIDADE_GERACOES = 1000
QUANTIDADE_POPULACAO = 100
PROBABILIDADE_MUTACAO = 0.2

distancias = []


def estadosAleatorios(n):
  primeiraCidade = random.randint(0, QUANTIDADE_CIDADES - 1)
  outrasCidades = [i for i in range(QUANTIDADE_CIDADES) if i != primeiraCidade]
  
  estados = []

  for _ in range(n - 1):
    random.shuffle(outrasCidades)

    estado = [primeiraCidade]
    estado.extend(outrasCidades)
    estado.append(primeiraCidade)

    estados.append(estado)

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

def funcaoAdaptativa(estado):
  custo = 0
  for i in range(len(estado) - 1):
    custo += distancia(estado[i], estado[i+1])

  return custo

def probabilidades(populacao):
  custos = [funcaoAdaptativa(estado) for estado in populacao]
  somaCustos = sum(custos)

  return [custo / somaCustos for custo in custos]

def selecionarPais(populacao, probabilidadesPopulacao):
  pai1, pai2 = random.choices(populacao, weights=probabilidadesPopulacao, k=2)
  return pai1, pai2

def cruzamento(pai1, pai2):
  pai1_1 = pai1[:len(pai1) // 2]
  pai2_1 = pai2[:len(pai2) // 2]

  filho1 = pai1_1
  for cidade in pai2:
    if cidade not in filho1:
      filho1.append(cidade)

  filho1.append(pai2[len(pai2) - 1])

  filho2 = pai2_1
  for cidade in pai1:
    if cidade not in filho2:
      filho2.append(cidade)

  filho2.append(pai2[len(pai2) - 1])

  return filho1, filho2

def mutacao(filho):
  i,j = random.sample(range(1, len(filho) - 1), 2)
  filho[i], filho[j] = filho[j], filho[i]
  return filho

def algoritmoGenetico():
  global distancias

  populacao = estadosAleatorios(QUANTIDADE_POPULACAO)
  # distancias = distanciaAleatoria(QUANTIDADE_CIDADES)
  distancias = [[0, 4, 16, 23], [14, 0, 5, 13], [14, 25, 0, 23], [22, 6, 14, 0]]

  print("População inicial: ", populacao)
  print("Distâncias: ", distancias)

  for _ in range(QUANTIDADE_GERACOES):
    probabilidadesPopulacao = probabilidades(populacao)
    
    novaPopulacao = []

    for _ in range(QUANTIDADE_POPULACAO // 2):
      pai1, pai2 = selecionarPais(populacao, probabilidadesPopulacao)
      filho1, filho2 = cruzamento(pai1, pai2)

      if random.random() < PROBABILIDADE_MUTACAO:
        filho1 = mutacao(filho1)
      
      if random.random() < PROBABILIDADE_MUTACAO:
        filho2 = mutacao(filho2)

      novaPopulacao.extend([filho1, filho2])

    populacao = novaPopulacao

  return min(populacao, key=funcaoAdaptativa)


estadoFinal = algoritmoGenetico()
print("Estado final: ", estadoFinal, "Função adaptativa: ", funcaoAdaptativa(estadoFinal))