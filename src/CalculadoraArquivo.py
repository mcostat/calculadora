from CalculadoraConsole import CalculadoraConsole


class CalculadoraArquivo(CalculadoraConsole):
    
    def main(self):
        super().main()
        
        with open("output.txt", "a+") as file:
            file.write(self.entrada + "\n" + str(self.resultado))
        
        
if __name__ == "__main__":
    c = CalculadoraArquivo()
    c.main()
