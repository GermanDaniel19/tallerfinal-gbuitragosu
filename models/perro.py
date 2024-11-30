from models.animal import Animal

class Perro(Animal):
    def __init__(self, peso: float, nombre: str , raza: str) -> None:
        super().__init__(peso)
        self._nombre = nombre
        self._raza = raza

    def hacer_ruido(self) -> str:
        return "Waua Wuau !!"
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')
        
    @property
    def raza(self) -> str:
        return self._raza
    
    @raza.setter
    def raza(self, value:str) -> None:
        if isinstance(value, str):
            self._raza = value
        else:
            raise ValueError('Expected str')