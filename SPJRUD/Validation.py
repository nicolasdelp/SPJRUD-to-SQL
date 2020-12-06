from SPJRUD.SPJRUD import SPJRUD
from Ope.Ope import Ope
from Ope.Equal import Equal
from Representation.Relation import Relation
from Representation.Attribute import Attribute
from Representation.Constante import Constante

import sys
sys.tracebacklimit = 0

def valid_Select(param1, param2):
    """
    Vérifications pour l'opérateur Select dans SPJRUD
    - param1 = une opération entre 2 termes (une égalité par exemple)
    - param2 = une relation
    """
    #on vérifie si le premier paramètre est du bon type
    if not isinstance(param1, Ope):
        raise Exception("SPJRUD -> Select : Le premier parametre doit etre du type \'Ope\'")

    #on vérifie si l'attribut de gauche de l'opération est dans la relation
    names = []
    for att in param2.get_Attributes():
        names.append(att.get_Name())
    
    if param1.return_NameList()[0] not in names:
        raise Exception("Operateur Equal : L\'attribut de gauche de l'egalite n\'existe pas dans la relation")

    if isinstance(param1.get_AttributeRight(), str): #quand ce n'est pas une constante
        if param1.return_NameList()[1] not in names: #on vérifie que l'argument existe dans la relation
            raise Exception("Operateur Equal : L\'attribut de droite de l'egalite n\'existe pas dans la relation")
        
        #on vérifie que les 2 attributs sont du même type
        attributes = []
        for att in param2.get_Attributes():
            if att.get_Name() in param1.return_NameList():
                attributes.append(att)
        
        if attributes[0].get_Type() != attributes[1].get_Type():
            raise Exception("SPJRUD -> Select : Le type des arguments n\'est pas compatible")
    
    if isinstance(param1.get_AttributeRight(), Constante): #quand c'est une constante
        if not isinstance(param1.get_AttributeRight().get_Value(), type(param1.get_AttributeLeft())):
            raise Exception("SPJRUD -> Select : Le type des arguments n\'est pas compatible")

  
def valid_Project(param1, param2):
    """
    Vérifications pour l'opérateur Project dans SPJRUD
    - param1 = une liste de paramètres (string) à projeter
    - param2 = une relation
    """
    #on vérifie si le premier parametre est du bon type
    if not isinstance(param1, list):
        raise Exception("SPJRUD -> Project : Le premier parametre doit etre du type \'list\'")

    #on verifie si les attributs de la liste sont bien dans la relation
    names = []
    for att in param2.get_Attributes():
        names.append(att.get_Name())

    for param in param1:
        if param not in names:
            raise Exception("SPJRUD -> Project : Un parametre de la liste n\'existe pas dans la relation")

def valid_Join(param1, param2):
    """
    Vérifications pour l'opérateur Join dans SPJRUD
    - param1 = une relation
    - param2 = une relation
    """
    #on vérifie si il existe au moins 1 attribut en commun dans les 2 relations
    attributes = []
    inTheList = 0

    for att in param1.get_Attributes():
        attributes.append(att.get_Name())
    
    for att in param2.get_Attributes():
        if att.get_Name() in attributes:
            inTheList += 1
    
    if inTheList == 0:
        raise Exception("SPJRUD -> Join : La jointure est impossible, aucun attribut n\'est dans les deux relations")

    #on vérifie si les attributs à joindre sont du même type
    toCheck = param1.get_Attributes()

    for att in toCheck:
        for att2 in toCheck:
            if att.get_Name() == att2.get_Name():
                if att.get_Type() != att2.get_Type():
                    raise Exception("SPJRUD -> Join : La jointure est impossible, les attributs ne sont pas du meme type")

def valid_Rename(param1, param2, param3):
    """
    Vérifications pour l'opérateur Select dans SPJRUD
    - param1 = l'ancien nom d'attribut
    - param2 = le nouveau nom d'attribut
    - param3 = une relation
    """
    #on vérifie si les deux paramètres sont du bon type
    if not isinstance(param1, str):
        raise Exception("SPJRUD -> Rename : Le premier parametre doit etre du type \'str\'")
    if not isinstance(param2, str):
        raise Exception("SPJRUD -> Rename : Le second parametre doit etre du type \'str\'")

    #on vérifie si l'attribut à renomer est dans la relation
    names = []
    for att in param3.get_Attributes():
        names.append(att.get_Name())
    
    if param1 not in names:
        raise Exception("SPJRUD -> Rename : Cet attribut n\'existe pas dans la relation")

def valid_Union(param1, param2):
    """
    Vérifications pour l'opérateur Union dans SPJRUD
    - param1 = une relation
    - param2 = une relation
    """
    #on vérifie si la jointure est possible
    attributes = []
    for att in param1.get_Attributes():
        attributes.append(att.get_Name())
    
    if len(param1.get_Attributes()) != len(param2.get_Attributes()):
        raise Exception("SPJRUD -> Union : Les deux relations n\'ont pas le meme nombre d\'attributs")
    
    for att in param2.get_Attributes():
        if att.get_Name() not in attributes:
            raise Exception("SPJRUD -> Union : Les attributs des relations ne sont pas les memes")
    
    #on vérifie si les attributs sont du même type
    toCheck = param1.get_Attributes()

    for att in toCheck:
        for att2 in toCheck:
            if att.get_Name() == att2.get_Name():
                if att.get_Type() != att2.get_Type():
                    raise Exception("SPJRUD -> Union : L\'union est impossible, les attributs ne sont pas du meme type")

def valid_Difference(param1, param2):
    """
    Vérifications pour l'opérateur Difference dans SPJRUD
    - param1 = une relation
    - param2 = une relation
    """
    #on vérifie si la difference est possible
    attributes = []
    for att in param1.get_Attributes():
        attributes.append(att.get_Name())
    
    if len(param1.get_Attributes()) != len(param2.get_Attributes()):
        raise Exception("SPJRUD -> Difference : Les deux relations n\'ont pas le meme nombre d\'attributs")
    
    for att in param2.get_Attributes():
        if att.get_Name() not in attributes:
            raise Exception("SPJRUD -> Difference : Les attributs des relations ne sont pas les memes")

    #on vérifie si les attributs sont du même type
    toCheck = param1.get_Attributes()

    for att in toCheck:
        for att2 in toCheck:
            if att.get_Name() == att2.get_Name():
                if att.get_Type() != att2.get_Type():
                    raise Exception("SPJRUD -> Difference : La difference est impossible, les attributs ne sont pas du meme type")