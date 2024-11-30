from models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):
    
    def __init__(self, peso: float, pais_origen: str, impuestos: float) -> None:
        super().__init__(peso, pais_origen, impuestos)

    def hacer_ruido(self) -> str:
        return "Eek Eek !!"
    

