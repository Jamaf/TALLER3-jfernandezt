from huron import Huron
from boa import Boa

class Guarderia:
    def __init__(self, boa1:Boa, boa2:Boa, huron1:Huron, huron2:Huron):
        self.boa1 = boa1
        self.boa2 = boa2
        self.huron1 = huron1
        self.huron2 = huron2

    def alimentar_boa(self, boa:Boa) -> str:
        resultado:str
        try:
            if boa is None:
                raise ValueError('Esta Boa no existe!')
            boa.agregar_raton(1)
            resultado = 'Éxito'
        except ValueError as err:
            if str(err) == 'Demasiados Ratones!':
                resultado = 'La boa está llena'
            else:
                resultado = str(err)
        return resultado

