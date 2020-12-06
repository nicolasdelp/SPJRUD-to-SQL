__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

class Attribute:

    def __init__(self, attribute_name, attribute_type):
        self.set_Name(attribute_name)
        self.set_Type(attribute_type)

    def set_Name(self, attribute_name):
        if not isinstance(attribute_name, str):
            raise Exception("Le nom de l\'attribut doit etre du type \'str\'")

        self.attribute_name = attribute_name

    def get_Name(self):
        return self.attribute_name

    def set_Type(self, attribute_type):
        type_available = ['TEXT', 'BLOB', 'REAL', 'INTEGER', 'NULL']
        #TEXT = str & unicode | BLOB = buffer | REAL = float | INTEGER = int & long | NULL = none

        if not isinstance(attribute_type, str):
            raise Exception("Le parametre doit etre une chaine de caracteres")

        if attribute_type.upper() not in type_available:
            raise Exception("Le type n\'est pas valide")

        self.attribute_type = attribute_type

    def get_Type(self):
        return self.attribute_type

    def isComparable(self, otherAttribute): #vérifie si 2 attributs sont comparables
        if not isinstance(otherAttribute, Attribute):
            raise Exception("Le parametre doit etre du type \'Attribute\'")

        if self.attribute_type != otherAttribute.get_Type():
            raise Exception("Les deux attributs ne sont pas du meme type -> (" + self.attribute_type + ") != (" + otherAttribute.get_Type + ")")

        return True