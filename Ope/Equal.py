__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

from Ope.Ope import Ope
from Representation.Attribute import Attribute
from Representation.Constante import Constante

import sys
sys.tracebacklimit = 0

class Equal(Ope):
    
    def __init__(self, attributeLeft, attributeRight): #Left = attribut | Right = constante ou attribut
        if not isinstance(attributeLeft, str):
            raise Exception("Ope -> Equal : Le premier parametre doit etre du type \'str\'")

        if not isinstance(attributeRight, str):
            if not isinstance(attributeRight, Constante):
                raise Exception("Ope -> Equal : Le deuxieme parametre doit etre du type \'str\' ou \'Constante\'")
        
        self.attributeLeft = attributeLeft
        self.attributeRight = attributeRight
        self.sign = " = "

    def __str__(self):
        if isinstance(self.attributeRight, Constante):
            return "Equal('" + self.attributeLeft + "', Constante('" + str(self.attributeRight.get_Value()) + "'))"
        else:
            return "Equal('" + self.attributeLeft + "', '" + self.attributeRight + "')"

    def get_AttributeLeft(self):
        return self.attributeLeft

    def get_AttributeRight(self):
        return self.attributeRight

    def get_Sign(self):
        return self.sign

    def return_NameList(self): #retourne une liste pour permettre à l'opérateur du dessus d'agir
        if isinstance(self.attributeRight, Constante):
            return [self.attributeLeft, self.attributeRight.get_Value()]
        else:
            return [self.attributeLeft, self.attributeRight]