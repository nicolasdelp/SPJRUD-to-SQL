__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

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


#---------------- A PARTIR D'UNE STUCTURE ----------------#
# w = Relation(
#     "NomDeLaRelation", 
#             [
#                 Attribute("attribute1", 'INTEGER'), 
#                 Attribute("attribute2", 'TEXT'), 
#                 Attribute("attribute3", 'TEXT'), 
#                 Attribute("attribute4", 'TEXT')
#             ])

# a = Project(['attribute2', 'attribute4'], w) #Créer une expression SPJRUD
# b = Select(Equal("attribute1", Constante("qd")), w)
# print(a) #Donne l'expression SPJRUD
# print(" ")
# print(b.get_SQL()) #Affiche la requete SQL
# print(" ")



#---------------- A PARTIR D'UNE BASE DE DONNEE ----------------#
# creat_Database("database") #Créé la base de donnée des TPs SQL pour faire des tests

# print_TableFromADatabase("database.db", "emp") #Affiche le contenu d'une table

# x = creat_RelationFromDatabase("database.db", "emp2") #Créé une relation à partir d'une table
# y = creat_RelationFromDatabase("database.db", "emp") #Créé une relation à partir d'une table
# z = creat_RelationFromDatabase("database.db", "dept") #Créé une relation à partir d'une table

# b = Project(["ename", "sal", "deptno"], y) #Créer une expression SPJRUD
# print(b) #Donne l'expression SPJRUD
# print(" ")
# print(b.get_SQL()) #Affiche la requete SQL
# print(" ")
# executeSQL_OnDatabase("database.db", b.get_SQL()) #Execute une requete SQL sur une base de donnée




