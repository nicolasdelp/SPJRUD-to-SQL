from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Select(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight): 
        if not isinstance(subExpressionLeft, Ope):
            raise Exception("Le premier parametre doit etre du type \'Ope\'")

        if not isinstance(subExpressionRight, Relation):
            raise Exception("Le deuxieme parametre doit etre du type \'Relation\'")
        
        if isinstance(subExpressionLeft, Equal): #si l'expression est une égalité de 2 paramêtres
            self.subExpressionLeft = subExpressionLeft #liste retourné par l'égalitée
            self.subExpressionRight = subExpressionRight #relation sur laquelle on doit travailler
        
        self.check_Expression(subExpressionLeft.return_NameList()[0], subExpressionRight) #verifie si l'attribut de gauche de subExpression est bien dans la relation

        if isinstance(subExpressionLeft.get_AttributeRight(), Attribute): #si l'attribut de droite de subExpression est de type Attribute on verifie si il est dans la relation
            self.check_Expression(subExpressionLeft.get_AttributeRight().get_Name(), subExpressionRight)

        self.set_SQL()

    def check_Expression(self, attributeName, relation): 
        names = []
        for att in relation.get_Attributes():
            names.append(att.get_Name())
        
        if attributeName not in names:
            raise Exception("Cet attribut n\'existe pas dans la relation")

    def get_Relation(self): #retourne la relation qui a été "modifié"
        return self.subExpressionRight
    
    def set_SQL(self): #remove duplicates
        if self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name():
            res = "SELECT * FROM " + self.subExpressionRight.get_SQL() + " WHERE " + self.subExpressionLeft.return_NameList()[0] + '=' + self.subExpressionLeft.return_NameList()[1]
        else:
            res = "SELECT * FROM (" + self.subExpressionRight.get_SQL() + ") WHERE " + self.subExpressionLeft.return_NameList()[0] + '=' + self.subExpressionLeft.return_NameList()[1]

        self.subExpressionRight.set_SQL(res)
    
    def print_SQL(self): #affiche à la console la requette SQL
        res = self.get_Relation()
        print(res.get_SQL())