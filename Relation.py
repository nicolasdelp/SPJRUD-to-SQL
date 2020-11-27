from Attribute import Attribute

class Relation:

    def __init__(self, relation_name, list_attributes):
        self.set_Name(relation_name)
        self.set_Attributes(list_attributes)

    def set_Name(self, relation_name):
        if not isinstance(relation_name, str):
            raise Exception("Le nom de la relation doit etre du type \'str\'")

        self.relation_name = relation_name

    def get_Name(self):
        return self.relation_name

    def set_Attributes(self, list_attributes):
        if not isinstance(list_attributes, list):
            raise Exception("Le parametre doit etre du type \'list\'")
        
        for att in list_attributes:
            if not isinstance(att, Attribute):
                raise Exception("Les elements de la liste ne sont pas du type \'Attibute\'")
            
        self.list_attributes = list_attributes

    def get_Attributes(self):
        return self.list_attributes