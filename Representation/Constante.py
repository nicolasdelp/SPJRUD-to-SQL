__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

class Constante:
    
    def __init__(self, value):
        """
        Constructeur d'une constante
        - value = le valeur de la constante

        >> Constante(1234876)
        >> Constante(3.14)
        >> Constante("Nicolas")
        """
        self.set_Value(value)

    def set_Value(self, value):
        """
        Enregistre la valeur de la constante
        - value = le valeur de la constante
        """
        self.value = value

    def get_Value(self):
        """
        Retourne la valeur de la constante
        """
        return self.value