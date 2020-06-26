from Caja import Caja

class Evento:
    """
    Clase que representa un evento
    """
    def __init__(self, tipo, reloj_inicio, caja, cliente):
        self.tipo = tipo
        self.inicio = reloj_inicio
        self.caja = caja
        self.cliente = cliente

    def __str__(self):
        return "Tipo:{0}-Va Iniciar en {1}".format(self.tipo,self.inicio)

    def __gt__(self, evento):
        return self.inicio > evento.inicio

    def asignar_caja(self, caja):
        self.caja = caja

    def get_caja(self):
        return self.caja

    def asignar_cliente(self, cliente):
        self.cliente = cliente

    def get_cliente(self):
        return self.cliente