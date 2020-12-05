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
        if isinstance(subExpressionRight, Relation):
            rel = subExpressionRight
        if isinstance(subExpressionRight, SPJRUD):
            rel = subExpressionRight.get_NewRelation()

        valid_Project(listOfParameters, rel)

        self.listOfParameters = listOfParameters
        self.relation = rel
        
        self.set_NewRelation()
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

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        #elements n'ayant pas de double
        sql1 = "SELECT " + ",".join(self.listOfParameters) + " FROM (" + self.relation.get_SQL() + ") GROUP BY " + ",".join(self.listOfParameters) + " HAVING COUNT(*) = 1"
        #elements ayant un (des) double(s)
        sql2 = "SELECT " + ",".join(self.listOfParameters) + " FROM (" + self.relation.get_SQL() + ") GROUP BY " + ",".join(self.listOfParameters) + " HAVING COUNT(*) > 1"
        #union des deux requetes
        sql = sql1 + " UNION " + sql2

        self.newRelation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()