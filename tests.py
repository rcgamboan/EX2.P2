import unittest
import eval
import mostrar

# para ejecutar las pruebas y calcular la cobertura ejecutar el siguiente comando:
# coverage run -m unittest tests.py
# Luego se puede acceder al reporte de la cobertura con el comando
# coverage report
class Tests(unittest.TestCase):

    def test_eval_pre_true(self):
        expresion = "| & => true true false true"
        self.assertEqual(eval.evalPrefix(expresion.split()) , "true")
    
    def test_eval_pre_false(self):
        expresion = "& ˆ false false"
        self.assertEqual(eval.evalPrefix(expresion.split()) , "false")
    
    def test_eval_post_true(self):
        expresion = "false true => true | true false & |"
        self.assertEqual(eval.evalPostfix(expresion.split()) , "true")

    def test_eval_post_false(self):
        expresion = "true false => false | true false ˆ | &"
        self.assertEqual(eval.evalPostfix(expresion.split()) , "false")
    
    def test_mostrar_pre(self):
        expresion = "| & => true true false true"
        self.assertEqual(mostrar.preFijoaInfijo(expresion.split()),"(true=>true) & false | true")
    
    def test_mostrar_post(self):
        expresion = "true false => false | true false ˆ | &"
        self.assertEqual(mostrar.postFijoaInfijo(expresion.split()), "(true=>false) | false & true | ˆfalse")


if __name__ == '__main__':
    unittest.main()