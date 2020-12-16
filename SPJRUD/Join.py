__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

from SPJRUD.Validation import *

class Join(SPJRUD):

    def __init__(self, subExpressionLeft, subExpressionRight):
        """
        Constructeur de l'opérateur Join
        - subExpressionLeft = une relation ou un SPJRUD
        - subExpressionRight = une relation ou un SPJRUD

        >> Join(Relation, Relation)
        """
        if isinstance(subExpressionLeft, Relation):
            rel = subExpressionLeft
            self.SPJRUD1 = False
        elif isinstance(subExpressionLeft, SPJRUD):
            rel = subExpressionLeft.get_NewRelation()
            self.SPJRUD1 = True
        else:
            raise Exception("SPJRUD -> Join : Le premier parametre doit etre du type \'Relation\' ou etre un operateur SPJRUD")

        if isinstance(subExpressionRight, Relation):
            rel2 = subExpressionRight
            self.SPJRUD2 = False
        elif isinstance(subExpressionRight, SPJRUD):
            rel2 = subExpressionRight.get_NewRelation()
            self.SPJRUD2 = True
        else:
            raise Exception("SPJRUD -> Join : Le second parametre doit etre du type \'Relation\' ou etre un operateur SPJRUD")

        valid_Join(rel, rel2)

        self.firstRelation = rel
        self.secondRelation = rel2

        self.set_NewRelation()
        self.AttributeInCommon()
        self.set_SQL()

    def __str__(self):
        """
        Méthode qui retourne l'opérateur sous forme d'une chaine de caractère
        """
        if not self.SPJRUD1 and not self.SPJRUD2:
            return "Join(Relation('" + self.firstRelation.__str__() + "'), Relation('" + self.secondRelation.__str__() + "'))"
        if self.SPJRUD1 and not self.SPJRUD2:
            return "Join(" + self.firstRelation.__str__() + ", Relation('" + self.secondRelation.__str__() + "'))"
        if not self.SPJRUD1 and self.SPJRUD2:
            return "Join(Relation('" + self.firstRelation.__str__() + "'), " + self.secondRelation.__str__() + ")"
        if self.SPJRUD1 and self.SPJRUD2:
            return "Join(" + self.firstRelation.__str__() + ", " + self.secondRelation.__str__() + ")"

    def set_NewRelation(self):
        """
        Crée une nouvelle relation apres avoir effectuer l'opérateur Join
        """
        attributes = []

        for att in self.firstRelation.get_Attributes():
            attributes.append(att)

        for att in self.secondRelation.get_Attributes():
            if att not in attributes:
                attributes.append(att)

        self.newRelation = Relation(self.firstRelation.get_Name(), attributes, SPJRUD=self.__str__())

    def get_NewRelation(self):
        """
        Retourne la nouvelle relation
        """
        return self.newRelation

    def AttributeInCommon(self):
        """
        Enregistre les atributs en communs de la jointure
        """
        self.attributeInCommon = []

        for att in self.secondRelation.get_Attributes():
            for att2 in self.firstRelation.get_Attributes():
                if att.get_Name() == att2.get_Name():
                    self.attributeInCommon.append(att)

    def set_SQL(self):
        """
        Enregistre la requête SQL dans la nouvelle relation
        """
        element = []

        for elem in self.attributeInCommon:
            element.append(self.firstRelation.get_Name() + "." + elem.get_Name() + " = " + self.secondRelation.get_Name() + "." + elem.get_Name())

        sql = "SELECT * FROM (" + self.firstRelation.get_SQL() + ") NATURAL JOIN (" + self.secondRelation.get_SQL() + ")"

        self.newRelation.set_SQL(sql)

    def get_SQL(self):
        """
        Retourne la requête SQL de la nouvelle relation
        """
        return self.newRelation.get_SQL()