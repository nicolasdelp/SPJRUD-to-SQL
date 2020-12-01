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

    #si l'attribut de droite de l'égalité est un attribut, on vérifie si il est du type Attribute
    if isinstance(param1.get_AttributeRight(), Attribute):
        if param1.return_NameList()[1] not in names:
            raise Exception("L\'attribut de droite de l'egalite n\'existe pas dans la relation")

def valid_Project(param1, param2):
    pass