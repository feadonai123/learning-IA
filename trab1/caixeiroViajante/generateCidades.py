from seed import cidadesAleatorias, matrixDistancias, estadosAleatorios
from main import Agente, TiposAgentes

optionsQtdCidades = [4, 8, 16, 32, 64]
optionsQtdPopulacao = [4, 8, 16, 32, 64]
optionsQtdsGeracoes = [100, 1000]
optionsProbMutacao = [0.1, 0.2, 0.3, 0.4, 0.5]

qtdTestesPorConfig = 5

# qtdCidades = 10
# qtdPopulacao = 5
# qtdGeracoes = 100
# probMutacao = 0.2
# i = 0

# cidades = cidadesAleatorias(qtdCidades)
# distancias = matrixDistancias(cidades)
# estadoInicial = estadosAleatorios(qtdPopulacao, qtdCidades)
# filename = f"AG_{qtdCidades}_{qtdPopulacao}_{qtdGeracoes}_{probMutacao}_{i}.txt"

# with open(filename, 'w') as arquivo:
#   arquivo.write(f"{qtdCidades} cidades, {qtdPopulacao} indivíduos\n")
#   arquivo.write(f"{cidades}\n")
#   arquivo.write(f"{distancias}\n")

#   driverAG = Agente(TiposAgentes.ALGORITMO_GENETICO)
#   driverAG.configurar({ 
#     'qtdGeracoes': qtdGeracoes, 
#     'probMutacao': probMutacao,
#     'distancias': distancias, 
#     'estadoInicial': estadoInicial,
#     'logs': True,
#     'arquivo': arquivo
#   })
#   driverAG.executar() 

for qtdCidades in optionsQtdCidades:
  cidades = cidadesAleatorias(qtdCidades)
  distancias = matrixDistancias(cidades)
  for qtdPopulacao in optionsQtdPopulacao:
    estadoInicial = estadosAleatorios(qtdPopulacao, qtdCidades)
    for qtdGeracoes in optionsQtdsGeracoes:
      for probMutacao in optionsProbMutacao:
        for i in range(qtdTestesPorConfig):
          filename = f"AG_{qtdCidades}_{qtdPopulacao}_{qtdGeracoes}_{probMutacao}_{i}.txt"
          with open(filename, 'w') as arquivo:
            arquivo.write(f"{qtdCidades} cidades, {qtdPopulacao} indivíduos\n")
            arquivo.write(f"{cidades}\n")
            arquivo.write(f"{distancias}\n")
  
            driverAG = Agente(TiposAgentes.ALGORITMO_GENETICO)
            driverAG.configurar({ 
              'qtdGeracoes': qtdGeracoes, 
              'probMutacao': probMutacao,
              'distancias': distancias, 
              'estadoInicial': estadoInicial,
              'logs': True,
              'arquivo': arquivo
            })
            driverAG.executar()     
      