

class CalculadoraAbstrata:

    #operacoes = {"mais": self.soma()}

    def soma(self, a, b):
        return a+b

    def calcula(self, entrada):
        lista = entrada.split(" ")

        num1 = float(lista[0])
        num2 = float(lista[-1])
        operacao = lista[1]

        #return self.operacoes[operacao](num1, num2)

        if operacao == "mais":
            return num1 + num2
        elif operacao == "menos":
            return num1 - num2
        elif operacao == "vezes":
            return num1 * num2
        elif operacao == "dividido":
            return num1 / num2
        elif operacao == "elevado":
            return num1 ** num2
        else:
            raise Exception("operação invalida!")
        


if __name__ == "__main__":
    c = CalculadoraAbstrata()
    print("aaa")