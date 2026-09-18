class CalculadoraPotencias:
    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return self.numero ** 2

    def calcular_cubo(self):
        return self.numero ** 3

    def mostrar_resultados(self):
        print("Número:", self.numero)
        print("Cuadrado:", self.calcular_cuadrado())
        print("Cubo:", self.calcular_cubo())


numero = float(input("Ingrese un número: "))

calculadora = CalculadoraPotencias(numero)
calculadora.mostrar_resultados()
