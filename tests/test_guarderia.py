import unittest
from huron import Huron
from boa import Boa
from guarderia import Guarderia

class TestGuarderia(unittest.TestCase):

    def test_alimentar_boa(self):
        my_boa = Boa('Boby', 10.0, 6, 'Colombia', 16.5)        
        my_boa2 = Boa('Boby 2', 20.0, 12, 'Colombia', 33.0)        
        my_huron = Huron('Buck', 3.5, 4, 'Brazil', 20.0)     
        my_huron2 = Huron('Buck 2', 7.0, 8, 'Brazil', 40.0)     

        my_guarderia = Guarderia(my_boa, my_boa2, my_huron, my_huron2)

        #se pone la boa al limite de ratones la boa2
        for i in range(20):
            my_guarderia.alimentar_boa(my_boa2)

        #validamos que efectivamente se haya comido los 10
        self.assertEqual(my_boa2.ratones_comidos, 20)

        resultado = my_guarderia.alimentar_boa(my_boa2)
        self.assertEqual(resultado, 'La boa está llena')

        resultado = my_guarderia.alimentar_boa(None)
        self.assertEqual(resultado, 'Esta Boa no existe!')

        # with self.assertRaises(ValueError):
        #     my_guarderia.alimentar_boa(my_boa2)   
        #     my_guarderia.alimentar_boa(my_boa2)   

        # with self.assertRaises(ValueError):
        #     my_guarderia.alimentar_boa(None)                   
