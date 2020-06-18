import numpy as np
import seaborn as sns
import math
from random import randint
import bisect

from Surtidor import Surtidor
from EstacionDeServicio import EstacionDeServicio
from Reloj import Reloj
from Evento import Evento
from Camion import Camion

def llegada_camiones():
    cantidad = randint(3,5)
    llegada = np.random.exponential(15, cantidad)
    #print (llegada)
    return llegada

def generar_eventos_llegada():
    eventos = []
    for i in llegada_camiones():
        evento = Evento(LLEGADA_CAMION, i, None, None)
        eventos.append(evento)
    return eventos

def fin_atencion(fel, nuevo_evento):
    bisect.insort(fel, nuevo_evento)
    return None

def generar_evento_fin_atencion(fel, inicio_evento, surtidor, camion):
    evento = Evento(FIN_ATENCION_CAMION,inicio_evento, surtidor,camion)
    fin_atencion(fel, evento)
    return None

def generar_FEL(horas_simulacion):
    fel = []
    for i in range(horas_simulacion):
        eventos_llegada = generar_eventos_llegada()
        fel+=eventos_llegada
    
    fel= sorted(fel)
    #sorted(fel, key=lambda evento: evento.inicio)
    print(len(fel))
    #for evento in fel:
        #print(evento)
    return fel

def remover_evento_fel(fel,evento):
    if evento in fel:
        fel.remove(evento)

def quitar_camion_cola(cola, camion):
    if camion in cola:
        cola.remove(camion)

def tomar_proximo_evento(fel, evento):
    if evento in fel:
        return evento
    else:
        return None

def procesar_evento(evento, reloj_simulacion, estacion, fel, cola):
    bandera=0
    if evento.tipo == LLEGADA_CAMION :
        #si es un evento reprocesado
        if evento.get_camion():
            camion = evento.get_camion()
        else:
            camion = Camion(reloj_simulacion.valor, 0, 0)

        surtidores_libres = estacion.verificar_surtidores_libres()
        if len(surtidores_libres):
            camion.set_tiempo_espera(reloj_simulacion.valor-camion.llegada)
            surtidor = surtidores_libres[0] 
            tiempo_atencion_surtidor = surtidor.tiempo_atencion()
            evento.asignar_surtidor(surtidor)
            surtidor.set_disponible(False)
            #print(tiempo_atencion_surtidor)
            remover_evento_fel(fel, evento)
            generar_evento_fin_atencion(fel, reloj_simulacion.valor + tiempo_atencion_surtidor, surtidor, camion)
        else:
            cola.append(camion)

    elif evento.tipo == FIN_ATENCION_CAMION :
        quitar_camion_cola(cola, evento.get_camion())
        estacion.cantidad_camiones_atendidos+=1
        surtidor = evento.get_surtidor()
        surtidor.set_disponible(True)
        remover_evento_fel(fel, evento)
        bandera=1
    
    return bandera 

#constantes
MAX_EXPERIMENTOS=60
MAX_CORRIDAS=100

CANTIDAD_HORAS_LABORABLES=24
CANTIDAD_MINUTOS_LABORABLES = (CANTIDAD_HORAS_LABORABLES*60) #24 hs * 60 minutos laborables
CANTIDAD_SURTIDORES=4

#eventos
LLEGADA_CAMION = 1
ATENCION_CAMION = 2
FIN_ATENCION_CAMION = 3
SALIDA_CAMION = 4

#variables
promedio_total_experimentos = []
tiempo_promedio_espera = 0

reloj_simulacion = Reloj()
estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_SURTIDORES)
FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)

cola_camiones = []
bandera = 0 #1 significa reiniciar
corte = True

while corte:
    for evento_actual in FEL:
        cantidad_eventos = len(FEL)
        print(cantidad_eventos)
        print("Procesar")
        print(evento_actual)
        if evento_actual:
            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)

            #procesar el evento actual
            bandera= procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL, cola_camiones)

        ultimo_evento = FEL[cantidad_eventos-1]
        if evento_actual == ultimo_evento:
            corte=False

        if bandera==1:
            break