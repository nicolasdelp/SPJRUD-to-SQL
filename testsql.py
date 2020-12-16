from SPJRUD import SPJRUD
from SPJRUD.Select import Select
from SPJRUD.Project import Project
from SPJRUD.Join import Join
from SPJRUD.Rename import Rename
from SPJRUD.Union import Union
from SPJRUD.Difference import Difference
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Attribute import Attribute
from Representation.Relation import Relation

from sql import *

#Sur une base de donnée

creat_Database("database")
print_TableFromADatabase("database.db", "emp")

x = creat_RelationFromDatabase("database.db", "emp2")
y = creat_RelationFromDatabase("database.db", "emp")
z = creat_RelationFromDatabase("database.db", "dept")

a = Select(Equal("ename", "job"), y)
print(a)
print(a.get_SQL())
print("--------------------------------------------------------------")

b = Project(["ename", "sal", "deptno"], y)
print(b)
print(b.get_SQL())
print("--------------------------------------------------------------")

bb = Project(["dname", "deptno", "loc"], z)
print(bb)
print(bb.get_SQL())
print("--------------------------------------------------------------")

c = Join(b, bb)
print(c)
print(c.get_SQL())
print("--------------------------------------------------------------")

d = Rename("ename", "Nom", y)
print(d)
print(d.get_SQL())
print("--------------------------------------------------------------")

e = Union(x, y)
print(e)
print(e.get_SQL())
print("--------------------------------------------------------------")

f = Difference(x, y)
print(f)
print(f.get_SQL())
print("--------------------------------------------------------------")

g = Join(Project(["name", "sal", "job", "deptno"], Select(Equal("name", Constante("JAMES")), Rename("ename", "name", y))), z)
print(g)
print(g.get_SQL())
print("--------------------------------------------------------------")

h = Select(Equal("name", Constante("JAMES")),  Rename("ename", "name", y))
print(h)
print(h.get_SQL())
print("--------------------------------------------------------------")

i = Project(["name", "sal", "job", "deptno"], Select(Equal("sal", Constante(5000.0)), Rename("ename", "name", y)))
print(i)
print(i.get_SQL())
print("--------------------------------------------------------------")

print("--------------------------------------------------------------")
print("--------------------------------------------------------------")
executeSQL_OnDatabase("database.db", i.get_SQL())
print("--------------------------------------------------------------")
print("--------------------------------------------------------------")

#Sur une relation créée moi-même

rel = Relation(
        "Personne", 
            [
                Attribute("id", 'INTEGER'), 
                Attribute("nom", 'TEXT'), 
                Attribute("prenom", 'TEXT')
            ])

rel2 = Relation(
        "Infos_Personne", 
            [
                Attribute("id", 'INTEGER'), 
                Attribute("sexe", 'TEXT'), 
                Attribute("age", 'INTEGER'),
                Attribute("taille", 'REAL'),
                Attribute("poids", 'REAL')
            ])

a = Select(Equal("nom", "prenom"), rel)
print(a)
print(a.get_SQL())
print("--------------------------------------------------------------")

b = Project(["id", "nom", "prenom"], rel)
print(b)
print(b.get_SQL())
print("--------------------------------------------------------------")

bb = Project(["id", "sexe", "age"], rel2)
print(bb)
print(bb.get_SQL())
print("--------------------------------------------------------------")

c = Join(b, bb)
print(c)
print(c.get_SQL())
print("--------------------------------------------------------------")

d = Rename("nom", "Name", rel)
print(d)
print(d.get_SQL())
print("--------------------------------------------------------------")

g = Join(Project(["id", "nom", "prenom"], Select(Equal("nom", Constante("DELPLANQUE")), rel)), rel2)
print(g)
print(g.get_SQL())
print("--------------------------------------------------------------")

h = Select(Equal("NomDeFamille", Constante("DELPLANQUE")),  Rename("nom", "NomDeFamille", rel))
print(h)
print(h.get_SQL())
print("--------------------------------------------------------------")