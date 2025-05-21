from classes import Tabuada

valor = int(input("Informe um valor para calcular: "))

tabuada_2 = Tabuada(valor)
tabuada_2.soma()
print("---"*15)
tabuada_2.subtracao()
print("---"*15)
tabuada_2.multiplicacao()
print("---"*15)
tabuada_2.divisão()
