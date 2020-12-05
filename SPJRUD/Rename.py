from SPJRUD.SPJRUD import SPJRUD
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Rename(SPJRUD):

    def __init__(self, oldName, newName, subExpressionRight):
        """
        Constructeur de l'opérateur Select
        - oldName = le nom de l'attribut cible
        - newName = le nouveau nom de cet attribut
        - subExpressionRight = une relation

        >> Rename(oldName, newName, Relation)
        """
        if isinstance(subExpressionRight, Relation):
            rel = subExpressionRight
        if isinstance(subExpressionRight, SPJRUD):
            rel = subExpressionRight.get_NewRelation()

        valid_Rename(oldName, newName, rel)

        self.oldName = oldName
        self.newName = newName
        self.relation = rel

        self.set_NewRelation()
        self.set_SQL()
    
    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Rename
        """
        attributes = []
        for att in self.relation.get_Attributes():
            if att.get_Name() != self.oldName:
                attributes.append(att)
            elif att.get_Name() == self.oldName:
                attributes.append(Attribute(self.newName, att.get_Type()))

        self.newRelation = Relation(self.relation.get_Name(), attributes)

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        attributes = []
        for att in self.relation.get_Attributes():
            if att.get_Name() != self.oldName:
                attributes.append(att.get_Name())

        sql = "SELECT " + self.oldName + " AS " + self.newName + "," + ",".join(attributes) + " FROM (" + self.relation.get_SQL() + ")"
        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()