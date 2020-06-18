class Camion:
    """
    Clase que representa a un camión
    """
    
    def __init__(self, tiempo_llegada, tiempo_salida):
        self.llegada = tiempo_llegada
        self.salida = tiempo_salida
    
    def get_tiempo_llegada(self):
        return self.llegada

    def set_tiempo_salida(self, salida):
        self.salida = salida
    
    