import numpy as np
import seaborn as sns
import math
from random import randint
import bisect

from Caja import Caja
from Comercio import Comercio
from Reloj import Reloj
from Evento import Evento
from Cliente import Cliente

'''Para calcular el intervalo de confianza'''
def calcular_intervalo_confianza(coficienteZ, media, error):
    margenError = coficienteZ * error
    return media - margenError, media + margenError


def llegada_clientes():
     #Como cada cliente llega aprox cada 10 min, en una hora pueden llegar entre 5 y 7 clientes.
    cantidad = randint(5,7)
    llegada = np.random.exponential(10, cantidad)
    return llegada


def generar_eventos_llegada():
    eventos = []
    for i in llegada_clientes():
        evento = Evento(LLEGADA_CLIENTE, int(i), None, None)
        eventos.append(evento)
    return eventos


def fin_atencion(fel, nuevo_evento):
    bisect.insort(fel, nuevo_evento)
    return None


def generar_evento_fin_atencion(fel, inicio_evento, caja, cliente):
    evento = Evento(FIN_ATENCION_CLIENTE,inicio_evento, caja,cliente)
    fin_atencion(fel, evento)
    return None


def generar_FEL(horas_simulacion):
    fel = []
    for i in range(horas_simulacion):
        eventos_llegada = generar_eventos_llegada()
        fel+=eventos_llegada
    
    fel= sorted(fel)

    return fel


def remover_evento_fel(fel,evento):
    if evento in fel:
        fel.remove(evento)
    return None



def quitar_cliente_cola(cola, cliente):
    if cliente in cola:
        cola.remove(cliente)


def tomar_proximo_evento(fel, evento):
    if evento in fel:
        return evento
    else:
        return None



def procesar_evento(evento, reloj_simulacion, comercio, fel, tiempos_promedio_corrida):
    avanzar=0
    
    if evento.tipo == LLEGADA_CLIENTE :

        #si es un evento reprocesado
        if evento.get_cliente():
            cliente = evento.get_cliente()
        else:
            cliente = Cliente(reloj_simulacion.valor, 0, 0)
            evento.asignar_cliente(cliente)

        cajas_libres = comercio.verificar_cajas_libres()
        
        if len(cajas_libres):

            caja = cajas_libres[0] 
            tiempo_atencion_caja = caja.tiempo_atencion()
            evento.asignar_caja(caja)
            caja.set_disponible(False)
            remover_evento_fel(fel, evento)
            avanzar=0
            generar_evento_fin_atencion(fel, reloj_simulacion.valor + tiempo_atencion_caja, caja, cliente)

            #tomo el tiempo del evento de salida
            if (reloj_simulacion.get_valor_acumulado() > reloj_simulacion.valor):
                tiempo_espera_cliente = reloj_simulacion.get_valor_acumulado() - evento.get_cliente().get_tiempo_llegada()
            else:
                tiempo_espera_cliente = 0
            
            caja.set_ocupacion(tiempo_atencion_caja)
            evento.get_cliente().set_tiempo_espera(tiempo_espera_cliente)
            tiempos_promedio_corrida.append(tiempo_espera_cliente)
        else:
            #reiniciamos la fel
            avanzar=1

    elif evento.tipo == FIN_ATENCION_CLIENTE :
        comercio.cantidad_clientes_atendidos+=1
        caja = evento.get_caja()
        caja.set_disponible(True)        
        remover_evento_fel(fel, evento)
        reloj_simulacion.acumular(reloj_simulacion.valor)   
    return avanzar



def calcular_porcentaje(ocupacion):
	tiempo_simulado = MAX_CORRIDAS * MAX_EXPERIMENTOS * CANTIDAD_MINUTOS_LABORABLES
	porcentaje = (ocupacion / tiempo_simulado) * 100
	return np.round(porcentaje, 2) #para dejarle 2 decimales

#constantes
MAX_EXPERIMENTOS=5
MAX_CORRIDAS=365

CANTIDAD_HORAS_LABORABLES=12
CANTIDAD_MINUTOS_LABORABLES = (CANTIDAD_HORAS_LABORABLES*60) #12 hs * 60 minutos laborables
CANTIDAD_CAJAS=3

#eventos
LLEGADA_CLIENTE = 1
ATENCION_CLIENTE = 2
FIN_ATENCION_CLIENTE = 3
SALIDA_CLIENTE = 4


#variables
tiempo_promedio_total = 0
tiempo_promedio_espera_total = []
promedio_corrida = 0

#variables para calcular el % de ocupacion
ocupacion_caja1=0
ocupacion_caja2=0
ocupacion_caja3=0


for experimento in range(MAX_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(MAX_CORRIDAS):
        FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)
        reloj_simulacion = Reloj()
        comercio= Comercio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_CAJAS)
        tiempos_promedio_corrida = []
        indice_fel=0

        while len(FEL)>0:
            evento_actual = FEL[indice_fel]
            cantidad_eventos = len(FEL)

            #avanzo el reloj al tiempo del evento actual
            reloj_simulacion.avanzar(evento_actual.inicio)
        
            #procesar el evento actual
            avanzar = procesar_evento(evento_actual, reloj_simulacion, comercio, FEL, tiempos_promedio_corrida)

            if avanzar==0:
                indice_fel=0
            elif avanzar == 1:
                indice_fel+=1
            
            if indice_fel>=len(FEL):
                if len(FEL) > 0: 
                    indice_fel = 0 
                else:
                    break 

        cajas = comercio.get_cajas()
        for caja in cajas:
            if caja.empleado == 1:
                ocupacion_caja1 += caja.ocupacion
            elif caja.empleado == 2:
                ocupacion_caja2 += caja.ocupacion
            else:
                ocupacion_caja3+= caja.ocupacion

    promedio_corrida = np.mean(tiempos_promedio_corrida)
    tiempo_promedio_espera_total.append(promedio_corrida)


print(ocupacion_caja1)
print(ocupacion_caja2)
tiempo_promedio_total = np.mean(tiempo_promedio_espera_total)

porcentanje_1 = calcular_porcentaje(ocupacion_caja1)
porcentanje_2 = calcular_porcentaje(ocupacion_caja2)
porcentanje_3 = calcular_porcentaje(ocupacion_caja3)

n = len(tiempo_promedio_espera_total)
media = tiempo_promedio_total
desvio = np.std(tiempo_promedio_espera_total)*3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575


extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)

print(f"El tiempo promedio de espera de las cajas es de {media}")
print(f"El intervalo de confianza va de {extremoInferior} a {extremoSuperior} con el 99% de confiabilidad")


print(f"Porcentaje de ocupacion del caja 1: {porcentanje_1}%")
print(f"Porcentaje de ocupacion del caja 2: {porcentanje_2}%")
print(f"Porcentaje de ocupacion del caja 3: {porcentanje_3}%")

sns_plot = sns.distplot(tiempo_promedio_espera_total)
fig = sns_plot.get_figure()
fig.savefig("Simulacion3Cajas.png")