from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def comer(self, kilos:float) -> None:
        pass

    def obtener_kilos_comidos(self) -> float:
        pass