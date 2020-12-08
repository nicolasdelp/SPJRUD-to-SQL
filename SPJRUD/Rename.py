__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

from SPJRUD.SPJRUD import SPJRUD
from Ope.Equal import Equal
from Representation.Constante import Constante
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

import sys
sys.tracebacklimit = 0

class Rename(SPJRUD):

    def __init__(self, oldName, newName, subExpressionRight):
        """
        Constructeur de l'opérateur Rename
        - oldName = le nom de l'attribut cible
        - newName = le nouveau nom de cet attribut
        - subExpressionRight = une relation ou un SPJRUD

        >> Rename(oldName, newName, Relation)
        """
        if isinstance(subExpressionRight, Relation):
            rel = subExpressionRight
            self.SPJRUD = False
        elif isinstance(subExpressionRight, SPJRUD):
            rel = subExpressionRight.get_NewRelation()
            self.SPJRUD = True
        else:
            raise Exception("SPJRUD -> Rename : Le second parametre doit etre du type \'Relation\' ou etre un operateur SPJRUD")

        valid_Rename(oldName, newName, rel)

        self.oldName = oldName
        self.newName = newName
        self.relation = rel

        self.set_NewRelation()
        self.set_SQL()

    def __str__(self):
        """
        Méthode qui retourne l'opérateur sous forme d'une chaine de caractère
        """
        if not self.SPJRUD:
            return "Rename('" + self.oldName + "', '" + self.newName + "', Relation('" + self.relation.__str__() + "'))"

        if self.SPJRUD:
            return "Rename('" + self.oldName + "', '" + self.newName + "', " + self.relation.__str__() + ")"
    
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

        self.newRelation = Relation(self.relation.get_Name(), attributes, SPJRUD=self.__str__())

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        attributes = []
        for att in self.relation.get_Attributes():
            if att.get_Name() != self.oldName:
                attributes.append(att.get_Name())

        sql = "SELECT " + self.oldName + " AS " + self.newName + "," + ",".join(attributes) + " FROM (" + self.relation.get_SQL() + ")"
        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()