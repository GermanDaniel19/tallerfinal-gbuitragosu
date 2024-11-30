import unittest
from boa_Constrictor import Boa_Constrictor

class TestBoa(unittest.TestCase):

    def test_hacer_ruido_should_return_ok(self):
        boa1 = Boa_Constrictor(peso = 12.5, pais_origen = "Colombia", impuestos = 116)
        self.assertIsInstance(boa1.hacer_ruido(),str)
        print(boa1.__dict__)

    def test_calcular_flete_should_return_float(self):
        boa2 = Boa_Constrictor(peso = 5.0, pais_origen = "Tailand", impuestos = 15.5)
        self.assertIsInstance(boa2.calcular_flete(),float)

    def test_comer_raton(self):
        boa3 = Boa_Constrictor(peso = 5.0, pais_origen = "Tailand", impuestos = 15.5)
        self.assertIsNone(boa3.comer_raton())