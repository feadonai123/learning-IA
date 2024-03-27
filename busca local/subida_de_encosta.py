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

  def nextBetter(estado):
    # retorna um estados vizinhos com a menor heuristica
    # pega tds os estados vizinhos e retorna o que tem a menor heuristica
    vizinhos = getVizinhos(estado)
    melhorVizinho = estado

    for vizinho in vizinhos:
      if heuristica(vizinho) < heuristica(melhorVizinho):
        melhorVizinho = vizinho

    return melhorVizinho

  return {
    'estadoInicial': estado,
    'heuristica': heuristica,
    'nextBetter': nextBetter
  }

def busca_subida_de_encosta(problema):
  estadoInicial, heuristica, nextBetter = problema['estadoInicial'], problema['heuristica'], problema['nextBetter']
  corrente = {
    'estado': estadoInicial,
    'heuristica': heuristica(estadoInicial)
  }

  while True:
    print(corrente)
    nextEstado = nextBetter(corrente['estado'])
    vizinho = {
      'estado': nextEstado,
      'heuristica': heuristica(nextEstado)
    } 

    if vizinho['heuristica'] >= corrente['heuristica']: # se o vizinho não é melhor que o corrente
      return corrente['estado']
    
    corrente = vizinho

def busca_local_subida_de_encosta(percepcao):
  estado = atualizar_estado(percepcao)
  problema = formular_problema(estado)
  solucao = busca_subida_de_encosta(problema)
  return solucao

def estadosAleatorios(k):
  def estadoAleatorio():
    return tuple([random.randint(0, 7) for _ in range(8)])
  return [estadoAleatorio() for _ in range(k)]

# os numeros são as posicoes das rapinhas no tabuleiro
resultado = busca_local_subida_de_encosta(estadosAleatorios(1)[0])
print(resultado) # (0, 4, 7, 5, 2, 6, 1, 3)
# o correto é retornar uma ação, e não o estado final

# Duvida: Nos outros modelos, busca não informada e busca informada, o agente retorna uma sequencia de ações, de forma a não depender de suas percepções,
# já nesse modelo, como a sequencia de ação é indiferente, o que o agente deve retornar?
# Na teoria, os agentes recebem uma percepção e retornam uma ação, mas nesse caso, o que o agente deve retornar?

# talvez o ideal seja retornar uma ação valida, que não seja a mesma que o estado atual, e que seja a mais proxima do estado final. Algo como mover uma rainha para sua posição final