import numpy as np

class Surtidor:
    """
    Clase que representa al surtidor
    """
    
    def __init__(self, horas, empleado, ocupacion):
        self.disponible = True
        self.horas = horas
        self.empleado = empleado
        self.ocupacion = ocupacion

    def estoy_libre(self):
        return self.disponible

    def set_disponible(self, valor):
        self.disponible = valor

    #genero tiempos de atencion
    def tiempo_atencion(self):
        tiempo_atencion = 0
        if self.empleado == 1:
            tiempo_atencion=int(np.random.normal(18,4,1))
        elif self.empleado == 2:
            tiempo_atencion=int(np.random.exponential(scale=15,size=1))
        elif self.empleado == 3:
            tiempo_atencion=int(np.random.exponential(scale=16, size=1))
        elif self.empleado == 4:
            tiempo_atencion=int(np.random.normal(18, 3, 1))
        else:
            tiempo_atencion=int(np.random.normal(19, 5, 1))
        
        return tiempo_atencion

    def set_ocupacion(self, tiempo):
        self.ocupacion = self.ocupacion + tiempo

    def __str__(self):
        return "Tiempo de atencion:{0}".format(self.empleado)