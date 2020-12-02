from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Select(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        """
        Constructeur de l'opérateur Select
        - subExpressionLeft = une opération entre 2 termes (une égalité par exemple)
        - subExpressionRight = une relation

        >> Select(Equal('Param1', 'Param2'), Relation)
        """
        valid_Select(subExpressionLeft, subExpressionRight)
        
        self.operation = subExpressionLeft
        self.relation = subExpressionRight

        self.set_SQL()

    def get_Relation(self):
        """
        Retourne la relation suite aux modifications effectuées
        """
        return self.relation
    
    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        sql = "SELECT * FROM (" + self.relation.get_SQL() + ") WHERE " + self.operation.return_NameList()[0] + self.operation.get_Sign() + self.operation.return_NameList()[1]
        self.relation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la liste des requêtes SQL de la relation
        """
        return self.get_Relation().get_SQL()