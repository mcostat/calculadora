from CalculadoraAbstrata import CalculadoraAbstrata


class CalculadoraConsole(CalculadoraAbstrata):
    entrada = ""
    resultado = 0
    
    def main(self):
        print("Bem vindo a calculadora!")
        print("")
        print("Digite a operação")
        self.entrada = input("")
        self.resultado = self.calcula(self.entrada)
        print(self.resultado)


if __name__ == "__main__":
    c = CalculadoraConsole()
    c.main()
