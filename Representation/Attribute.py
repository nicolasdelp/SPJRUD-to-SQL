from Representation.Node import Node

class Attribute(Node):

    def __init__(self, attribute_name, attribute_type):
        self.get_Name(attribute_name)
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