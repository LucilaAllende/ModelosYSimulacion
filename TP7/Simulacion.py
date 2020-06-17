import numpy as np
import seaborn as sns
import math

from Empleado import Empleado
from Surtidor import Surtidor
from EstacionDeServicio import EstacionDeServicio
from Reloj import Reloj

def generar_FEL(horas_simulacion):
    fel = []
    for hora in range(horas_simulacion):
        camiones= np.random.exponential(1/CAMIONES_POR_HORA)
        print(camiones)
    return fel

def inicializacion():
    #genero tiempos de atencion
    atencion_empleado1 = np.random.normal(18,4,1)
    atencion_empleado2 = np.random.exponential(scale=1/15,size=1)
    atencion_empleado3 = np.random.exponential(scale=1/16, size=1)
    atencion_empleado4 = np.random.normal(18, 3, 1)

    return atencion_empleado1, atencion_empleado2, atencion_empleado3, atencion_empleado4


#constantes
MAX_EXPERIMENTOS=60
MAX_CORRIDAS=100

CANTIDAD_HORAS=24
CANTIDAD_MINUTOS_HORA = (24*60) #24 hs * 60 minutos laborables
CANTIDAD_EMPLEADOS=4
CANTIDAD_SURTIDORES=4

CAMIONES_POR_HORA=15


#variables
duraciones_atenciones = []
promedio_total_experimentos = []


horas_transcurridas = 0
reloj_simulacion = Reloj()
estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS,CANTIDAD_EMPLEADOS,CANTIDAD_SURTIDORES)
FEL=generar_FEL(CANTIDAD_HORAS)

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



