from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Difference(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        """
        Constructeur de l'opérateur Difference
        - subExpressionLeft = une relation
        - subExpressionRight = une relation

        >> Difference(Relation, Relation)
        """
        if isinstance(subExpressionLeft, Relation):
            rel = subExpressionLeft
            self.SPJRUD1 = False
        elif isinstance(subExpressionLeft, SPJRUD):
            rel = subExpressionLeft.get_NewRelation()
            self.SPJRUD1 = True
        else:
            raise Exception("Le premier parametre doit etre du type \'Relation\' ou un operateur SPJRUD")

        if isinstance(subExpressionRight, Relation):
            rel2 = subExpressionRight
            self.SPJRUD2 = False
        elif isinstance(subExpressionRight, SPJRUD):
            rel2 = subExpressionRight.get_NewRelation()
            self.SPJRUD2 = True
        else:
            raise Exception("Le second parametre doit etre du type \'Relation\' ou un operateur SPJRUD")

        valid_Difference(rel, rel2)

        self.firstRelation = rel
        self.secondRelation = rel2

        self.set_NewRelation()
        self.set_SQL()

    def __str__(self):
        if not self.SPJRUD1 and not self.SPJRUD2:
            return "Difference(Relation('" + self.firstRelation.__str__() + "'), Relation('" + self.secondRelation.__str__() + "'))"
        if self.SPJRUD1 and not self.SPJRUD2:
            return "Difference(" + self.firstRelation.__str__() + ", Relation('" + self.secondRelation.__str__() + "'))"
        if not self.SPJRUD1 and self.SPJRUD2:
            return "Difference(Relation('" + self.firstRelation.__str__() + "'), " + self.secondRelation.__str__() + ")"
        if self.SPJRUD1 and self.SPJRUD2:
            return "Difference(" + self.firstRelation.__str__() + ", " + self.secondRelation.__str__() + ")"
    
    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Difference
        """
        self.newRelation = Relation(self.firstRelation.get_Name(), self.firstRelation.get_Attributes(), SPJRUD=self.__str__())

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        sql = "SELECT * FROM (" + self.firstRelation.get_Name() + ") EXCEPT SELECT * FROM (" + self.secondRelation.get_Name() + ")"
        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()
