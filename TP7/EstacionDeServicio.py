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

        self.cantidad_vehiculos_atendidos=0