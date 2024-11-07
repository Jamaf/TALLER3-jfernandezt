import unittest
from boa import Boa

class TestBoa(unittest.TestCase):
    
    def setUp(self):
        self.my_boa = Boa('Boby', 10.0, 6, 'Colombia', 16.5)        
            
    def test_hacer_sonido(self):
        self.assertEqual(self.my_boa.hacer_sonido(), '¡Tsss!.')

    def test_calcular_flete(self):
        self.assertEqual(self.my_boa.calcular_flete(), 165)

    def test_agregar_raton(self):
        self.my_boa.agregar_raton(3)
        self.my_boa.agregar_raton(3)
        self.assertEqual(self.my_boa.ratones_comidos, 6)
        self.my_boa.agregar_raton(4)
        self.assertEqual(self.my_boa.ratones_comidos, 10)
        with self.assertRaises(ValueError):
            self.my_boa.agregar_raton(1)


if __name__ == '__main__':
    unittest.main()    