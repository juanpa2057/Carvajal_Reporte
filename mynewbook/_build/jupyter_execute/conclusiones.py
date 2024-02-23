#!/usr/bin/env python
# coding: utf-8

# #### Conclusiones y Hallazgos: 

# 
# - Distribución del consumo de energía por máquina y mes: El análisis muestra que la máquina 'Energía Activa Extrusora' representa el 38% del consumo total de kWh de energía, seguida por 'Energía Activa Chiller' con el 24%, y 'Energía Activa Espumas' con el 15%. Estas tres máquinas en conjunto representan el 78% del consumo total de kWh de energía durante el periodo monitoreado.
# 
# <div style="text-align:center">
# 
# ![Estrusora](imagen/at.png)
# 
# 
# </div>
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
# - Según la segmentación del consumo de kWh por turno, se observa que el tercer turno, que abarca desde las 22:00 hasta las 6:00 horas, es el que presenta el mayor consumo de energía. Se recomienda validar con el personal de planta qué acciones se están implementando durante este turno que puedan estar contribuyendo a un mayor consumo energético, en comparación con el primer y segundo turno de operación.
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
# **Recomendación adicional:**
# 
# Con el fin de obtener mayor información de los procesos medidos, será necesario ampliar el alcance del proyecto aumentando el número de variables medidas (físicas y eléctricas). Adicional, se deben medir las ratas de producción de las máquinas que están siendo monitoreadas. Esto con el fin de estimar variaciones en la productividad de la máquina (kWh/Unidad producida). De esta manera se podrá analizar la disciplina operativa que se tenga en los procesos, tiempos muertos de producción o de paro del proceso y posibles estimaciones de costos reales que llevaran a tener información precisa sobre cuales son las acciones que se deben seguir para lograr ahorros significativos. 
