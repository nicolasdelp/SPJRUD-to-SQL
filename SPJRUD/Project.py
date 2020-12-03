from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Project(SPJRUD):

    def __init__(self, listOfParameters, subExpressionRight):
        """
        Constructeur de l'opérateur Project
        - listOfParameters = une liste de paramètres (string) à projeter
        - subExpressionRight = une relation

        >> Project(['Param1', 'Param2', ...], Relation)
        """
        valid_Project(listOfParameters, subExpressionRight)

        self.listOfParameters = listOfParameters
        self.relation = subExpressionRight
        
        self.set_NewRelation()
        self.set_CleanSQL()
        self.set_SQL()

    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Project
        """
        newAttributes = []

        for elem in self.listOfParameters:
            for att in self.relation.get_Attributes():
                if elem == att.get_Name():
                    newAttributes.append(att)

        self.newRelation = Relation(self.relation.get_Name(), newAttributes)

    def get_NewRelation(self):
        """
        Retourne la relation suite aux modifications effectuées
        """
        return self.newRelation
    
    def set_CleanSQL(self):
        """
        Supprime les doublons car SQL ne le fais pas automatiquement
        """
        element = []

        for elem in self.listOfParameters:
            element.append("a." + elem + " = b." + elem)

        sql = "DELETE a FROM (" + self.relation.get_SQL() + ") AS a, (" + self.relation.get_SQL() + ") AS b WHERE " + " AND ".join(element)
        self.newRelation.set_CleanSQL(sql)
    
    def get_CleanSQL(self):
        """
        Retourne la requête SQL qui supprime les doublons de la nouvelle relation
        """
        return self.newRelation.get_CleanSQL()

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        sql = "SELECT " + ",".join(self.listOfParameters) + " FROM (" + self.relation.get_SQL() + ")"
        self.newRelation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()