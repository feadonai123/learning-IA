# função ALGORITMO-GENÉTICO(população, FN-ADAPTA) retorna um indivíduo
# entradas: população, um conjunto de indivíduos
# FN-ADAPTA, uma função que mede a adaptação de um indivíduo
# repita
# nova_população ← conjunto vazio
# para i = 1 até TAMANHO(população) faça
# x ← SELEÇÃO-ALEATÓRIA(população, FN-ADAPTA)
# y ← SELEÇÃO-ALEATÓRIA(população, FN-ADAPTA)
# filho ← REPRODUZ(x, y)
# se (pequena probabilidade aleatória) então filho ← MUTAÇÃO(filho)
# adicionar filho a nova_população
# população ← nova_população
# até algum indivíduo estar adaptado o suficiente ou até ter decorrido tempo suficiente
# retornar o melhor indivíduo em população, de acordo com FN-ADAPTA
# _____________________________________________________________________________________________________________
# função REPRODUZ(x, y) retorna um indivíduo
# entradas: x, y, indivíduos pais
# n ← COMPRIMENTO(x)c ← número aleatório de 1 a n
# retornar CONCATENA(SUBCADEIA(x, 1 c), SUBCADEIA(y, c + 1, n))


import random

def funcao_adaptativa(individuo):
  # individuo na forma de uma tupla com 8 elementos, cada elemento é um inteiro de 0 a 7
  # cada número é a posição de uma rainha em uma coluna
  # retorn
  # a o número de pares de rainhas não atacantes, que têm o valor 28 para uma solução

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
  for i, rainha1 in enumerate(individuo):
    for j, rainha2 in enumerate(individuo[i+1:], start=i+1):
      if atacando((i, rainha1), (j, rainha2)):
        qtdAtaques += 1

  return 28 - qtdAtaques

def algoritmo_genetico(populacao, fnAdaptativa):

  def selecaoAleatoria(populacao, fnAdaptativa):
    # aplicar a função de adaptação em cada individuo da população
    valorAdaptacaoIndividuos = [fnAdaptativa(individuo) for individuo in populacao]

    # print("Adaptacao", valorAdaptacaoIndividuos)
    # soma o valor de adaptação de todos os individuos
    somaAdaptacao = sum(valorAdaptacaoIndividuos)
    # define a probabilidade de cada individuo, como sendo a sua adaptação dividida pela soma das adaptações
    probabilidades = [valor / somaAdaptacao for valor in valorAdaptacaoIndividuos]
    
    # print("Probabilidades", probabilidades)
    # e retornar um individuo aleatorio com base na probabilidade de adaptação
    return random.choices(populacao, weights=probabilidades)[0]

  def reproduzir(x, y):
    # retornar um individuo filho com base nos individuos pais x e y
    # etapas de crossover e mutacao

    # divide o individuo em duas partes
    randomCorte = random.randint(1, len(x) - 1)

    # faz o crossover
    filho1 = x[:randomCorte] + y[randomCorte:]
    filho2 = y[:randomCorte] + x[randomCorte:]

    return [filho1, filho2]

  def mutacao(filho):
    # aplicar mutação no individuo filho
    # trocar um gene aleatorio

    # escolhe uma posicao aleatoria
    posicao = random.randint(0, len(filho) - 1)
    valor = random.randint(0, len(filho) - 1)

    filho[posicao] = valor
    return filho

  count = 0
  while True:
    novaPopulacao = []

    # print("\nGeracao", count, populacao, max([fnAdaptativa(individuo) for individuo in populacao]))

    for i in range(len(populacao) // 2):
      x = selecaoAleatoria(populacao, fnAdaptativa)
      y = selecaoAleatoria(populacao, fnAdaptativa)

      filhos = reproduzir(x, y)
      # print("\nPais", x, y, "Filhos", filhos)

      for i in range(len(filhos)):
        if random.random() < 0.1:
          filhos[i] = mutacao(filhos[i])

      novaPopulacao.extend(filhos)

    populacao = novaPopulacao

    for individuo in populacao:
      if fnAdaptativa(individuo) == 28:
        return individuo
      
    if(count >= 1000):
      return max(populacao, key=fnAdaptativa)
      
    count += 1

def estadosAleatorios(k):
  def estadoAleatorio():
    return [random.randint(0, 7) for _ in range(8)]
  return [estadoAleatorio() for _ in range(k)]
  

solucao = algoritmo_genetico(estadosAleatorios(100), funcao_adaptativa)
print("\n SOLUÇÃO", solucao, funcao_adaptativa(solucao)) # (0, 4, 7, 5, 2, 6, 1, 3) 28