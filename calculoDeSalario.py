class Calculadora:
    def __init__(self):
        self.salarioPorHora = float(input("Quantos reais você ganha por hora?\n"))
        self.horasTrabalhadas = float(input("Quantas horas foram trabalhadas no mês?\n"))

    def calculoDoSalarioNoMes (self):
        salarioNoMes = self.salarioPorHora * self.horasTrabalhadas
        print("O salário total no mês foi de R$", salarioNoMes)
