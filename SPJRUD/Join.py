from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Join(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        """
        Constructeur de l'opérateur Join
        - subExpressionLeft = une relation
        - subExpressionRight = une relation

        >> Join(Relation, Relation)
        """
        valid_Join(subExpressionLeft, subExpressionRight)

        self.firstRelation = subExpressionLeft
        self.secondRelation = subExpressionRight

        self.set_NewRelation()
        self.AttributeInCommon()
        self.set_SQL()


    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Join
        """
        attributes = []

        for att in self.firstRelation.get_Attributes():
            attributes.append(att)

        for att in self.secondRelation.get_Attributes():
            if att not in attributes:
                attributes.append(att)

        self.newRelation = Relation(self.firstRelation.get_Name(), attributes)

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def AttributeInCommon(self):
        """
        Enregistre les atributs en communs de la jointure
        """
        self.attributeInCommon = []

        for att in self.secondRelation.get_Attributes():
            if att in self.firstRelation.get_Attributes():
                self.attributeInCommon.append(att)

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        element = []

        for elem in self.attributeInCommon:
            element.append(self.firstRelation.get_Name() + "." + elem.get_Name() + "=" + self.secondRelation.get_Name() + "." + elem.get_Name())

        sql = "SELECT * FROM (" + self.firstRelation.get_SQL() + ") INNER JOIN (" + self.secondRelation.get_SQL() + ") ON " + ", ".join(element)

        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()