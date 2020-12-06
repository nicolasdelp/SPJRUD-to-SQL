from SPJRUD.SPJRUD import SPJRUD
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

# creat_Database("database")
# print_TableFromADatabase("database.db", "emp")
# for x in get_AttributesFromTable("database.db", "emp"):
#     print(x)

x = creat_RelationFromDatabase("database.db", "emp2")
y = creat_RelationFromDatabase("database.db", "emp")
z = creat_RelationFromDatabase("database.db", "dept")

# a = Select(Equal("ename", "sal"), y)

b = Project(["ename", "sal", "deptno"], y)
print(b)

bb = Project(["dname", "deptno", "loc"], z)
print(bb)

c = Join(b, bb)
print(c)

d = Rename("ename", "Nom", y)
print(d)

e = Union(x, y)
print(e)

f = Difference(x, y)
print(f)

g = Join(Project(["name", "sal", "job", "deptno"], Select(Equal("name", Constante("JAMES")), Rename("ename", "name", y))), z)
print(g)

h = Select(Equal("name", Constante("JAMES")),  Rename("ename", "name", y))
print(h)

i = Project(["name", "sal", "job", "deptno"], Select(Equal("name", Constante("JAMES")), Rename("ename", "name", y)))
print(i)


sql = g.get_SQL()

# executeSQL_OnDatabase("database.db", sql)