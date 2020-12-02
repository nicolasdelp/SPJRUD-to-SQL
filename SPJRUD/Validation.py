from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute

def valid_Select(param1, param2):
    """
    Vérifications pour l'opérateur Select dans SPJRUD
    - param1 = une opération entre 2 termes (une égalité par exemple)
    - param2 = une relation
    """
    #on vérifie si les deux paramètres sont du bon type
    if not isinstance(param1, Ope):
        raise Exception("Le premier parametre doit etre du type \'Ope\'")

    if not isinstance(param2, Relation):
        raise Exception("Le second parametre doit etre du type \'Relation\'")

    #on vérifie si l'attribut de gauche de l'opération est dans la relation
    names = []
    for att in param2.get_Attributes():
        names.append(att.get_Name())
    
    if param1.return_NameList()[0] not in names:
        raise Exception("L\'attribut de gauche de l'egalite n\'existe pas dans la relation")

def valid_Project(param1, param2):
    """
    Vérifications pour l'opérateur Project dans SPJRUD
    - param1 = une liste de paramètres (string) à projeter
    - param2 = une relation
    """
    #on vérifie si les deux paramètres sont du bon type
    if not isinstance(param1, list):
        raise Exception("Le premier parametre doit etre du type \'list\'")

    if not isinstance(param2, Relation):
        raise Exception("Le second parametre doit etre du type \'Relation\'")
    
    #on verifie si les attributs de la liste sont bien dans la relation
    names = []
    for att in param2.get_Attributes():
        names.append(att.get_Name())

    for param in param1:
        if param not in names:
            raise Exception("Un parametre de la liste n\'existe pas dans la relation")

def valid_Join(param1, param2):
    """
    Vérifications pour l'opérateur Join dans SPJRUD
    - param1 = une relation
    - param2 = une relation
    """
    #on vérifie si les deux paramètres sont du bon type
    if not isinstance(param1, Relation):
            raise Exception("Le premier parametre doit etre du type \'Relation\'")
    if not isinstance(param2, Relation):
        raise Exception("Le second parametre doit etre du type \'Relation\'")

    #on vérifie si il existe au moins 1 attribut en commun dans les 2 relations
    attributes = []
    inTheList = 0

    for att in param1.get_Attributes():
        attributes.append(att.get_Name())
    
    for att in param2.get_Attributes():
        if att.get_Name() in attributes:
            inTheList += 1
    
    if inTheList == 0:
        raise Exception("La jointure est impossible, aucun attribut n\'est dans les deux relations")

def valid_Rename(param1, param2, param3):
    """
    Vérifications pour l'opérateur Select dans SPJRUD
    - param1 = l'ancien nom d'attribut
    - param2 = le nouveau nom d'attribut
    - param3 = une relation
    """
    #on vérifie si les deux paramètres sont du bon type
    if not isinstance(param1, str):
        raise Exception("Le premier parametre doit etre du type \'str\'")
    if not isinstance(param2, str):
        raise Exception("Le second parametre doit etre du type \'str\'")
    if not isinstance(param3, Relation):
        raise Exception("Le dernier parametre doit etre du type \'Relation\'")

    #on vérifie si l'attribut à renomer est dans la relation
    names = []
    for att in param3.get_Attributes():
        names.append(att.get_Name())
    
    if param1 not in names:
        raise Exception("Cet attribut n\'existe pas dans la relation")