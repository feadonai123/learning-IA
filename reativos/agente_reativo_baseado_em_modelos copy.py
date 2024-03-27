# função AGENTE-REATIVO-BASEADO-EM-MODELOS (percepção) retorna uma ação
# persistente: estado, a concepção do agente do estado atual do mundo
# modelo, uma descrição de como o próximo estado depende do estado atual e da
# ação
# regras, um conjunto de regras condição-ação
# ação, a ação mais recente, inicialmente nenhuma
# estado ← ATUALIZAR-ESTADO (estado, ação, percepção, modelo)
# regra ← REGRA-CORRESPONDENTE (estado, regras)
# ação ← regra, AÇÃO
# retornar ação


# para o mundo do aspirador de pó
# o estado é a posição do agente e a situação dos locais
# exemplo: [A, SUJO, LIMPO]
# as percepções são a posição do agente e a situação do local
# exemplo: [A, SUJO]
# o modelo é a descrição de como o próximo estado depende do estado atual e da ação
# exemplo: se a ação é ASPIRAR e o estado é [A, SUJO, LIMPO] então o próximo estado é [A, LIMPO, LIMPO]
# as regras são condição-ação
# exemplo: se situação = Sujo então retorna Aspirar


acao = None
estado = ('A', 'SUJO', 'SUJO')
regras = {
  ('A', 'SUJO'): 'ASPIRAR',
  ('A', 'LIMPO'): 'DIREITA',
  ('B', 'SUJO'): 'ASPIRAR',
  ('B', 'LIMPO'): 'DIREITA'
}
modelo = {
  ('ASPIRAR', ('A', 'SUJO', 'SUJO')): ('A', 'LIMPO', 'SUJO'),
  ('ASPIRAR', ('B', 'SUJO', 'SUJO')): ('B', 'LIMPO', 'SUJO'),
  ('DIREITA', ('A', 'SUJO', 'SUJO')): ('B', 'SUJO', 'SUJO'),
  ('DIREITA', ('B', 'SUJO', 'SUJO')): ('A', 'SUJO', 'SUJO'),
  ('ESQUERDA', ('A', 'SUJO', 'SUJO')): ('A', 'SUJO', 'SUJO'),
  ('ESQUERDA', ('B', 'SUJO', 'SUJO')): ('B', 'SUJO', 'SUJO'),
}

def atualizar_estado(estado, acao, percepcao, modelo):
  return modelo[(acao, estado)]


def agente_reativo_baseado_em_modelos(percepcao):
  global estado
  global modelo
  global regras
  global acao
  estado = atualizar_estado(estado, acao, percepcao, modelo)
  regra = regra_correspondente(estado, regras)
  acao = regra['acao']
  return acao


# ideia
# 1. inicialmente, o agente tem conhecimento total do ambiente
# 2. o agente mantem o estado atual do mundo
# 3. ao receber uma percepção, ele atualiza o seu estado atual com base no seu ultimo estado, na sua ultima ação e na percepção recebida (para isso ele usa um modelo)
# 4. após atualizar o estado do mundo, ele busca a regra que deve ser aplicada para o estado atual
# 5. por ultimo ele aplica a ação que a regra indica

# a escolha da ação é REATIVA. Não há planejamento (busca por um objetivo), apenas um mapeamento direto da percepção para a ação. Se o estado é X, então a ação é Y.