import unittest

from CalculadoraAbstrata import CalculadoraAbstrata


class TestCalculadora(unittest.TestCase):
    
    def testa_se_calcula_correto(self):
        calculadora = CalculadoraAbstrata()
        
        self.assertEqual(calculadora.calcula("2 mais 3"), 5)
        self.assertEqual(calculadora.calcula("2 menos 1"), 0)
        self.assertEqual(calculadora.calcula("2 vezes 3"), 6)
        self.assertEqual(calculadora.calcula("2 elevado a 3"), 8)
        self.assertEqual(calculadora.calcula("2 dividido por 2"), 1)
    
    def teste_se_nao_calcula(self):
        calculadora = CalculadoraAbstrata()
        
        with self.assertRaises(Exception):
            calculadora.calcula("2 sadasdasdasda 2")