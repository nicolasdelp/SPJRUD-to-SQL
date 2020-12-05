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
# print_Databases("database.db")
# for x in get_AttributesFromTable("database.db", "emp"):
#     print(x)

x = creat_RelationFromDatabase("database.db", "emp2")
y = creat_RelationFromDatabase("database.db", "emp")
z = creat_RelationFromDatabase("database.db", "dept")

# a = Select(Equal("ename", "sal"), y)

b = Project(["ename", "sal", "deptno"], y)

bb = Project(["dname", "deptno", "loc"], z)

c = Join(b, bb)

d = Rename("ename", "Nom", y)

e = Union(x, y)

f = Difference(x, y)

g = Join(Project(["sal", "job", "deptno"], Select(Equal("name", Constante("JAMES")), Rename("ename", "name", y))), z)


sql = g.get_SQL()

executeSQL_OnDatabase("database.db", sql)