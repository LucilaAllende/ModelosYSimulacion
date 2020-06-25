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

def calcular_intervalo_confianza(coficienteZ, media, error):
    margenError = coficienteZ * error
    return media - margenError, media + margenError

def llegada_camiones():
    cantidad = randint(3,5)
    llegada = np.random.exponential(15, cantidad)
    return llegada

def generar_eventos_llegada():
    eventos = []
    for i in llegada_camiones():
        evento = Evento(LLEGADA_CAMION, int(i), None, None)
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

def procesar_evento(evento, reloj_simulacion, estacion, fel, tiempos_promedio_corrida):
    avanzar=0
    
    if evento.tipo == LLEGADA_CAMION :
        #si es un evento reprocesado
        if evento.get_camion():
            camion = evento.get_camion()
        else:
            camion = Camion(reloj_simulacion.valor, 0, 0)
            evento.asignar_camion(camion)

        surtidores_libres = estacion.verificar_surtidores_libres()
        
        if len(surtidores_libres):

            surtidor = surtidores_libres[0] 
            tiempo_atencion_surtidor = surtidor.tiempo_atencion()
            evento.asignar_surtidor(surtidor)
            surtidor.set_disponible(False)
            remover_evento_fel(fel, evento)
            avanzar=0
            generar_evento_fin_atencion(fel, reloj_simulacion.valor + tiempo_atencion_surtidor, surtidor, camion)
            #tomo el tiempo del evento de salida
            if (reloj_simulacion.get_valor_acumulado() > reloj_simulacion.valor):
                tiempo_espera_camion = reloj_simulacion.get_valor_acumulado() - evento.get_camion().get_tiempo_llegada()
            else:
                tiempo_espera_camion = 0
            evento.get_camion().set_tiempo_espera(tiempo_espera_camion)
            tiempos_promedio_corrida.append(tiempo_espera_camion)
        else:
            #reiniciamos la fel
            avanzar=1

    elif evento.tipo == FIN_ATENCION_CAMION :
        estacion.cantidad_camiones_atendidos+=1
        surtidor = evento.get_surtidor()
        surtidor.set_disponible(True)        
        remover_evento_fel(fel, evento)
        reloj_simulacion.acumular(reloj_simulacion.valor)   
    return avanzar

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
tiempo_promedio_total = 0
tiempo_promedio_espera_total = []
promedio_corrida = 0

for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):
        FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)
        reloj_simulacion = Reloj()
        estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_SURTIDORES)
        tiempos_promedio_corrida = []
        indice_fel=0

        while len(FEL)>0:
            evento_actual = FEL[indice_fel]
            cantidad_eventos = len(FEL)
            #print(len(FEL))

            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)
        
            #procesar el evento actual
            avanzar = procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL, tiempos_promedio_corrida)

            if avanzar==0:
                indice_fel=0
            elif avanzar == 1:
                indice_fel+=1
            
            if indice_fel>=len(FEL):
                if len(FEL) > 0: 
                    indice_fel = 0 
                else:
                    break 
                    
    promedio_corrida = np.mean(tiempos_promedio_corrida)
    tiempo_promedio_espera_total.append(promedio_corrida)

tiempo_promedio_total = np.mean(tiempo_promedio_espera_total)

n = len(tiempo_promedio_espera_total)
media = tiempo_promedio_total
desvio = np.std(tiempo_promedio_espera_total)*3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575

extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)

print(f"El tiempo promedio de espera de los camiones es de {media}")
print(f"El intervalo de confianza va de {extremoInferior} a {extremoSuperior}] con el 99% de confiabilidad")

sns_plot = sns.distplot(tiempo_promedio_espera_total)
fig = sns_plot.get_figure()
fig.savefig("Exponencial.png") 