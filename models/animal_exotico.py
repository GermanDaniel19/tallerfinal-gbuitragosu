from models.animal import Animal

class Animal_Exotico(Animal):

    def __init__(self, peso:float, pais_origen:str, impuestos:float) -> None:
        super().__init__(peso=peso)
        self._pais_origen = pais_origen
        self._impuestos = impuestos

    def calcular_flete(self) -> float:
        return round(float(self._peso * self._impuestos),2)
    
    #aqui deberia ir el metodo hacer_ruido?

    #getters and setters
    @property
    def pais_origen(self) -> str:
        return self._pais_origen
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        if isinstance(value, str):
            self._pais_origen = value
        else:
            raise ValueError('Expected str')
        
    @property
    def impuestos(self) -> float:
        return self._impuestos
    
    @impuestos.setter
    def impuestos(self, value:float) -> None:
        if isinstance(value, float):
            self._impuestos = value
        else:
            raise ValueError('Expected float')
        
    @property
    def data_animal(self) -> str:
        return str("Peso: " + str(self._peso) + ", pais origen: " + self._pais_origen + ", impuestos:" + str(self._impuestos))

# animal1 = Animal_Exotico(10.1,"colombia",112.1)
# print(str(animal1.data_animal))
# print(str(animal1.calcular_flete()))