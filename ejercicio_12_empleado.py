class Empleado:
    def __init__(self, horas_trabajadas, valor_hora):
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = 0.125

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_retencion(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * self.porcentaje_retencion

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = self.calcular_retencion()
        return salario_bruto - retencion

    def mostrar_resultados(self):
        bruto = self.calcular_salario_bruto()
        retencion = self.calcular_retencion()
        neto = self.calcular_salario_neto()

        print("SALARIO BRUTO:", bruto)
        print("RETENCIÓN EN LA FUENTE:", retencion)
        print("SALARIO NETO:", neto)


horas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de la hora: "))

empleado = Empleado(horas, valor_hora)
empleado.mostrar_resultados()
