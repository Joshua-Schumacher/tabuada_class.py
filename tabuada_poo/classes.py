class Tabuada:
    def __init__(self,numero):
        self.valor = numero
        self._resultado = 0 

    def soma(self):
            for i in range(1,10+1):
                self._resultado = self.valor + i
                print(f"{self.valor} + {i} = {self._resultado}")

    def subtracao(self):       
            for i in range(1,10+1):
                self._resultado = self.valor - i
                print(f"{self.valor} - {i} = {self._resultado}")

    def multiplicacao(self):
         for i in range(1,10+1):
              self._resultado = self.valor * i
              print(f"{self.valor} * {i} = {self._resultado}")
    
    def divisão(self):
         for i in range(1,10+1):
              self._resultado = self.valor / i
              print(f"{self.valor} / {i} = {self._resultado}")


tabuada_2 = Tabuada(2)

tabuada_2.soma()
print("---"*15)
tabuada_2.subtracao()
print("---"*15)
tabuada_2.multiplicacao()
print("---"*15)
tabuada_2.divisão()
