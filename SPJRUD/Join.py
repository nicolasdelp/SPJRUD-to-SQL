from SPJRUD.SPJRUD import SPJRUD
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

        self.AttributeInCommon()

    def check_Expression(self, firstRelation, secondRelation): 
        attributes = []
        inTheList = 0
        for att in firstRelation.get_Attributes():
            attributes.append(att.get_Name())
        
        for att in secondRelation.get_Attributes():
            if att.get_Name() in attributes:
                inTheList += 1
        
        if inTheList == 0:
            raise Exception("La jointure n\'est pas possible aucun attribut n\'est dans les deux relations")

    def get_Relation(self): #retourne la relation qui a été "modifié"
        attributes = []
        for att in self.subExpressionLeft.get_Attributes():
            attributes.append(att)

        for att in self.subExpressionRight.get_Attributes():
            if att not in attributes:
                attributes.append(att)

        res = Relation("JoinRelation", attributes)
        return res

    def AttributeInCommon(self): #les éléments en commun dans les deux relations
        attributes = []
        for att in self.subExpressionLeft.get_Attributes():
            attributes.append(att)

        self.attributeInCommon = []
        for att in self.subExpressionRight.get_Attributes():
            if att in attributes:
                self.attributeInCommon.append(att)

    def set_SQL(self, relation): #str
        element = []
        for elem in self.attributeInCommon:
            element.append(self.subExpressionLeft.get_Name() + "." + elem.get_Name() + "=" + self.subExpressionRight.get_Name() + "." + elem.get_Name())

        if (self.subExpressionLeft.get_SQL() == self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name()):
            res = "SELECT * FROM " + self.subExpressionLeft.get_Name() + " INNER JOIN " + self.subExpressionRight.get_Name() + " ON " + ", ".join(element)

        elif (self.subExpressionLeft.get_SQL() != self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() == self.subExpressionRight.get_Name()):
            res = "SELECT * FROM (" + self.subExpressionLeft.get_Name() + ") INNER JOIN " + self.subExpressionRight.get_Name() + " ON " + ", ".join(element)

        elif (self.subExpressionLeft.get_SQL() == self.subExpressionLeft.get_Name()) and (self.subExpressionRight.get_SQL() != self.subExpressionRight.get_Name()):
            res = "SELECT * FROM " + self.subExpressionLeft.get_Name() + " INNER JOIN (" + self.subExpressionRight.get_Name() + ") ON " + ", ".join(element)

        else:
            res = "SELECT * FROM (" + self.subExpressionLeft.get_Name() + ") INNER JOIN (" + self.subExpressionRight.get_Name() + ") ON " + ", ".join(element)

        relation.set_SQL(res)

    def print_SQL(self): #affiche à la console la requette SQL
        res = self.get_Relation()
        self.set_SQL(res)
        print(res.get_SQL())