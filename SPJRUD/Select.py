from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute
from Representation.Constante import Constante

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

        self.set_NewRelation()
        self.set_SQL()

    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Select
        """
        self.newRelation = Relation(self.relation.get_Name(), self.relation.get_Attributes())

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation
    
    def set_SQL(self):
        """
        Enregistre la requête SQL dans la relation
        """
        if isinstance(self.operation.get_AttributeRight(), Constante):
            sql = "SELECT * FROM (" + self.relation.get_SQL() + ") WHERE " + self.operation.return_NameList()[0] + self.operation.get_Sign() + "'" + self.operation.return_NameList()[1] + "'"
        else:
            sql = "SELECT * FROM (" + self.relation.get_SQL() + ") WHERE " + self.operation.return_NameList()[0] + self.operation.get_Sign() + self.operation.return_NameList()[1]

        self.newRelation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la liste des requêtes SQL de la relation
        """
        return self.newRelation.get_SQL()