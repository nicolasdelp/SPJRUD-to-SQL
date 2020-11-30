from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Join(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        if not isinstance(subExpressionLeft, Relation):
            raise Exception("Le premier parametre doit etre du type \'Relation\'")
        if not isinstance(subExpressionRight, Relation):
            raise Exception("Le second parametre doit etre du type \'Relation\'")

        self.check_Expression(subExpressionLeft, subExpressionRight) #verifie si la jointure est possible

        self.subExpressionLeft = subExpressionLeft #premiere relation
        self.subExpressionRight = subExpressionRight #deuxieme relation

        self.set_SQL()

    def check_Expression(self, firstRelation, secondRelation): 
        firstAttributes = []
        inTheList = 0
        for att in firstRelation.get_Attributes():
            firstAttributes.append(att.get_Name())
        
        for att in secondRelation.get_Attributes():
            if att.get_Name() in firstAttributes:
                inTheList += 1
        
        if inTheList == 0:
            raise Exception("La jointure n\'est pas possible aucun attribut n\'est dans les deux relations")

    def get_Relation(self): #retourne la relation qui a été "modifié" --------MAUVAIS
        attributes = []
        for att in self.subExpressionLeft.get_Attributes():
            attributes.append(att)
        for att in self.subExpressionRight.get_Attributes():
            attributes.append(att)
        res = Relation("JoinRelation", attributes)

    def set_SQL(self): #str
        pass

    def to_New_Relation(self): #Relation
        pass