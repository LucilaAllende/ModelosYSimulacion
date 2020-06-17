class Surtidor:
    """
    Clase que representa al surtidor
    """
    
    def __init__(self,horas):
        self.disponible = True
        self.horas = horas

    def estoy_libre(self):
        return self.disponible
