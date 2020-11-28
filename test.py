from SPJRUD.SPJRUD import SPJRUD
from SPJRUD.Select import Select
from SPJRUD.Join import Join
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Attribute import Attribute
from Representation.Relation import Relation

from Representation.Node import Node

a = Attribute("Attribute", 'TEXT')
abis = Attribute("Attribute2", 'TEXT')
atris = Attribute("Attribute3", 'TEXT')

b = Constante("Nicolas")
c = Equal(a, Constante("Constante"))
d = Relation("Relation", [a, abis, atris])
e = Equal(abis,atris)

ni = Select(c,d).to_SQL()
co = Select(e,d).to_SQL()
# for z in c:
#     print(z)

print(ni)
print(co)