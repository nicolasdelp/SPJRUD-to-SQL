from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Join(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):

        valid_Join(subExpressionLeft, subExpressionRight)

        self.firstRelation = subExpressionLeft
        self.secondRelation = subExpressionRight

        self.AttributeInCommon()

    def AttributeInCommon(self):
        """
        Enregistre les atributs en communs et crée la nouvelle relation suite à la jointure
        """
        attributes = []
        self.attributeInCommon = []

        for att in self.firstRelation.get_Attributes():
            attributes.append(att)

        for att in self.secondRelation.get_Attributes():
            if att not in attributes:
                attributes.append(att)
            else:
                self.attributeInCommon.append(att)

        self.newRelation = Relation("JoinRelation", attributes)

    def get_Relation(self):
        """
        Retourne la relation suite aux modifications effectuées
        """
        return self.newRelation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        element = []

        for elem in self.attributeInCommon:
            element.append(self.firstRelation.get_Name() + "." + elem.get_Name() + "=" + self.secondRelation.get_Name() + "." + elem.get_Name())

        sql = "SELECT * FROM (" + self.firstRelation.get_SQL() + ") INNER JOIN (" + self.secondRelation.get_SQL() + ") ON " + ", ".join(element)

        self.newRelation.set_SQL(sql)

    def print_SQL(self):
        """
        Retourne la liste des requêtes SQL de la relation
        """
        return self.newRelation.get_SQL()