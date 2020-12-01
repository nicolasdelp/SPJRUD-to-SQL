from SPJRUD.SPJRUD import SPJRUD
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Rename(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        if not isinstance(subExpressionLeft, Equal):
            raise Exception("Le premier parametre doit etre du type \'Equal\'")
        if isinstance(subExpressionLeft, Equal):
            if not isinstance(subExpressionLeft.get_AttributeLeft(), Attribute):
                raise Exception("Le premier sous-parametre du premier parametre doit etre du type \'Attribute\'")
            if not isinstance(subExpressionLeft.get_AttributeRight(), Constante):
                raise Exception("Le second sous-parametre du premier parametre doit etre du type \'Constante\'")
        if not isinstance(subExpressionRight, Relation):
            raise Exception("Le second parametre doit etre du type \'Relation\'")

        self.check_Expression(subExpressionLeft.return_NameList()[0], subExpressionRight) #verifie si l'attribut de gauche de subExpression est bien dans la relation

        self.subExpressionLeft = subExpressionLeft
        self.subExpressionRight = subExpressionRight

        self.set_SQL()

    def check_Expression(self, attributeName, relation): 
        names = []
        for att in relation.get_Attributes():
            names.append(att.get_Name())
        
        if attributeName not in names:
            raise Exception("Cet attribut n\'existe pas dans la relation")

    def get_Relation(self): #retourne la relation qui a été "modifié"
        return self.subExpressionRight

    def set_SQL(self):
        if self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name():
            res = "SELECT " + self.subExpressionLeft.return_NameList()[0] + " AS " + self.subExpressionLeft.return_NameList()[1] + " FROM " + self.subExpressionRight.get_SQL()
        else:
            res = "SELECT " + self.subExpressionLeft.return_NameList()[0] + " AS " + self.subExpressionLeft.return_NameList()[1] + " FROM (" + self.subExpressionRight.get_SQL() + ")"
        self.subExpressionRight.set_SQL(res)

    def print_SQL(self): #affiche à la console la requette SQL
        res = self.get_Relation()
        print(res.get_SQL())