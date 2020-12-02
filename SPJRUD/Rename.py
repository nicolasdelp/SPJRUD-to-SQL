from SPJRUD.SPJRUD import SPJRUD
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Rename(SPJRUD):

    def __init__(self, oldName, newName, subExpressionRight):

        self.oldName = oldName
        self.newName = newName
        self.relation = subExpressionRight

        self.set_NewRelation()
        self.set_SQL()
    
    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Rename
        """
        attributes = []
        for att in self.relation.get_Attributes():
            if att.get_Name() != self.oldName:
                attributes.append(att)
            elif att.get_Name() == self.oldName:
                attributes.append(Attribute(self.newName, att.get_Type()))

        self.newRelation = Relation("RenameRelation", attributes)

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        sql = "SELECT " + self.oldName + " AS " + self.newName + " FROM (" + self.relation.get_SQL() + ")"
        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la liste des requêtes SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()