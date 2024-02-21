#!/usr/bin/env python
# coding: utf-8

# #### Conclusiones y Hallazgos: 

# 
# - Distribución del consumo de energía por máquina y mes: El análisis muestra que la máquina "Energía Activa Extrusora" tiene el mayor consumo kWh de energía, seguida por "Energía Activa Chiller" y "Energía Activa Espumas". Estas tres máquinas representan la mayor parte del consumo kWh total de energía.
# 
# - Consumo por tipo de día: El análisis revela que los días jueves y viernes exhiben un mayor consumo de energía, aproximadamente un 3% más alto en comparación con los otros días de la semana. Por otro lado, los fines de semana, particularmente los domingos, muestran una notable disminución del consumo de energía, disminuyendo hasta un 53.2% en comparación con el jueves.
# 
# <div style="text-align:center">
# 
# ![Consumos dias](imagen/newplot.png)
# 
# 
# </div>
# 
# - Los análisis indican que los viernes y jueves presentan un aumento del 3% en la demanda de energía eléctrica. Siguiendo esta observación y en línea con las conversaciones mantenidas con el equipo de Carvajal, donde se sugiere que la producción se mantiene constante en promedio a lo largo de la semana, podría plantearse la hipótesis de que la productividad del proceso podría disminuir para los otros días de la semana.
# 
# 
# - Se observa que el consumo de energía para la extrusora es mayor por un 2.83% de consumo en el tercer turno donde se evidencia que desde las 22:00 horas hasta las 6:00 horas aumenta. Se recomienda validar con personal de campo las actividades y procesos que se están llevando a cabo durante este período de tiempo.
# 
# <div style="text-align:center">
# 
# ![Estrusora](imagen/estrusora.png)
# 
# 
# </div>
# 
# **Recomendación Sistemas de enfriamiento:**
# - Mejora de aislamiento térmico de tanques. Agua gana aproximadamente 2°C mientras permanece almacenada en el tanque.
#  
# - Incremento del factor de carga del chiller Trane. Promedio de carga del chiller Trane es de 50%, se propone llevarlo a porcentajes de carga cercanos al 80% hasta antes de encender chillers auxiliares, teniendo en cuenta que el chiller Trane es el más eficientes los equipos disponibles.
# 
# - Con el fin de obtener mayor información de los procesos medidos, será necesario ampliar el alcance del proyecto aumentando el número de variables medidas (físicas y eléctricas). Adicional, se deben medir las ratas de producción de las máquinas que están siendo monitoreadas. Esto con el fin de estimar variaciones en la productividad de la máquina (kWh/Unidad producida). De esta manera se podrá analizar la disciplina operativa que se tenga en los procesos, tiempos muertos de producción o de paro del proceso y posibles estimaciones de costos reales que llevaran a tener información precisa sobre cuales son las acciones que se deben seguir para lograr ahorros significativos.
# 
# 
# **Recomendación adicional:**
# 
# Con el fin de obtener mayor información de los procesos medidos, será necesario ampliar el alcance del proyecto aumentando el número de variables medidas (físicas y eléctricas). Adicional, se deben medir las ratas de producción de las máquinas que están siendo monitoreadas. Esto con el fin de estimar variaciones en la productividad de la máquina (kWh/Unidad producida). De esta manera se podrá analizar la disciplina operativa que se tenga en los procesos, tiempos muertos de producción o de paro del proceso y posibles estimaciones de costos reales que llevaran a tener información precisa sobre cuales son las acciones que se deben seguir para lograr ahorros significativos. 
