class Surtidor:
    """
    Clase que representa al surtidor
    """
    
    def __init__(self,horas):
        self.disponible = True
        self.horas = horas

    def get_disponible(self):
    	return self.disponible

    def set_disponible(self, disponibilidad):
    	self.disponible = disponibilidad
