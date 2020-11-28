from SPJRUD.SPJRUD import SPJRUD
from SPJRUD.Select import Select
from SPJRUD.Join import Join

from Representation.Node import Node

x = Select()

if isinstance(x, Node):
    print("Hello")
if isinstance(x, SPJRUD):
    print("World")
if isinstance(x, Select):
    print("World")
if isinstance(x, Join):
    print("World")