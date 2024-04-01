from enum import Enum
import algoritmoGenetico
import temperaSimulada

class TiposAgentes(Enum):
  TEMPERA_SIMULADA = 'TEMPERA_SIMULADA'
  ALGORITMO_GENETICO = 'ALGORITMO_GENETICO'

class Agente:
  def __init__(self, tipoAgente):
    if tipoAgente not in TiposAgentes:
      raise ValueError('Tipo de agente inválido')
    
    self.tipoAgente = tipoAgente

  def configurar(self, options):
    self.estado = None

    if self.tipoAgente == TiposAgentes.TEMPERA_SIMULADA:
      if 'distancias' not in options or 'estadoInicial' not in options:
        raise ValueError('Distâncias ou estado inicial não informados')
      self.distancias = options['distancias']
      self.estadoInicial = options['estadoInicial']
      self.logs = options['logs'] if 'logs' in options else False
    elif self.tipoAgente == TiposAgentes.ALGORITMO_GENETICO:
      if 'qtdGeracoes' not in options or 'probMutacao' not in options or 'distancias' not in options or 'estadoInicial' not in options:
        raise ValueError('Quantidade de gerações, probabilidade de mutação, distâncias ou estado inicial não informados')
      self.qtdGeracoes = options['qtdGeracoes']
      self.probMutacao = options['probMutacao']
      self.distancias = options['distancias']
      self.estadoInicial = options['estadoInicial']
      self.logs = options['logs'] if 'logs' in options else False

  def atualizarEstado(self, percepcao):
    self.estado = percepcao

  def executar(self):
    # fase atualização do estado
    self.atualizarEstado(self.estadoInicial)

    # fase formulação do problema
    if self.tipoAgente == TiposAgentes.TEMPERA_SIMULADA:
      problema = temperaSimulada.formularProblema(self.estado, self.distancias)
    elif self.tipoAgente == TiposAgentes.ALGORITMO_GENETICO:
      problema = algoritmoGenetico.formularProblema(self.estado, self.distancias, self.probMutacao)
    
    # fase busca da solução
    if self.tipoAgente == TiposAgentes.TEMPERA_SIMULADA:
      solucao = temperaSimulada.exec(problema, self.logs)
    elif self.tipoAgente == TiposAgentes.ALGORITMO_GENETICO:
      solucao = algoritmoGenetico.exec(problema, self.qtdGeracoes, self.logs)

    # fase execução da solução: Aqui o ideal seria o agente retornar cada ação individualmente que levará a solução encontrada. Para facilitar, estou retornando a solução completa
    return solucao