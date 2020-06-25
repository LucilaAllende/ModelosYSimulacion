class Reloj:
    """
    Clase que representa un reloj
    """
    def __init__(self):
        self.valor = 0 #en minutos
        self.valor_acumulado = 0

    def avanzar(self, nuevo_valor):
        self.valor = nuevo_valor
    
    def acumular(self, valor):
        self.valor_acumulado=valor

    def get_valor_acumulado(self):
        return self.valor_acumulado