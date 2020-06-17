import numpy as np
import seaborn as sns
import math
from random import randint

from Empleado import Empleado
from Surtidor import Surtidor
from EstacionDeServicio import EstacionDeServicio
from Reloj import Reloj
from Evento import Evento

def llegada_camiones():
    cantidad = randint(3,5)
    llegada = np.random.exponential(1/15, cantidad)
    #print (llegada)
    return llegada

def generar_eventos_llegada():
    eventos = []
    for i in llegada_camiones():
        evento = Evento(LLEGADA_CAMION, i)
        eventos.append(evento)
    return eventos

def generar_FEL(horas_simulacion):
    fel = []
    for i in range(horas_simulacion):
        eventos_llegada = generar_eventos_llegada()
        fel+=eventos_llegada
    print(len(fel))
    for evento in fel:
        print(evento)
    
    sorted(fel)
    #sorted(fel, key=lambda evento: evento.inicio)
    
    print("Ordenado")
    for evento in fel:
        print(evento)

    evento1 = fel[0]
    evento2 = fel[1]
    print("e1")
    print(evento1)
    print("e2")
    print(evento2)
    return fel

def tomar_proximo_evento(fel):
    if (len(fel) > 0):
        proximo_evento = fel[0]
        fel.remove(proximo_evento)
        return proximo_evento
    else:
        return None


def procesar_evento(evento, reloj_simulacion, estacion, fel):

    if evento.tipo == LLEGADA_CAMION :
        surtidores = estacion.verificar_surtidores_libres()
        if len(surtidores):

    else:
        return None

#Esta funcion no va mas
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

CANTIDAD_HORAS_LABORABLES=24
CANTIDAD_MINUTOS_LABORABLES = (CANTIDAD_HORAS_LABORABLES*60) #24 hs * 60 minutos laborables
CANTIDAD_EMPLEADOS=4
CANTIDAD_SURTIDORES=4


#eventos
LLEGADA_CAMION = 1
ATENCION_CAMION = 2
FIN_ATENCION_CAMION = 3
SALIDA_CAMION = 4


#variables
duraciones_atenciones = []
promedio_total_experimentos = []

reloj_simulacion = Reloj()
estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_EMPLEADOS,CANTIDAD_SURTIDORES)
FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)

for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):

        evento_actual = tomar_proximo_evento(FEL)

        if evento_actual:
            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)

            #procesar el evento actual
            procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL)
        
        duracion_atencion = 0
       
        #Acumulo la duracion de la atencion actual
        duracion_experimento += duracion_atencion

        #Agrego la duracion de la atencion actual a la lista de duraciones de todas las atenciones
        duraciones_atenciones.append(duracion_atencion)

    promedio_total_experimentos.append(duracion_experimento/MAX_CORRIDAS)



