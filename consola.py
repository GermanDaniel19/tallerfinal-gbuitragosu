from models.huron import Huron
from models.boa_Constrictor import Boa_Constrictor
from models.guarderia import Guarderia
from models.perro import Perro
from models.gato import Gato



"""
Ejemplo
"""

print("======huron=======")
huron1 = Huron(5.2,"guinea ecuatorial",115.8)
print(huron1.data_animal)
print("flete: " + str(huron1.calcular_flete()))
print(huron1.hacer_ruido())

print("======boa constrictor=======")
boa = Boa_Constrictor(15.4,"Amazonas",20.4,"boanacleta")
print(boa.data_animal)
print("flete: " + str(boa.calcular_flete()))
print(boa.hacer_ruido())
print("ratones merendiados: " + str(boa.ratones_comidos()))
boa.comer_raton()
print("ratones merendiados: " + str(boa.ratones_comidos()))

print("======Perro=======")
perro = Perro(5.5,"Budapest","firulai")
print(perro.hacer_ruido())

print("======Gato=======")
gato = Gato(15.4,"Bogota","gatubelo")
print(gato.hacer_ruido())


