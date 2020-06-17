class Evento:
    """
    Clase que representa un evento
    """
    def __init__(self, tipo, reloj_inicio):
        self.tipo = tipo
        self.inicio = reloj_inicio

    def __str__(self):
        return "Tipo:{0}-Va Iniciar en {1}".format(self.tipo,self.inicio)

    def __gt__(self, evento):
        return self.inicio > evento.inicio


