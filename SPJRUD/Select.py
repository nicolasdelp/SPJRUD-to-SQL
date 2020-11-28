from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope

class Select(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight): 
        if not isinstance(subExpressionLeft, Ope):
            raise Exception("Le premier paramêtre doit etre de type \'Ope\'")
        if not isinstance(subExpressionRight,)

    def to_SQL(self): #str
        pass

    def to_New_Relation(self): #Relation
        pass