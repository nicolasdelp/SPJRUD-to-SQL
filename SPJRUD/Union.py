from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Union(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        if not isinstance(subExpressionLeft, Relation):
            raise Exception("Le premier parametre doit etre du type \'Relation\'")
        if not isinstance(subExpressionRight, Relation):
            raise Exception("Le second parametre doit etre du type \'Relation\'")

        self.check_Expression(subExpressionLeft, subExpressionRight) #verifie si la jointure est possible

        self.subExpressionLeft = subExpressionLeft #premiere relation
        self.subExpressionRight = subExpressionRight #deuxieme relation
    
    def check_Expression(self, firstRelation, secondRelation): 
        attributes = []
        for att in firstRelation.get_Attributes():
            attributes.append(att.get_Name())
        
        if len(firstRelation.get_Attributes()) != len(secondRelation.get_Attributes()):
            raise Exception("Les deux relations n\'ont pas le meme nombre d\'attributs")
        
        for att in secondRelation.get_Attributes():
            if att.get_Name() not in attributes:
                raise Exception("Les deux relation ne sont pas compatible, les attributs ne sont pas les memes")
    
    def get_Relation(self): #retourne la relation qui a été "modifié"
        res = Relation("UnionRelation", self.subExpressionLeft.get_Attributes())
        return res

    def set_SQL(self, relation):
        if (self.subExpressionLeft.get_SQL() == self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name()):
            res = "(SELECT * FROM " + self.subExpressionLeft.get_Name() + ") UNION (SELECT * FROM " + self.subExpressionRight.get_Name() + ")"

        elif (self.subExpressionLeft.get_SQL() != self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name()):
            res = "(SELECT * FROM (" + self.subExpressionLeft.get_Name() + ")) UNION (SELECT * FROM " + self.subExpressionRight.get_Name() + ")"

        elif (self.subExpressionLeft.get_SQL() == self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() != self.subExpressionRight.get_Name()):
            res = "(SELECT * FROM " + self.subExpressionLeft.get_Name() + ") UNION (SELECT * FROM (" + self.subExpressionRight.get_Name() + "))"

        else:
            res = "(SELECT * FROM (" + self.subExpressionLeft.get_Name() + ")) UNION (SELECT * FROM (" + self.subExpressionRight.get_Name() + "))"
        
        relation.set_SQL(res)

    def print_SQL(self): #affiche à la console la requette SQL
        res = self.get_Relation()
        self.set_SQL(res)
        print(res.get_SQL())
