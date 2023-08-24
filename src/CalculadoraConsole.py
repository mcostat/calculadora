from CalculadoraAbstrata import CalculadoraAbstrata


class CalculadoraConsole(CalculadoraAbstrata):

    def main(self):
        print("Bem vindo a calculadora!")
        print("")
        print("Digite a operação")
        entrada = input()
        resultado = self.calcula(entrada)
        print(resultado)


if __name__ == "__main__":
    c = CalculadoraConsole()
    c.main()
