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

import sqlite3

def requestOnDatabase(database, SPJRUD):
    #connexion à la base de donnée
    connection = sqlite3.connect(database + ".db")
    cursor = connection.cursor()

    for row in cursor.execute(SPJRUD.print_SQL()):
        print(row)
    
    #interruption de la connexion
    connection.close()

def getAttributesFromTable(databaseName, table) :
    #connexion à la base de donnée
    connection = sqlite3.connect(databaseName + ".db")
    cursor = connection.cursor()

    #récupère les caractéristique des colonnes
    infos = cursor.execute("PRAGMA table_info(" + table + ");")
    
    #attributes = []
    for tup in infos :
        print(tup)
        #attributes.append(Attribute(tup[1], tup[2]))
    
    #return attributes or False

# x = Equal(Attribute("ename", 'TEXT'), Constante("BLAKE"))
# y = Relation("emp", )

# requestOnDatabase("database", Select())