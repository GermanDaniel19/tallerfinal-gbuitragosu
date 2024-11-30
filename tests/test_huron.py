import unittest
from huron import Huron

class TestHuron(unittest.TestCase):

    def test_hacer_ruido_should_return_ok(self):
        huron1 = Huron(peso = 5.0, pais_origen = "Tailand", impuestos = 15.5)
        self.assertEqual(huron1.hacer_ruido(),"¡Eek Eek!")
        print(huron1.__dict__)

    def test_calcular_flete_should_return_float(self):
        huron2 = Huron(peso = 5.0, pais_origen = "Tailand", impuestos = 15.5)
        self.assertIsInstance(huron2.calcular_flete(),float)

        
