class Reloj:
    """
    Clase que representa un reloj
    """
    def __init__(self):
        self.valor = 0 #en minutos

    def avanzar(self, nuevo_valor):
        self.valor += nuevo_valor