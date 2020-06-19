class Camion:
    """
    Clase que representa a un camión
    """
    
    def __init__(self, tiempo_llegada, tiempo_salida, tiempo_espera):
        self.llegada = tiempo_llegada
        self.espera = tiempo_espera
        self.salida = tiempo_salida
    
    def get_tiempo_llegada(self):
        return self.llegada

    def set_tiempo_salida(self, salida):
        self.salida = salida
    
    def set_tiempo_espera(self, espera):
        self.espera = espera

    def get_tiempo_espera(self):
        return self.espera
    