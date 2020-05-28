import numpy as np
import seaborn as sns
import math

CANTIDAD_EXPERIMENTOS=30
CANTIDAD_CORRIDAS=100

def calcular_intervalo_confianza(coficienteZ, media, error):
    margenError = coficienteZ * error
    return media - margenError, media + margenError

duraciones_proyectos = []
promedio_total_experimentos = []

for experimento in range(CANTIDAD_EXPERIMENTOS):
    duracion_experimento = 0
    for corrida in range(CANTIDAD_CORRIDAS):
        #tiempos para cada tarea
        tarea_a = np.random.uniform(low=2, high=4)
        tarea_b = np.random.uniform(low=3, high=6)
        tarea_c = np.random.uniform(low=2, high=5)
        tarea_d = np.random.uniform(low=3, high=6)
        tarea_e = np.random.uniform(low=2, high=5)
        tarea_f = np.random.uniform(low=4, high=8)
        tarea_g = np.random.uniform(low=3, high=7)
        
        #agrupo las tareas 
        acceso_superior = [tarea_a, tarea_b, tarea_c]
        acceso_medio = [tarea_d,tarea_e]
        acceso_inferior = [tarea_f,tarea_g]
        
        #el proyecto tiene 3 grupos de tareas
        proyecto = {
            "Acceso_superior": acceso_superior,
            "Acceso_medio": acceso_medio,
            "Acceso_inferior": acceso_inferior
        }
        
        # La suma del tiempo de todas las tareas es la duracion del proyecto
        sumaAS= sum(acceso_superior)
        sumaAM= sum(acceso_medio)
        sumaAI= sum(acceso_inferior)
        
        duracion_proyecto = sumaAS + sumaAM + sumaAI
       
        #Acumulo la duracion del proyecto actual
        duracion_experimento += duracion_proyecto

        #Agrego la duracion del proyecto actual a la lista de duraciones de todos los proyectos (3000)
        duraciones_proyectos.append(duracion_proyecto)

    promedio_total_experimentos.append(duracion_experimento/CANTIDAD_CORRIDAS)

n = len(duraciones_proyectos)
media = np.mean(duraciones_proyectos)
desvio = np.std(duraciones_proyectos)*3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575

extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)

print(f"El tiempo promedio de finalizacion del proyecto es de {media}")
print(f"El intervalo de confianza va de {extremoInferior} a {extremoSuperior}] con el 99% de confiabilidad")



