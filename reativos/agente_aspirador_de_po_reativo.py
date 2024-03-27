# função AGENTE-ASPIRADOR-DE-PÓ-REATIVO ([posição, situação]) retorna uma ação*
# se situação = Sujo então retorna Aspirar
# senão se posição = A então retorna Direita
# senão se posição = B então retorna Esquerda



def agente_aspirador_de_po_reativo(percepcao):
  posicao, situacao = percepcao
  if situacao == 'SUJO':
    return 'ASPIRAR'
  elif posicao == 'A':
    return 'DIREITA'
  elif posicao == 'B':
    return 'ESQUERDA'
  
assert agente_aspirador_de_po_reativo(('A', 'SUJO')) == 'ASPIRAR'
assert agente_aspirador_de_po_reativo(('A', 'LIMPO')) == 'DIREITA'
assert agente_aspirador_de_po_reativo(('B', 'SUJO')) == 'ASPIRAR'
assert agente_aspirador_de_po_reativo(('B', 'LIMPO')) == 'ESQUERDA'