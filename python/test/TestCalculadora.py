import unittest

from CalculadoraAbstrata import CalculadoraAbstrata


class TestCalculadora(unittest.TestCase):
    
    def testa_se_calcula_correto(self):
        calculadora = CalculadoraAbstrata()
        
        self.assertEqual(calculadora.calcula("2 mais 3"), 5)
        self.assertEqual(calculadora.calcula("2 menos 1"), 1)
        self.assertEqual(calculadora.calcula("2 vezes 3"), 6)
        self.assertEqual(calculadora.calcula("2 elevado a 3"), 8)
        self.assertEqual(calculadora.calcula("2 dividido por 2"), 1)
    
    def testa_se_nao_calcula(self):
        calculadora = CalculadoraAbstrata()
        
        self.assertEqual(calculadora.calcula("2 sadasdasdasda 2"), "Entrada invalida")
        self.assertEqual(calculadora.calcula("btrww qwe"), "Entrada invalida")
        self.assertEqual(calculadora.calcula("3 dividido por 0"), "Erro de calculo")
        self.assertEqual(calculadora.calcula("0 elevado a 0"), "Erro de calculo")
        
    def testa_varios_numeros(self):
        calculadora = CalculadoraAbstrata()
        
        for a in range(-100, 100):
            for b in range(-100, 100):
                if a != 0 and b != 0:
                    self.assertEqual(calculadora.calcula(f"{a} mais {b}"), a + b)
                    self.assertEqual(calculadora.calcula(f"{a} menos {b}"), a - b)
                    self.assertEqual(calculadora.calcula(f"{a} vezes {b}"), a * b)
                    self.assertEqual(calculadora.calcula(f"{a} dividido por {b}"), a / b)
                    #self.assertEqual(calculadora.calcula(f"{a} elevado a {b}"), a ** b)