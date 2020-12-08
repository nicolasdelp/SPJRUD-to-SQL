__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute
from Representation.Constante import Constante

from SPJRUD.Validation import *

import sys
sys.tracebacklimit = 0

class Select(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        """
        Constructeur de l'opérateur Select
        - subExpressionLeft = une opération entre 2 termes (une égalité par exemple)
        - subExpressionRight = une relation ou un SPJRUD

        >> Select(Equal('Param1', 'Param2'), Relation)
        """
        if isinstance(subExpressionRight, Relation):
            rel = subExpressionRight
            self.SPJRUD = False
        elif isinstance(subExpressionRight, SPJRUD):
            rel = subExpressionRight.get_NewRelation()
            self.SPJRUD = True
        else:
            raise Exception("SPJRUD -> Select : Le second parametre doit etre du type \'Relation\' ou etre un operateur \'SPJRUD\'")

        valid_Select(subExpressionLeft, rel)
        
        self.operation = subExpressionLeft
        self.relation = rel

        self.set_NewRelation()
        self.set_SQL()

    def __str__(self):
        """
        Méthode qui retourne l'opérateur sous forme d'une chaine de caractère
        """
        if not self.SPJRUD:
            return "Select(" + self.operation.__str__() + ", Relation('" + self.relation.__str__() + "'))"
        if self.SPJRUD:
            return "Select(" + self.operation.__str__() + ", " + self.relation.__str__() + ")"

    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Select
        """
        self.newRelation = Relation(self.relation.get_Name(), self.relation.get_Attributes(), SPJRUD=self.__str__())

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
            sql = "SELECT * FROM (" + self.relation.get_SQL() + ") WHERE " + self.operation.return_NameList()[0] + self.operation.get_Sign() + "'" + str(self.operation.return_NameList()[1]) + "'"
        else:
            sql = "SELECT * FROM (" + self.relation.get_SQL() + ") WHERE " + self.operation.return_NameList()[0] + self.operation.get_Sign() + self.operation.return_NameList()[1]

        self.newRelation.set_SQL(sql)
    
    def get_SQL(self):
        """
        Retourne la liste des requêtes SQL de la relation
        """
        return self.newRelation.get_SQL()