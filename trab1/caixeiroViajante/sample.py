import sys
import concurrent.futures
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

if tipoAgente == TiposAgentes.TEMPERA_SIMULADA:
  estadoInicial = estadosAleatorios(1, QUANTIDADE_CIDADES)[0]
  cidades =  [(82, 3), (88, 16), (29, 55), (84, 86), (57, 29), (10, 85), (35, 30), (54, 10), (80, 52), (78, 60)]
  distancias = matrixDistancias(cidades)
  # cidades = cidadesAleatorias(QUANTIDADE_CIDADES)

  # print("Estado inicial: ", estadoInicial)
  # print("Cidades: ", cidades)
  # print("Distancias: ", distancias)

  driverTempera = Agente(TiposAgentes.TEMPERA_SIMULADA)
  driverTempera.configurar({ 
    'distancias': distancias, 
    'estadoInicial': estadoInicial[0],
    'logs': True
  })
  driverTempera.executar()

elif tipoAgente == TiposAgentes.ALGORITMO_GENETICO:
  QUANTIDADE_CIDADES = 64
  TAMANHO_POPULACAO = 128

  estadoInicial = estadosAleatorios(TAMANHO_POPULACAO, QUANTIDADE_CIDADES)
  # cidades =  [(82, 3), (88, 16), (29, 55), (84, 86), (57, 29), (10, 85), (35, 30), (54, 10), (80, 52), (78, 60)]
  
  cidades = [(78, 95), (45, 11), (91, 73), (38, 18), (73, 3), (20, 71), (43, 1), (2, 27), (62, 68), (74, 5), (15, 31), (18, 50), (90, 64), (66, 81), (56, 48), (38, 84), (41, 43), (52, 19), (56, 37), (99, 24), (87, 70), (47, 27), (64, 66), (53, 36), (51, 96), (2, 74), (96, 10), (24, 27), (73, 81), (22, 28), (83, 24), (73, 98), (84, 7), (54, 12), (76, 6), (1, 83), (33, 45), (8, 87), (94, 65), (18, 58), (52, 88), (40, 25), (82, 7), (52, 63), (87, 79), (79, 9), (50, 38), (66, 81), (96, 35), (2, 80), (58, 82), (87, 63), (54, 88), (41, 100), (37, 70), (88, 72), (76, 57), (7, 24), (99, 95), (24, 48), (17, 69), (77, 24), (35, 59), (44, 51)]
  
  # cidades = cidadesAleatorias(QUANTIDADE_CIDADES)
  # cidades = [(95, 13), (59, 69), (33, 97), (63, 17), (91, 50), (66, 45), (29, 100), (36, 78), (27, 58), (52, 18), (40, 88), (38, 64), (34, 62), (29, 91), (44, 21), (87, 14), (36, 1), (18, 5), (29, 38), (38, 51), (18, 5), (14, 92), (90, 75), (91, 65), (53, 46), (80, 58), (47, 21), (39, 62), (36, 16), (15, 45), (45, 37), (40, 47), (27, 20), (59, 31), (50, 94), (57, 11), (11, 39), (69, 70), (7, 55), (35, 30), (85, 34), (86, 11), (88, 29), (92, 81), (14, 50), (31, 16), (50, 26), (50, 82), (45, 36), (34, 80), (25, 42), (65, 2), (39, 54), (54, 64), (45, 71), (48, 85), (82, 11), (82, 63), (45, 83), (70, 17), (45, 11), (93, 45), (40, 89), (98, 18), (19, 70), (12, 56), (66, 28), (6, 78), (27, 88), (3, 90), (72, 75), (17, 72), (56, 90), (74, 93), (49, 39), (24, 31), (72, 5), (5, 94), (69, 49), (97, 20), (92, 91), (49, 92), (68, 96), (11, 55), (60, 13), (1, 49), (28, 8), (43, 76), (88, 3), (2, 98), (54, 19), (78, 44), (92, 56), (92, 72), (64, 46), (83, 27), (42, 31), (9, 79), (10, 51), (1, 81)]
  distancias = matrixDistancias(cidades)
  
  print(f"{QUANTIDADE_CIDADES} cidades, {TAMANHO_POPULACAO} indivíduos")
  print(cidades)
  print(distancias)

  # print("Estado inicial: ", estadoInicial)
  # print("Cidades: ", cidades)
  # print("Distancias: ", distancias)
  
  quantidadeTestes = 10
  
  def minhaTarefa(numero):
    print("Inicio ", numero)
    
    filename = f'teste_{numero}.txt'
    with open(filename, 'w') as arquivo:
      arquivo.write(f"{QUANTIDADE_CIDADES} cidades, {TAMANHO_POPULACAO} indivíduos\n")
      arquivo.write(f"{cidades}\n")
      arquivo.write(f"{distancias}\n")
              
      driverAG = Agente(TiposAgentes.ALGORITMO_GENETICO)
      driverAG.configurar({ 
        'qtdGeracoes': 5000, 
        'probMutacao': 0.05, 
        'distancias': distancias, 
        'estadoInicial': estadoInicial,
        'logs': True,
        'arquivo': arquivo
      })
      driverAG.executar()
      
      print("Fim intra", numero)
    print("Fim extra", numero)
      
  tarefas = [i for i in range(quantidadeTestes)]
  
  with concurrent.futures.ThreadPoolExecutor() as executor:
    resultados = [executor.submit(minhaTarefa, tarefa) for tarefa in tarefas]
    
  concurrent.futures.wait(resultados)