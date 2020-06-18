from Surtidor import Surtidor

class Evento:
    """
    Clase que representa un evento
    """
    def __init__(self, tipo, reloj_inicio, surtidor,camion):
        self.tipo = tipo
        self.inicio = reloj_inicio
        self.surtidor = surtidor
        self.camion = camion

    def __str__(self):
        return "Tipo:{0}-Va Iniciar en {1}".format(self.tipo,self.inicio)

    def __gt__(self, evento):
        return self.inicio > evento.inicio

    def asignar_surtidor(self, surtidor):
        self.surtidor = surtidor

    def get_surtidor(self):
        return self.surtidor

    def asignar_camion(self, camion):
        self.camion = camion

    def get_camion(self):
        return self.camion


