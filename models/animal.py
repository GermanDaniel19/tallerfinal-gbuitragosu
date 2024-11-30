from models.ianimal import iAnimal
from abc import abstractmethod

class Animal(iAnimal):

    def __init__(self, peso:float) -> None:
        self._peso = peso
    
    #setters and getters
    @property
    def peso(self) -> float:
        return self._peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        if isinstance(value, float):
            self._peso = value
        else:
            raise ValueError('Expected float')
        

        if isinstance(value, int):
            self._edad = value
        else:
            raise ValueError('Expected int')