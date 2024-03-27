#EXEMPLO 1:

# problema aspirador de pó IA
# O ambiente é um quarto com dois locais A e B. O agente aspirador de pó
# percebe se o local está limpo ou sujo e sua localização. O agente pode
# aspirar a sujeira, mover para a esquerda ou direita e desligar. O objetivo
# é limpar todos os locais.


# função AGENTE-DIRIGIDO-POR-TABELA(percepção) retorna uma ação
# variáveis estáticas: percepções, uma sequência, inicialmente vazia
# tabela, uma tabela de ações, indexada por sequências de percepções,
# inicialmente completamente especificada
# anexar percepção ao fim de percepções
# ação ← ACESSAR(percepções, tabela)
# retornar ação

# O agente é dirigido por uma tabela que mapeia sequências de percepções
# para ações. A tabela é inicialmente completamente especificada e é 
# atualizada conforme o agente interage com o ambiente.


percepcoes = ()
tabela = {
  ('SUJO', 'A'): 'ASPIRAR',
  ('SUJO', 'B'): 'ASPIRAR',
  ('LIMPO', 'A'): 'DIREITA',
  ('LIMPO', 'B'): 'ESQUERDA'
}

def agente_dirigido_por_tabela(percepcao):
  global percepcoes
  global tabela
  percepcoes += percepcao
  acao = tabela[tuple(percepcoes)]
  return acao

assert agente_dirigido_por_tabela(('SUJO', 'A')) == 'ASPIRAR'

# PROBLEMA: A tabela é se comporta como a função do agente, e deve conter
# todas as sequências de percepções possíveis. Isso é impraticável para
# ambientes complexos. A solução é usar uma função que mapeia percepções
# para ações. A tabela é uma forma de especificar essa função.