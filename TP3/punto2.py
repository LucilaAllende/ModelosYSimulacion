
import numpy as np
import seaborn as sns

# 2.a genero 1000 datos con una distribucion de probabilidad uniforme.
datos_uniforme = np.random.uniform(low=0.0, high=1.0, size=1000)
# grafico histograma de distribución uniforme.
sns_plot = sns.distplot(datos_uniforme)
fig = sns_plot.get_figure()
fig.savefig("distribucionUniforme.png") 

# 2.b genero 1000 datos con una distribucion de probabilidad normal.
mu, sigma = 0, 1 # media y desvio estandar
datos_normal = np.random.normal(mu, sigma, 1000) #creando muestra de datos
# grafico histograma de distribución normal.
sns_plot = sns.distplot(datos_normal)
fig = sns_plot.get_figure()
fig.savefig("distribucionNormal.png")

# 2.c genero 1000 datos con una distribucion de probabilidad poisson.
lamb = 5 #lambda
datos_poisson = np.random.poisson(lam=lamb, size=1000) #creando muestra de datos
# grafico histograma de distribución poisson.
sns_plot = sns.distplot(datos_poisson)
fig = sns_plot.get_figure()
fig.savefig("distribucionPoisson.png")

# 2.d genero 1000 datos con una distribucion de probabilidad exponencial.
beta = 1/4 #beta
datos_exponencial = np.random.exponential(scale=beta, size=1000) #creando muestra de datos
# grafico histograma de distribución exponencial.
sns_plot = sns.distplot(datos_exponencial)
fig = sns_plot.get_figure()
fig.savefig("distribucionExponencial.png") 