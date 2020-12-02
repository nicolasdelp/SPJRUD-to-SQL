from Ope.Ope import Ope
from Representation.Attribute import Attribute
from Representation.Constante import Constante

class Equal(Ope):
    
    def __init__(self, attributeLeft, attributeRight): #Left = attribut | Right = constante ou attribut
        if not isinstance(attributeLeft, str):
            raise Exception("Le premier parametre doit etre du type \'str\'")

        if not isinstance(attributeRight, str):
            raise Exception("Le deuxieme parametre doit etre du type \'str\'")
        
        self.attributeLeft = attributeLeft
        self.attributeRight = attributeRight
        self.sign = " = "

    def get_AttributeLeft(self):
        return self.attributeLeft

    def get_AttributeRight(self):
        return self.attributeRight

    def get_Sign(self):
        return self.sign

    def return_NameList(self): #retourne une liste pour permettre à l'opérateur du dessus d'agir
        return [self.attributeLeft, self.attributeRight]