from time import sleep

class Fase:
    def __init__(self, id, duracion):
        '''
        Constructor: id->identifica a la fase duracion->el tiempo que dura la fase
        '''
        self.id = id
        self.duracion = duracion
    
    def descontar_experiencia(self, empleados):
        for emple in empleados:
            if(self.id == emple.id):
                self.duracion = self.duracion - emple.experiencia
                cadena = "Pero la fase " + str(self.id) + " con la experiencia del empleado " + str(emple.id) + " dura: " + str(self.duracion) + " minutos"
                print(cadena)

    def aumentar_vehiculo(self, vehiculo):
        print("Ademas el tiempo varia de acuerdo al tipo de vehiculo")
        self.duracion = self.duracion + ((self.duracion*vehiculo)/100)
        cadena = "La fase " + str(self.id) + " para el tipo de vehiculo ingresado dura: " + str(self.duracion)
        print(cadena)

    def realizar(self, empleados, vehiculo):

        self.descontar_experiencia(empleados) 
        self.aumentar_vehiculo(vehiculo)       
        #sleep(self.duracion)
        return self.duracion
    
    def __str__(self):
        cadena = "La fase " + str(self.id) + " deberia durar: " + str(self.duracion) + " minutos"
        return cadena

class Empleado:
    def __init__(self, id, experiencia):
        self.id = id
        self.experiencia = experiencia
    
    def __str__(self):
        cadena = "El empleado" + str(self.id) + " tiene " + str(self.experiencia) + " de experiencia"
        return cadena

class Lavado:
    def __init__(self, tiempos_fases, experiencia_empleados, ajuste_vehiculo):
        self.fases = [Fase(id, duracion) for id, duracion in enumerate(tiempos_fases)]
        self.empleados = [Empleado(id, experiencia) for id, experiencia in enumerate(experiencia_empleados)]
        self.vehiculo = ajuste_vehiculo

    def lavar(self):

        duracion_total = 0
        for fase in self.fases:
            print(fase)
            duracion_total += fase.realizar(self.empleados, self.vehiculo)

        print("Vehiculo lavado - duración total:", duracion_total)
        self.detectarfaselenta()

    def detectarfaselenta(self):
        fase_lenta = max(self.fases, key=lambda d: d.duracion)
        cadena = "La fase " + str(fase_lenta.id) + " es la mas lenta con una duracion de: " + str(fase_lenta.duracion) + " minutos"
        print(cadena)


lavado = Lavado([15,10,10,10,5,10], [4,3,2,1,1,1], 10 )
lavado.lavar()
