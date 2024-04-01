import sys
from seed import estadosAleatorios, cidadesAleatorias, matrixDistancias
from main import Agente, TiposAgentes

# Exemplo comando:
# python sample.py AG > out/AG.txt
# python sample.py TEMPERA > out/TEMPERA.txt

args = sys.argv

if len(sys.argv) < 2:
  print("Erro:  Tipo de agente não informado")
  print("Uso:   python sample.py <TEMPERA | AG>")
  sys.exit(1)

tipoAgente = None
if args[1] == 'TEMPERA':
  tipoAgente = TiposAgentes.TEMPERA_SIMULADA
elif args[1] == 'AG':
  tipoAgente = TiposAgentes.ALGORITMO_GENETICO

if tipoAgente is None:
  print("Erro:  Tipo de agente inválido")
  print("Uso:   python sample.py <TEMPERA | AG>")
  sys.exit(1)

QUANTIDADE_CIDADES = 10
TAMANHO_POPULACAO = 50

estadoInicial = estadosAleatorios(TAMANHO_POPULACAO, QUANTIDADE_CIDADES)
# cidades = cidadesAleatorias(QUANTIDADE_CIDADES)
cidades =  [(82, 3), (88, 16), (29, 55), (84, 86), (57, 29), (10, 85), (35, 30), (54, 10), (80, 52), (78, 60)]
distancias = matrixDistancias(cidades)

print("Estado inicial: ", estadoInicial)
print("Cidades: ", cidades)
print("Distancias: ", distancias)

if tipoAgente == TiposAgentes.TEMPERA_SIMULADA:
  driverTempera = Agente(TiposAgentes.TEMPERA_SIMULADA)
  driverTempera.configurar({ 
    'distancias': distancias, 
    'estadoInicial': estadoInicial[0],
    'logs': True
  })
  driverTempera.executar()

elif tipoAgente == TiposAgentes.ALGORITMO_GENETICO:
  driverAG = Agente(TiposAgentes.ALGORITMO_GENETICO)
  driverAG.configurar({ 
    'qtdGeracoes': 1000, 
    'probMutacao': 0.2, 
    'distancias': distancias, 
    'estadoInicial': estadoInicial,
    'logs': True
  })
  driverAG.executar()