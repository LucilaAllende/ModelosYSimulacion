class Reloj:
    """
    Clase que representa un reloj
    """
    def __init__(self):
        self.valor = 0 #en minutos

    def avanzar(self, nuevo_valor):
        self.valor = nuevo_valor


                    #cuando el indice sea mayor a la longitud de la lista, corto. 
            # Y esto se cumple lo probe, anduvo 20 veces y de repente dejo de andar