#importando a classe, da forma mais usual
import matplotlib.pyplot as plt
#definindo variáveis que vamos usar nos exemplos
x = [1, 2, 3]
y = [10, 20, 30]
y2 = [15, 10, 40]
y3 = [20, 10, 35]
yBar = [3, 10, 7, 5, 3, 4.5, 6, 8.1]
z = [i * 1.5 for i in yBar]
xBar = range(len(yBar))
azul = "blue"
verde = "green"
preto = "black"
# Desenhando uma linha:
def plota_linha_1():
  plt.plot(x, y)
  plt.show()

print("plota_linha_1")
plota_linha_1()