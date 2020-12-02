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
        
        self.clean_SQL()
        self.set_SQL()
    
    def clean_SQL(self):
        """
        Supprime les doublons car SQL ne le fais pas automatiquement
        """
        element = []
        for elem in self.listOfParameters:
            element.append("a." + elem + " = b." + elem)

        sql = "DELETE a FROM (" + self.relation.get_SQL() + ") AS a, (" + self.relation.get_SQL() + ") AS b WHERE " + " AND ".join(element)
        self.relation.set_CleanSQL(sql)

    def get_Relation(self):
        """
        Retourne la relation suite aux modifications effectuées
        """
        return self.relation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        sql = "SELECT " + ",".join(self.listOfParameters) + " FROM (" + self.relation.get_SQL() + ")"
        self.relation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la liste des requêtes SQL de la relation
        """
        return [self.get_Relation().get_CleanSQL(), self.get_Relation().get_SQL()]