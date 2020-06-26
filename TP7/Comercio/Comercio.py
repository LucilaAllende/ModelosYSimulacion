from Caja import Caja

class Comercio:
    """
    Clase que representa el Comercio
    """
    def __init__(self, horas_simulacion, cantidad_cajas):
        
        self.cajas = []
        for i in range(cantidad_cajas):
            self.cajas.append(Caja(horas_simulacion, i+1, 0))

        self.cantidad_clientes_atendidos=0

    def verificar_cajas_libres(self):
        libres = []
        for caja in self.cajas:
            estado = caja.estoy_libre()
            if estado == True:
               libres.append(caja)
        return libres
    
    def get_cajas(self):
        return self.cajas