__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

from Representation.Attribute import Attribute

import sys
sys.tracebacklimit = 0

class Relation:

    def __init__(self, relation_name, list_attributes, SPJRUD=""):
        """
        Constructeur d'une relation
        - relation_name = le nom de la relation
        - list_attributes = la liste d'attributs de la relation
        - SPJRUD = l'expression SPJRUD de la relation

        >> Relation("nomdelarelation", [a, b, c, d])
        >> Relation("nomdelarelation", [a, b, c, d], SPJRUD="Join(relation1, relation2))
        """
        self.SQL = []
        self.set_Name(relation_name)
        self.set_Attributes(list_attributes)
        self.set_SQL(relation_name)
        self.SPJRUD = SPJRUD

    def __str__(self):
        """
        Méthode qui retourne la relation sous forme d'une chaine de caractère
        """
        if len(self.SPJRUD) == 0:
            return self.relation_name
        else:
            return self.SPJRUD

    def set_Name(self, relation_name):
        """
        Enregistre le nom de la relation
        - relation_name = le nom de la relation
        """
        if not isinstance(relation_name, str):
            raise Exception("Relation : Le nom de la relation doit etre du type \'str\'")

        self.relation_name = relation_name

    def get_Name(self):
        """
        Retourne le nom de la relation
        """
        return self.relation_name

    def set_Attributes(self, list_attributes):
        """
        Enregistre la liste d'attributs
        - list_attributes = la liste d'attributs
        """
        if not isinstance(list_attributes, list):
            raise Exception("Relation : Le parametre doit etre du type \'list\'")
        
        for att in list_attributes:
            if not isinstance(att, Attribute):
                raise Exception("Relation : Les elements de la liste ne sont pas du type \'Attibute\'")
            
        self.list_attributes = list_attributes

    def get_Attributes(self):
        """
        Retourne les attributs de la relation
        """
        return self.list_attributes

    def set_SQL(self, SQL):
        """
        Enregistre la requête SQL de la relation
        - SQL = la requête SQL
        """
        self.SQL = SQL

    def get_SQL(self):
        """
        Retourne la requête SQL de la relation
        """
        return self.SQL

