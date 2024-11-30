from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, peso: float, pais_origen: str, impuestos: float, nombre: str) -> None:
        super().__init__(peso, pais_origen, impuestos)
        self._nombre = nombre
        self._ratones_comidos:int = 0

    def hacer_ruido(self) -> str:
        return "Tsss Tsss!"
    
    def comer_raton(self) -> None:
        if self._ratones_comidos < 20:
            self._ratones_comidos += 1
        else:
            raise ValueError("Demasiados Ratones!")

    def ratones_comidos(self) -> int:
        return self._ratones_comidos
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        if isinstance(value, str):
            self._nombre = value
        else:
            raise ValueError('Expected str')