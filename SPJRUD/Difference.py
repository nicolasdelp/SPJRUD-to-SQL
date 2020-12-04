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
        valid_Difference(subExpressionLeft, subExpressionRight)

        self.firstRelation = subExpressionLeft
        self.secondRelation = subExpressionRight

        self.set_NewRelation()
        self.set_SQL()
    
    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Difference
        """
        self.newRelation = Relation(self.firstRelation.get_Name(), self.firstRelation.get_Attributes())

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
