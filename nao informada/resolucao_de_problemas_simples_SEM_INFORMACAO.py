# ao adicionar INFORMAÇÃO, o que estamos fazendo é durante o processo de busca, expandir o nó com maiores chances de ser o nó correto. Para isso, usamos uma função de heuristica que nos diz qual nó expandir. A heuristica é uma função que estima o custo de se chegar no objetivo a partir de um nó
# OBS, é importante considerar tanto a heuristica quando o custo até o momento (g(n)). Se considerarmos apenas h(n), será um modelo guloso, que pode gerar soluções não ótimas

seq = []
estado = [[4,3,2],[1,5,6],[7,8,0]]

def atualizar_estado(estado, percepcao):
  return percepcao

def formular_objetivo(estado):
  return [[0,1,2],[3,4,5],[6,7,8]]

def formular_problema(estado, objetivo):
  def testeDeObjetivo(estado):
      return estado == objetivo
  
  def acoes(estado):
    def get_index_zero(estado):
      for i, linha in enumerate(estado):
          for j, elemento in enumerate(linha):
              if elemento == 0:
                  return i, j
              
    i, j = get_index_zero(estado)
    acoes = ['esquerda', 'cima', 'direita', 'baixo']
    if(i == 0):
      acoes.remove('cima')
    if(i == 2):
      acoes.remove('baixo')
    if(j == 0):
      acoes.remove('esquerda')
    if(j == 2):
      acoes.remove('direita')

    return acoes

  def resultado(estado, acao):
    def get_index_zero(estado):
      for i, linha in enumerate(estado):
          for j, elemento in enumerate(linha):
              if elemento == 0:
                  return i, j
              
    i, j = get_index_zero(estado)

    novo_estado = [linha.copy() for linha in estado]
    if acao == 'esquerda':
      novo_estado[i][j] = estado[i][j-1]
      novo_estado[i][j-1] = 0
    if acao == 'cima':
      novo_estado[i][j] = estado[i-1][j]
      novo_estado[i-1][j] = 0
    if acao == 'direita':
      novo_estado[i][j] = estado[i][j+1]
      novo_estado[i][j+1] = 0
    if acao == 'baixo':
      novo_estado[i][j] = estado[i+1][j]
      novo_estado[i+1][j] = 0

    return novo_estado
  
  def custoDoPasso(estado, acao):
    return 1
  
  return {
    'estadoInicial': estado,
    'testeDeObjetivo': testeDeObjetivo,
    'acoes': acoes,
    'resultado': resultado,
    'custoDoPasso': custoDoPasso
  }

def busca_em_largura(problema):
  estadoInicial, testeDeObjetivo, acoes, resultado, custoDoPasso = problema['estadoInicial'], problema['testeDeObjetivo'], problema['acoes'], problema['resultado'], problema['custoDoPasso']

  def solucao(no):
    if no['pai'] == None:
      return []
    return solucao(no['pai']) + [no['acao']]

  no = {
    'estado': estadoInicial,
    'pai': None,
    'acao': None,
    'custoDeCaminho': 0
  }
  if testeDeObjetivo(no['estado']):
    return solucao(no)
  borda = [no]
  explorado = []

  # print("estadoInicial", estadoInicial)

  while True:
    # print(len(explorado))
    if not borda:
      return 'falha'
    no = borda.pop(0)
    explorado.append(no['estado'])

    for acao in acoes(no['estado']):
      filho = {
        'estado': resultado(no['estado'], acao),
        'pai': no,
        'acao': acao,
        'custoDeCaminho': no['custoDeCaminho'] + custoDoPasso(no['estado'], acao)
      }
      if filho['estado'] not in explorado and filho['estado'] not in [x['estado'] for x in borda]:
        if testeDeObjetivo(filho['estado']):
          return solucao(filho)
        borda.append(filho)

def busca(problema):
  return busca_em_largura(problema)
  # dado um estado inicial e um objetivo, retorna uma sequencia de ações que chegam no objetivo
  # nessa etapa usariamos um algoritmo de busca, como busca em largura, busca em profundidade, busca A*, etc

def quebra_cabeca_8_pecas_agente_de_resolucao_de_problemas_simples(percepcao):
  global estado
  global seq
  estado = atualizar_estado(estado, percepcao)
  if not seq:
    objetivo = formular_objetivo(estado)
    problema = formular_problema(estado, objetivo)
    seq = busca(problema)
    print("seq", seq)
  if seq == 'falha':
    return None
  acao = seq[0]
  seq = seq[1:]
  return acao

for acao in  ['esquerda', 'cima', 'direita', 'direita', 'baixo', 'esquerda', 'cima', 'esquerda', 'baixo', 'direita', 'direita', 'cima', 'esquerda', 'esquerda']:
  assert quebra_cabeca_8_pecas_agente_de_resolucao_de_problemas_simples([[1, 2, 3], [4, 0, 5], [6, 7, 8]]) == acao
