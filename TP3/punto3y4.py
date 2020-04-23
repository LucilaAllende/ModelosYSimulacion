import numpy as np
import seaborn as sns
import math

def calcular_intervalo_confianza(coficienteZ, media, error):
    margenError = coficienteZ * error
    return media + margenError, media - margenError

# Punto 3.c genero 100 datos con una distribucion de probabilidad exponencial.
beta = 1/2 #beta
datos_exponencial_1 = np.random.exponential(scale=beta, size=100) #creando muestra de datos
# grafico histograma de distribución exponencial.
sns_plot = sns.distplot(datos_exponencial_1)
fig = sns_plot.get_figure()
fig.savefig("distribucionExponencial100.png")

#Punto 4 calculo la media, la varianza y el intervalo de confianza para el punto 3.c
n = len(datos_exponencial_1)
media = np.mean(datos_exponencial_1)
varianza = np.var(datos_exponencial_1)
desvio = 3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575

extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)
cadena100 = "El intervalo de confianza de 100 valores va de: " + str(extremoInferior) + " a " + str(extremoSuperior)

print("La media de 100 valores",media)
print("La varianza de 100 valores", varianza)
print(cadena100)


# Punto 3.d genero 1000 datos con una distribucion de probabilidad exponencial.
beta = 1/2 #beta
datos_exponencial_2 = np.random.exponential(scale=beta, size=1000) #creando muestra de datos
# grafico histograma de distribución exponencial.
sns_plot = sns.distplot(datos_exponencial_2)
fig = sns_plot.get_figure()
fig.savefig("distribucionExponencial1000.png")

#Punto 4 calculo la media, la varianza y el intervalo de confianza para el punto 3.d
n = len(datos_exponencial_2)
media = np.mean(datos_exponencial_2)
varianza = np.var(datos_exponencial_2)
desvio = 3
error = (desvio/(math.sqrt(n)))
coficienteZ = 2.575

extremoInferior, extremoSuperior = calcular_intervalo_confianza(coficienteZ, media, error)
cadena1000 = "El intervalo de confianza de 1000 valores va de: " + str(extremoInferior) + " a " + str(extremoSuperior)

print("La media de 1000 valores",media)
print("La varianza de 1000 valores", varianza)
print(cadena1000)

#Punto 3.a transformo de uniforme a exponencial
def transformacion(dato, lambd):
    return (np.log(dato)*-1)/lambd

# genero 1000 datos con una distribucion de probabilidad uniforme.
datos_uniforme = np.random.uniform(low=0.0, high=1.0, size=1000)

lambdaE = 6
datos_transformados = list(map(lambda i: transformacion(i,lambdaE), datos_uniforme))

# grafico histograma de distribución exponencial.
sns_plot = sns.distplot(datos_transformados)
fig = sns_plot.get_figure()
fig.savefig("distribucionTransformacion.png")


