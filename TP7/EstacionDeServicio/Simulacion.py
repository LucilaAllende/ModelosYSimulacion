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
    llegada = np.random.exponential(15, 1)
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
    return None

def quitar_camion_cola(cola, camion):
    if camion in cola:
        cola.remove(camion)

def tomar_proximo_evento(fel, evento):
    if evento in fel:
        return evento
    else:
        return None

def incrementar_tiempo_espera(tiempo,cola):  
    for camion in cola:
        camion.set_tiempo_espera(tiempo-camion.get_tiempo_llegada())

def procesar_evento(evento, reloj_simulacion, estacion, fel, cola):
    avanzar=0
    if evento.get_camion():
        camion_cola = evento.get_camion()
        if not camion_cola in cola:
            incrementar_tiempo_espera(reloj_simulacion.valor, cola)
    
    if evento.tipo == LLEGADA_CAMION :
        print("Soy llegada. Reloj:")
        print(reloj_simulacion.valor)

        #si es un evento reprocesado
        if evento.get_camion():
            camion = evento.get_camion()
            print("Ya fui procesado")
        else:
            camion = Camion(reloj_simulacion.valor, 0, 0)
            evento.asignar_camion(camion)
            print("CAMION CREADO")

        surtidores_libres = estacion.verificar_surtidores_libres()
        if len(surtidores_libres):
            #camion.set_tiempo_espera(reloj_simulacion.valor-camion.llegada)
            print("Tiempo de espera")
            print(camion.espera)
            surtidor = surtidores_libres[0] 
            tiempo_atencion_surtidor = surtidor.tiempo_atencion()
            evento.asignar_surtidor(surtidor)
            surtidor.set_disponible(False)
            remover_evento_fel(fel, evento)
            avanzar=0
            generar_evento_fin_atencion(fel, reloj_simulacion.valor + tiempo_atencion_surtidor, surtidor, camion)
        else:
            print("NO hay s libres")
            cola.append(camion)
            avanzar=1

    elif evento.tipo == FIN_ATENCION_CAMION :
        print("SOy fin. Reloj")
        print(reloj_simulacion.valor)
        quitar_camion_cola(cola, evento.get_camion())
        estacion.cantidad_camiones_atendidos+=1
        surtidor = evento.get_surtidor()
        surtidor.set_disponible(True)        
        remover_evento_fel(fel, evento)
        print("BOrre un evento")
    
    return avanzar 

#constantes
MAX_EXPERIMENTOS=1
MAX_CORRIDAS=1

CANTIDAD_HORAS_LABORABLES=10
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

for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):
        FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)
        reloj_simulacion = Reloj()
        estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_SURTIDORES)
        cola_camiones = []
        indice_fel=0
        for evento in FEL:
            print(evento)
        while len(FEL)>0:
            evento_actual = FEL[indice_fel]
            cantidad_eventos = len(FEL)
            print(cantidad_eventos)
            for evento in FEL:
                print(evento)
            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)
        
            #procesar el evento actual
            avanzar = procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL, cola_camiones)

            if avanzar==0:
                indice_fel=0
            elif avanzar == 1:
                indice_fel+=1
            
            if indice_fel>=len(FEL):
                if len(FEL) > 0: 
                    indice_fel = 0 
                else:
                    break 