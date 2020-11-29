from SPJRUD.SPJRUD import SPJRUD
from SPJRUD.Select import Select
from SPJRUD.Join import Join
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Attribute import Attribute
from Representation.Relation import Relation

from Representation.Node import Node


#---EQUAL---#
# a = Constante("Constante")
# b = Attribute("Attribute", 'TEXT')

# res = Equal(a,b)
"""
Exception: Le premier parametre doit etre du type 'Attribute'
"""

#res = Equal(b, "NotAttributeandNotConsant")
"""
Exception: Le deuxieme parametre doit etre du type 'Attribute' ou 'Constante'
"""

# res = Equal(b,a)
# for r in res.return_NameList():
#     print(r)
"""
Attribute
Constante
"""

# res = Equal(b,b)
# for r in res.return_NameList():
#     print(r)
"""
Attribute
Attribute
"""



#---SELECT---#
a = Attribute("Attribute", 'TEXT')
b = Attribute("Attribute2", 'TEXT')
c = Attribute("Attribute3", 'TEXT')
d = Attribute("Attribute4", 'TEXT')

e = Relation("Relation", [a, b, c])
z = Relation("Relation", [a, b, c])

f = Constante("Constante")

g = Equal(a, f)
h = Equal(b, c)
# i = Equal(d, f)
"""
Exception: Cet attribut n'existe pas dans la relation
"""

res1 = Select(g, e)
res2 = Select(h, z)
# res3 = Select(i, e)

res1.print_SQL()
res2.print_SQL()
# print(res3.print_SQL())

res4 = Select(g, res1.to_Relation())
res4.print_SQL()

res5 = Select(g, res4.to_Relation())
res5.print_SQL()