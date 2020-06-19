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

def procesar_evento(evento, reloj_simulacion, estacion, fel, cola):
    if evento.tipo == LLEGADA_CAMION :
        print("SOy llegada. Reloj")
        print(reloj_simulacion.valor)

        #si es un evento reprocesado
        if evento.get_camion():
            camion = evento.get_camion()
            print("Ya fui procesado")
        else:
            camion = Camion(reloj_simulacion.valor, 0, 0)

        surtidores_libres = estacion.verificar_surtidores_libres()
        if len(surtidores_libres):
            camion.set_tiempo_espera(reloj_simulacion.valor-camion.llegada)
            surtidor = surtidores_libres[0] 
            tiempo_atencion_surtidor = surtidor.tiempo_atencion()
            evento.asignar_surtidor(surtidor)
            surtidor.set_disponible(False)
            print("ATENCION SURTIDOR-----")
            print(tiempo_atencion_surtidor)
            remover_evento_fel(fel, evento)
            generar_evento_fin_atencion(fel, reloj_simulacion.valor + tiempo_atencion_surtidor, surtidor, camion)
        else:
            print("NO hay s libres")
            cola.append(camion)

    elif evento.tipo == FIN_ATENCION_CAMION :
        print("SOy fin. Reloj")
        quitar_camion_cola(cola, evento.get_camion())
        estacion.cantidad_camiones_atendidos+=1
        surtidor = evento.get_surtidor()
        surtidor.set_disponible(True)        
        remover_evento_fel(fel, evento)
        print("BOrre un evento")
    
    return None 

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


estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_SURTIDORES)


cola_camiones = []
bandera = 0 #1 significa reiniciar
corte = True

for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):
        FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)
        reloj_simulacion = Reloj()
        indice_fel=0
        for evento in FEL:
            print(evento)
        while len(FEL)>0:
            evento_actual = FEL[indice_fel]
            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)
            print("Reloj")
            print(reloj_simulacion.valor)
            print("Cantidad eventos")
            print(len(FEL))
            print("Procesar")
            print(evento_actual)
            print("Indice antes")
            print(indice_fel)

        
            #procesar el evento actual
            procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL, cola_camiones)

            print("Indice despues procesar")
            print(indice_fel)
            indice_fel+=1

            print("Indice despues incre")
            print(indice_fel)
            if indice_fel>=len(FEL):
                if indice_fel>0:
                    indice_fel=0
                else:
                    break

