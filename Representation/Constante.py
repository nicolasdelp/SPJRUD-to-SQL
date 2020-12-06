__author__ = "Nicolas Delplanque"
__credits__ = ["Nicolas Delplanque"]
__version__ = "1.0.1"
__maintainer__ = "Nicolas Delplanque"
__email__ = "nicolas.delplanque@student.umons.ac.be"

class Constante: #représente une constante
    
    def __init__(self, value):
        self.set_Value(value)

    def set_Value(self, value):
        self.value = value

    def get_Value(self):
        return self.value