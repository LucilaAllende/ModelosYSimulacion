import numpy as np
import seaborn as sns
import math

from Empleado import Empleado
from Surtidor import Surtidor
from EstacionDeServicio import EstacionDeServicio

def inicializacion():
    #genero tiempos de atencion
    atencion_empleado1 = np.random.normal(18,4,1)
    atencion_empleado2 = np.random.exponential(scale=1/15,size=1)
    atencion_empleado3 = np.random.exponential(scale=1/16, size=1)
    atencion_empleado4 = np.random.normal(18, 3, 1)

    print(atencion_empleado1)

    return atencion_empleado1, atencion_empleado2, atencion_empleado3, atencion_empleado4


#constantes
MAX_EXPERIMENTOS=60
MAX_CORRIDAS=100
CANTIDAD_HORAS=24
CANTIDAD_EMPLEADOS=4
CANTIDAD_SURTIDORES=4


#variables
surtidores=[]
duraciones_atenciones = []
promedio_total_experimentos = []
FEL=[]

for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):
       
        inicializacion()
        
        duracion_atencion = 0
       
        #Acumulo la duracion de la atencion actual
        duracion_experimento += duracion_atencion

        #Agrego la duracion de la atencion actual a la lista de duraciones de todas las atenciones
        duraciones_atenciones.append(duracion_atencion)

    promedio_total_experimentos.append(duracion_experimento/MAX_CORRIDAS)



