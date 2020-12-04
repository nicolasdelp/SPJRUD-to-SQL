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

from Representation.Node import Node

from sql import *

# creat_Database("database")
# print_Databases("database.db")
# for x in get_AttributesFromTable("database.db", "emp"):
#     print(x)

# creat_Database("database")
y = creat_RelationFromDatabase("database.db", "emp")

a = Select(Equal("ename", Constante("JAMES")), y)

b = Project(["ename", "sal", 'job'], y)


sql = b.get_SQL()

executeSQL_OnDatabase("database.db", sql)