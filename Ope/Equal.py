from Ope.Ope import Ope
from Representation.Attribute import Attribute
from Representation.Constante import Constante

class Equal(Ope):
    
    def __init__(self, attributeLeft, attributeRight): #Left = attribut | Right = constante ou attribut
        if not isinstance(attributeLeft, Attribute):
            raise Exception("Le premier parametre doit etre du type \'Attribute\'")

        if not isinstance(attributeRight, Attribute):
            if not isinstance(attributeRight, Constante):
                raise Exception("Le deuxieme parametre doit etre du type \'Attribute\' ou \'Constante\'")
        
        self.attributeLeft = attributeLeft
        self.attributeRight = attributeRight

    def get_AttributeLeft(self):
        return self.attributeLeft

    def get_AttributeRight(self):
        return self.attributeRight

    def return_NameList(self): #retourne une liste pour permettre à l'opérateur du dessus d'agir
        if isinstance(self.attributeRight, Attribute):
            if self.attributeLeft.isComparable(self.attributeRight):
                return [self.attributeLeft.get_Name(), self.attributeRight.get_Name()]
        
        if isinstance(self.attributeRight, Constante):
            return [self.attributeLeft.get_Name(), self.attributeRight.get_Value()]