
class CalculadoraAbstrata:
    def soma(self, a, b):
        return a + b

    def subtrai(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            return "Erro de calculo"

        return a/b

    def eleva(self, a, b):
        if b == 0 and a <= 0:
            return "Erro de calculo"

        return a ** b

    def vezes(self, a, b):
        return a * b

    operacoes = {"mais": soma, "menos": subtrai,
                 "dividido": divide, "elevado": eleva, "vezes": vezes}

    def calcula(self, entrada):
        lista = entrada.split(" ")

        if len(lista) < 3 or len(lista) > 4:
            return "Entrada invalida"
        
        try:
            num1 = float(lista[0])
            num2 = float(lista[-1])
            operacao = lista[1]

            return self.operacoes.get(operacao)(self, num1, num2)
        except Exception:
            return "Entrada invalida"
