from SPJRUD.SPJRUD import SPJRUD
from Representation.Relation import Relation
from Representation.Attribute import Attribute

class Project(SPJRUD):

    def __init__(self, listOfParameters, subExpressionRight):
        if not isinstance(listOfParameters, list):
            raise Exception("Le premier parametre doit etre du type \'list\'")

        if not isinstance(subExpressionRight, Relation):
            raise Exception("Le deuxieme parametre doit etre du type \'Relation\'")
        
        self.listOfParameters = listOfParameters #liste retourné par l'égalitée
        self.subExpressionRight = subExpressionRight #relation sur laquelle on doit travailler

        for param in listOfParameters: #verifie si les attributs de la liste sont bien dans la relation
            self.check_Expression(param, subExpressionRight)
        
        self.set_SQL()

    def check_Expression(self, attributeName, relation): 
        names = []
        for att in relation.get_Attributes():
            names.append(att.get_Name())
        
        if attributeName not in names:
            raise Exception("Cet attribut n\'existe pas dans la relation")

    def get_Relation(self): #retourne la relation qui a été "modifié"
        return self.subExpressionRight

    def set_SQL(self):
        res = "SELECT " + ",".join(self.listOfParameters) + " FROM (" + self.subExpressionRight.get_SQL() + ")"
        self.subExpressionRight.set_SQL(res)
    
    def print_SQL(self): #affiche à la console la requette SQL
        res = self.get_Relation()
        print(res.get_SQL())