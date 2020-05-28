import numpy as np
import seaborn as sns
import math

CANTIDAD_EXPERIMENTOS=30
CANTIDAD_CORRIDAS=100

duraciones_proyectos = []
promedio_total_experimentos = []
contador_as = 0
contador_am = 0
contador_ai = 0

def calcular_intervalo_confianza(coficienteZ, media, error):
    margenError = coficienteZ * error
    return media - margenError, media + margenError

def calcular_porcentaje(contador):
    return (contador*100)/(CANTIDAD_CORRIDAS*CANTIDAD_EXPERIMENTOS)

def inicializacion():
    #tiempos para cada tarea
    tarea_a = np.random.uniform(low=1, high=5)
    tarea_b = np.random.uniform(low=1, high=3)
    tarea_c = np.random.uniform(low=1, high=3)
    tarea_d = np.random.uniform(low=1, high=6)
    tarea_e = np.random.uniform(low=6, high=12)
    tarea_f = np.random.uniform(low=5, high=10)
    tarea_g = np.random.uniform(low=10, high=15)
    
    #agrupo las tareas 
    acceso_superior = [tarea_a, tarea_b, tarea_c]
    acceso_medio = [tarea_a,tarea_d,tarea_e, tarea_f]
    acceso_inferior = [tarea_f,tarea_g]
    
    # La suma del tiempo de todas las tareas es la duracion del proyecto
    sumaAS= sum(acceso_superior)
    sumaAM= sum(acceso_medio)
    sumaAI= sum(acceso_inferior)

    return sumaAS, sumaAM, sumaAI


for experimento in range(CANTIDAD_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(CANTIDAD_CORRIDAS):

        sumaAS, sumaAM, sumaAI = inicializacion()
        duracion_proyecto = sumaAS + sumaAM + sumaAI
       
        #Acumulo la duracion del proyecto actual
        duracion_experimento += duracion_proyecto

        #Agrego la duracion del proyecto actual a la lista de duraciones de todos los proyectos (3000)
        duraciones_proyectos.append(duracion_proyecto)

        #si la ruta que lleva mas tiempo es Acceso superior incremento su contador
        if sumaAS> sumaAM and sumaAS>sumaAI:
            contador_as += 1
        #si la ruta que lleva mas tiempo es Acceso medio incremento su contador
        elif sumaAM> sumaAS and sumaAM>sumaAI:
            contador_am += 1
        #si la ruta que lleva mas tiempo es Acceso inferior incremento su contador
        elif sumaAI> sumaAS and sumaAI>sumaAM:
            contador_ai += 1

    promedio_total_experimentos.append(duracion_experimento/CANTIDAD_CORRIDAS)

n = len(duraciones_proyectos)
media = np.mean(duraciones_proyectos)
desvio = np.std(duraciones_proyectos)*3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575

extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)

porcentanje_as = calcular_porcentaje(contador_as)
porcentanje_am = calcular_porcentaje(contador_am)
porcentanje_ai = calcular_porcentaje(contador_ai)

print(f"El tiempo promedio de finalizacion del proyecto es de {media}")
print(f"El intervalo de confianza va de {extremoInferior} a {extremoSuperior}] con el 99% de confiabilidad")
print(f"El porcentaje de criticidad que tiene el acceso superior es {porcentanje_as}% ")
print(f"El porcentaje de criticidad que tiene el acceso medio es {porcentanje_am}% ")
print(f"El porcentaje de criticidad que tiene el acceso inferior es {porcentanje_ai}% ")

sns_plot = sns.distplot(duraciones_proyectos)
fig = sns_plot.get_figure()
fig.savefig("distribucionLavadero3000Corridas.png")

sns_plot2 = sns.distplot(promedio_total_experimentos)
fig2 = sns_plot2.get_figure()
fig2.savefig("distribucion30Experimentos.png")