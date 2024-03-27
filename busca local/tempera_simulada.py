import math
import random


def atualizar_estado(percepcao):
  return percepcao

def formular_problema(estado):

  def heuristica(estado):
    # estado: tupla com 8 elementos, cada elemento é um inteiro de 0 a 7
    # os numeros são as posicoes das rainhas nas linhas do tabuleiro, e o index é a posição nas colunas
    # número de pares de rainhas se atacando direta ou indiretamente

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
  
  def getVizinhos(estado):
    vizinhos = []
    # os vizinhos são os estados que podem ser gerados a partir de um estado
    # consiste em pegar cada rainha e mover ela para outra posição na mesma linha
    # de	forma	que	cada	estado	tenha	8	×	7	=	56	sucessores

    for i, rainha in enumerate(estado):
      for j in range(8):
        if j != rainha:
          vizinho = list(estado)
          vizinho[i] = j
          vizinhos.append(tuple(vizinho))

    return vizinhos

  def nextRandom(estado):
    vizinhos = getVizinhos(estado)
    return random.choice(vizinhos)
  
  # escalonador linear
  # def escalonamento(t):
  #   return 1000 - t

  # escalonador exponencial
  def escalonamento(t):
    return round(1000 * math.exp(-0.01 * t), 2)

  return {
    'estadoInicial': estado,
    'heuristica': heuristica,
    'nextRandom': nextRandom,
    'escalonamento': escalonamento
  }

def busca_tempera_simulada(problema):
  estadoInicial, heuristica, nextRandom, escalonamento = problema['estadoInicial'], problema['heuristica'], problema['nextRandom'], problema['escalonamento']
  corrente = {
    'estado': estadoInicial,
    'heuristica': heuristica(estadoInicial)
  }

  i = 1
  while True:
    T = escalonamento(i)
    print(corrente, T)
    if T <= 0:
      return corrente['estado']
    proximoTemp = nextRandom(corrente['estado'])
    proximo = {
      'estado': proximoTemp,
      'heuristica': heuristica(proximoTemp)
    }
    deltaE = proximo['heuristica'] - corrente['heuristica']
    if deltaE < 0: # se o vizinho tem heuristica maior então delta é positivo
      corrente = proximo
    else:
      if random.random() < math.exp(-deltaE / T):
        print('aceitou')
        corrente = proximo
    i += 1

def busca_local_tempera_simulada(percepcao):
  estado = atualizar_estado(percepcao)
  problema = formular_problema(estado)
  solucao = busca_tempera_simulada(problema)
  return solucao

def estadosAleatorios(k):
  def estadoAleatorio():
    return tuple([random.randint(0, 7) for _ in range(8)])
  return [estadoAleatorio() for _ in range(k)]
  

# os numeros são as posicoes das rapinhas no tabuleiro
resultado = busca_local_tempera_simulada(estadosAleatorios(1)[0])
print(resultado) # (0, 4, 7, 5, 2, 6, 1, 3)