class Constante: #représente une constante
    
    def __init__(self, value):
        self.set_Value(value)

    def set_Value(self, value):
        self.value = value

    def get_Value(self):
        return self.value