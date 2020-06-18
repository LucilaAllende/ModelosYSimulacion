# #constantes
# MAX_EXPERIMENTOS=60
# MAX_CORRIDAS=100

# CANTIDAD_HORAS_LABORABLES=24
# CANTIDAD_MINUTOS_LABORABLES = (CANTIDAD_HORAS_LABORABLES*60) #24 hs * 60 minutos laborables
# CANTIDAD_SURTIDORES=4


# #eventos
# LLEGADA_CAMION = 1
# ATENCION_CAMION = 2
# FIN_ATENCION_CAMION = 3
# SALIDA_CAMION = 4


# #variables
# promedio_total_experimentos = []
# tiempo_promedio_espera = 0

# #reloj_simulacion = Reloj()
# #estacion_de_servicio = EstacionDeServicio(CANTIDAD_HORAS_LABORABLES,CANTIDAD_SURTIDORES)
# #FEL=generar_FEL(CANTIDAD_HORAS_LABORABLES)

# for experimento in range(MAX_EXPERIMENTOS):
#     duracion_experimento = 0
#     for corrida in range(MAX_CORRIDAS):
#         cola_camiones = []
#         for evento_actual in FEL:
#             #evento_actual = tomar_proximo_evento(FEL, evento)
#             if evento_actual:
#                 #avanzo el reloj al tiempo del evento actual
#                 #reloj_simulacion.avanzar(evento_actual.inicio)

#                 #procesar el evento actual
#                 #procesar_evento(evento_actual, reloj_simulacion, estacion_de_servicio, FEL, cola_camiones)
                    

#         #duracion_atencion = 0
       
#         #Acumulo la duracion de la atencion actual
#         #duracion_experimento += duracion_atencion

#         #Agrego la duracion de la atencion actual a la lista de duraciones de todas las atenciones
#         #duraciones_atenciones.append(duracion_atencion)

#     #promedio_total_experimentos.append(duracion_experimento/MAX_CORRIDAS)