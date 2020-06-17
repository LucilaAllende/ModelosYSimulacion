from Empleado import Empleado
from Surtidor import Surtidor

class EstacionDeServicio:
    """
    Clase que representa la Estacion De Servicio
    """
    def __init__(self, horas_simulacion, cantidad_empleados, cantidad_surtidores):

        self.empleados = []
        for i in range(cantidad_empleados):
            self.empleados.append(Empleado(horas_simulacion))
        
        self.surtidores = []
        for i in range(cantidad_surtidores):
            self.surtidores.append(Surtidor(horas_simulacion))

        self.cantidad_camiones_atendidos=0

    def verificar_surtidores_libres(self):
        libres = []
        for surtidor in self.surtidores:
            estado = surtidor.estoy_libre()
            if estado == True:
               libres+=surtidor
        return libres