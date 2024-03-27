#  função	AGENTE-DE	RESOLUÇÃO-DE-PROBLEMAS-SIMPLES(percepção)	retorna	uma ação
#  persistente:	seq,	uma	sequência	de	ações,	inicialmente	vazia
#  estado,	alguma	descrição	do	estado	atual	do	mundo
#  objetivo,	um	objetivo,	inicialmente	nulo
#  problema,	uma	formulação	de	problema
#  estado	←	ATUALIZAR-ESTADO(estado,	percepção)
#  se	seq	está	vazia	então	faça
#  objetivo	←	FORMULAR-OBJETIVO(estado)
#  problema	←	FORMULAR-PROBLEMA(estado,	objetivo)
#  seq	←	BUSCA(problema)
#  se	seq	=	falhar	então	retorne	uma	ação	nula
#  ação	←	PRIMEIRO(seq)
#  seq	←	RESTO(seq)
#  retornar	ação


# seq = []

# def agente_de_resolucao_de_problemas_simples(percepcao):
#   estado = atualizar_estado(estado, percepcao)
#   if not seq:
#     objetivo = formular_objetivo(estado)
#     problema = formular_problema(estado, objetivo)
#     seq = busca(problema)
#   if seq == 'falhar':
#     return None
#   acao = seq[0]
#   seq = seq[1:]
#   return acao


# nos modelos reativos, existe uma tabela de regras, que mapeia um determinado estado para uma ação. Se estado X, então ação Y

# nos modelos de resolução de problemas, existe um modelo de transição, que a partir de um determinado estado e ação, define o prox estado
# nesse modelo, é definido um problema e um objetivo, resolve, e define uma sequencia de ações que chegam nesse objetivo
# nesse modelo, a partir da primeira persepção, o agente define toda a sequencia de ações que ele deve tomar para chegar no objetivo, independente das novas persepções que ele receba, pois ele "já sabe" tudo que vai acontecer
#  Quando	todos	os	custos	de	passos	forem	iguais,	a	busca	em	largura	será	ótima	porque
#  sempre	expande	o	nó	mais	raso	não	expandido

# EXEMPLO: O	quebra-cabeça	de	oito	peças,	consiste	de	um	tabuleiro
#  3	×	3	com	oito	peças	numeradas	e	um	quadrado	vazio.	Uma	peça	adjacente	ao	quadrado	vazio
#  pode	deslizar	para	esse	quadrado.	O	objetivo	é	alcançar	um	estado	objetivo	especificado
# A	formulação-padrão	é	dada	por:
#  •		Estados:	Uma	descrição	de	estado	especifica	a	posição	de	cada	uma	das	oito	peças	e	do
#  quadrado	vazio	em	um	dos	nove	quadrados.
#  •		Estado	inicial:	Qualquer	estado	pode	ser	designado	como	o	estado	inicial.	Observe	que
#  qualquer	objetivo	específico	pode	ser	alcançado	a	partir	de	exatamente	metade	dos
# estados	iniciais	possíveis	(Exercício	3.4).
#  •		Ações:	A	formulação	mais	simples	define	as	ações	como	movimentos	do	quadrado	vazio
#  Esquerda,	Direita,	Para	Cima	ou	Para	Baixo.	Pode	haver	subconjuntos	diferentes	desses,
#  dependendo	de	onde	estiver	o	quadrado	vazio.
#  •		Modelo	de	transição:	Dado	um	estado	e	ação,	ele	devolve	o	estado	resultante;	por
#  exemplo,	se	aplicarmos	Esquerda	para	o	estado	inicial	na	Figura	3.4,	o	estado	resultante
#  terá	comutado	o	5	e	o	branco.
#  •		Teste	de	objetivo:	Verifica	se	o	estado	corresponde	à	configuração	de	estado	objetivo
#  mostrada	na	Figura	3.4	(são	possíveis	outras	configurações	de	objetivos).
#  •		Custo	de	caminho:	Cada	passo	custa	1	e,assim,	o	custo	do	caminho	é	o	número	de
#  passos	do	caminho.

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
  
  def heuristica(estado):
      # Usar a distância de Manhattan
      # A distância de Manhattan é a soma da distância das peças até a posição final
      def get_index(elemento, objetivo):
          for i, linha in enumerate(objetivo):
              for j, valor in enumerate(linha):
                  if valor == elemento:
                      return i, j

      objetivo = [[0,1,2],[3,4,5],[6,7,8]]
      distancia = 0

      for i, linha in enumerate(estado):
          for j, elemento in enumerate(linha):
              if elemento != 0:
                  objetivo_i, objetivo_j = get_index(elemento, objetivo)
                  distancia += abs(i - objetivo_i) + abs(j - objetivo_j)

      return distancia
  
  return {
    'estadoInicial': estado,
    'testeDeObjetivo': testeDeObjetivo,
    'acoes': acoes,
    'resultado': resultado,
    'custoDoPasso': custoDoPasso,
    'heuristica': heuristica
  }

def busca_a_estrela(problema):
  estadoInicial, testeDeObjetivo, acoes, resultado, custoDoPasso, heuristica = problema['estadoInicial'], problema['testeDeObjetivo'], problema['acoes'], problema['resultado'], problema['custoDoPasso'], problema['heuristica']

  def solucao(no):
    if no['pai'] == None:
      return []
    return solucao(no['pai']) + [no['acao']]

  no = {
    'estado': estadoInicial,
    'pai': None,
    'acao': None,
    'custoDeCaminho': 0,
    'heuristica': heuristica(estadoInicial)
  }
  if testeDeObjetivo(no['estado']):
    return solucao(no)
  borda = [no]
  explorado = []

  # print("estadoInicial", estadoInicial)

  while True:
    print(len(explorado))
    if not borda:
      return 'falha'
    
    borda.sort(key=lambda x: x['custoDeCaminho'] + x['heuristica'])  # Ordena a borda pelo custo total

    no = borda.pop(0)

    if(testeDeObjetivo(no['estado'])):
      return solucao(no)
    
    explorado.append(no['estado'])

    for acao in acoes(no['estado']):
      print(no['estado'], no['custoDeCaminho'], no['heuristica'])
      filho = {
        'estado': resultado(no['estado'], acao),
        'pai': no,
        'acao': acao,
        'custoDeCaminho': no['custoDeCaminho'] + custoDoPasso(no['estado'], acao),
        'heuristica': heuristica(resultado(no['estado'], acao))
      }        
      if filho['estado'] not in explorado and filho['estado'] not in [x['estado'] for x in borda]:
        borda.append(filho)
      elif(filho['estado'] in [x['estado'] for x in borda]): 
        for i2, no2 in enumerate(borda):
          if no2['estado'] == filho['estado']:
            if no2['custoDeCaminho'] + no2['heuristica'] > filho['custoDeCaminho'] + filho['heuristica']:
              borda[i2] = filho

def busca(problema):
  return busca_a_estrela(problema)
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

# com heuristica: 127 estados
# sem heuristica: 3719 estados