from Surtidor import Surtidor

class EstacionDeServicio:
    """
    Clase que representa la Estacion De Servicio
    """
    def __init__(self, horas_simulacion, cantidad_surtidores):
        
        self.surtidores = []
        for i in range(cantidad_surtidores):
            self.surtidores.append(Surtidor(horas_simulacion, i+1, 0))

        self.cantidad_camiones_atendidos=0

    def verificar_surtidores_libres(self):
        libres = []
        for surtidor in self.surtidores:
            estado = surtidor.estoy_libre()
            if estado == True:
               libres.append(surtidor)
        return libres
    
    def get_surtidores(self):
        return self.surtidores