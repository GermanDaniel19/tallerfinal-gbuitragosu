from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor

class Guarderia():

    def __init__(self) -> None:
        huron1 = Huron(13.4,"Australia",563.4)
        huron2 = Huron(5.0,"Irlanda",563.4)
        boa1 = Boa_Constrictor(11.3,"Japon",564.15,"boa11")
        boa2 = Boa_Constrictor(11.3,"Peru",36.85, "boa2")

        self.boas: list = [boa1,boa2]
        self.hurones: list = [huron1,huron2]

    def alimentar_boa(self,value: str):

        boa_alimentar: Boa_Constrictor = None

        
        for boa in self.boas:
            if boa._nombre == value:
                boa_alimentar = boa
                print(boa_alimentar.__dict__)
                break
        
        if boa_alimentar is None:
            print("Esta boa no existe !")
        else:
            try:
                boa.comer_raton()
            except Exception as e:
                return print("La boa está llena")
            else:
                return print("Éxito")
        
    
