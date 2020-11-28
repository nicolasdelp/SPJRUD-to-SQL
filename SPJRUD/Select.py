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

    def to_SQL(self):
        return "SELECT * FROM " + self.subExpressionRight.get_Name() + " WHERE " + self.subExpressionLeft.return_List()[0] + '=' + self.subExpressionLeft.return_List()[1]