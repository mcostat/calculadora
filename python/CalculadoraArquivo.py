from CalculadoraConsole import CalculadoraConsole


class CalculadoraArquivo(CalculadoraConsole):
    
    def main(self):
        super().main()
        
        with open("output-python.txt", "a+") as file:
            file.write(self.entrada + "\n" + str(self.resultado) + "\n")
        
        
if __name__ == "__main__":
    c = CalculadoraArquivo()
    c.main()
