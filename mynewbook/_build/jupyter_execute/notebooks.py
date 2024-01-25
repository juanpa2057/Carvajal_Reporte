#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt
import json
from datetime import datetime

import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

pio.renderers.default = "notebook"
pio.templates.default = "plotly_white"


# this enables relative path imports
import os
from dotenv import load_dotenv
load_dotenv()
_PROJECT_PATH: str = os.environ["_project_path"]
_PICKLED_DATA_FILENAME: str = os.environ["_pickled_data_filename"]

import sys
from pathlib import Path
project_path = Path(_PROJECT_PATH)
sys.path.append(str(project_path))

import config_v2 as cfg

from library_report_v2 import Cleaning as cln
from library_report_v2 import Graphing as grp
from library_report_v2 import Processing as pro
from library_report_v2 import Configuration as repcfg


# In[2]:


import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[3]:


periodo_historico = cfg.BASELINE
periodo_de_estudio = cfg.STUDY


# In[4]:


def show_response_contents(df):
    print("The response contains:")
    print(json.dumps(list(df['variable'].unique()), sort_keys=True, indent=4))
    print(json.dumps(list(df['device'].unique()), sort_keys=True, indent=4))


# In[5]:


DEVICE_NAME = 'Reporte Carvajal'


# In[6]:


df = pd.read_pickle(project_path / 'data' / _PICKLED_DATA_FILENAME)
#df = df.query("device_name == @DEVICE_NAME")
show_response_contents(df)


# In[7]:


conteo_variable_df = df['variable'].value_counts().to_frame().reset_index()
conteo_variable_df.columns = ['variable', 'conteo']


# In[8]:


df = df.sort_values(by=['variable','datetime'])
df = pro.datetime_attributes(df)


# In[9]:


ea_bomba_torre = df.query("variable == 'ea-cvl-bomba-torre'").copy()
ea_chiller = df.query("variable == 'ea-chiller'").copy()
ea_espuma = df.query("variable == 'ea-espuma'").copy()
ea_extrusora = df.query("variable == 'ea-extrusora-welex'").copy()
ea_horno = df.query("variable == 'ea-horno-recocido'").copy()
ea_termo = df.query("variable == 'ea-termoformadora'").copy()
ea_tubos = df.query("variable == 'ea-tubos-colapsibles'").copy()
ea_ventilador = df.query("variable == 'ea-ventilador-torre'").copy()
eficiencia_chiller = df.query("variable == 'eficiencia-chiller'").copy()


# In[10]:


ea_bomba_torre = cln.remove_outliers_by_zscore(ea_bomba_torre, zscore=4)
ea_chiller = cln.remove_outliers_by_zscore(ea_chiller, zscore=4)
ea_espuma = cln.remove_outliers_by_zscore(ea_espuma, zscore=4)
ea_extrusora = cln.remove_outliers_by_zscore(ea_extrusora, zscore=4)
ea_horno = cln.remove_outliers_by_zscore(ea_horno, zscore=4)
ea_termo = cln.remove_outliers_by_zscore(ea_termo, zscore=4)
ea_tubos = cln.remove_outliers_by_zscore(ea_tubos, zscore=4)
ea_ventilador = cln.remove_outliers_by_zscore(ea_ventilador, zscore=4)

df_ea = df.copy()
df_ea = cln.remove_outliers_by_zscore(df_ea, zscore=4)
eficiencia_chiller = cln.remove_outliers_by_zscore(eficiencia_chiller, zscore=4)


eficiencia_chiller = eficiencia_chiller[eficiencia_chiller['value'] >0]


# In[11]:


ea_bomba_torre_mean = ea_bomba_torre.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_bomba_torre_mean = pro.datetime_attributes(ea_bomba_torre_mean)

ea_chiller_mean = ea_chiller.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_chiller_mean = pro.datetime_attributes(ea_chiller_mean)

ea_espuma_mean = ea_espuma.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_espuma_mean = pro.datetime_attributes(ea_espuma_mean) 

ea_extrusora_mean = ea_extrusora.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_extrusora_mean = pro.datetime_attributes(ea_extrusora_mean)

ea_horno_mean = ea_horno.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_horno_mean = pro.datetime_attributes(ea_horno_mean)

ea_termo_mean = ea_termo.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_termo_mean = pro.datetime_attributes(ea_termo_mean)

ea_tubos_month = ea_tubos.groupby(by=["variable"]).resample('H').median().reset_index().set_index('datetime')
ea_tubos_month = pro.datetime_attributes(ea_tubos_month)

df_planta = df_ea.groupby(by=["variable"]).resample('H').sum().reset_index().set_index('datetime')
df_planta = pro.datetime_attributes(df_planta)

eficiencia_chiller_ok = eficiencia_chiller.groupby(by=["variable"]).resample('H').mean().reset_index().set_index('datetime')
eficiencia_chiller_ok = pro.datetime_attributes(eficiencia_chiller_ok)

#para sacar las graficas de mes y tabla
df_ea_month = df_ea.groupby(by=["variable"]).resample('M').sum().reset_index().set_index('datetime')
df_ea_month = pro.datetime_attributes(df_ea_month)

#df_ea_eficiencia = eficiencia_chiller.groupby(by=["variable"]).resample('D').mean().reset_index().set_index('datetime')
#df_ea_eficiencia = pro.datetime_attributes(df_ea_eficiencia)


# In[12]:


valores_a_buscar = [
    "ea-cvl-bomba-torre",
    "ea-chiller",
    "ea-espuma",
    "ea-extrusora-welex",
    "ea-horno-recocido",
    "ea-termoformadora",
    "ea-tubos-colapsibles",
    "ea-ventilador-torre"
]

mapeo = {
    "ea-cvl-bomba-torre": "energia activa bomba torre",
    "ea-chiller": "energia activa chiller",
    "ea-espuma": "energia activa espuma",
    "ea-extrusora-welex": "energia activa extrusora",
    "ea-horno-recocido": "energia activa horno recocido",
    "ea-termoformadora": "energia activa termoformadora",
    "ea-tubos-colapsibles": "energia activa linea 7",
    "ea-ventilador-torre": "energia activa ventilador torres"
}


# In[13]:


# Reemplazar los valores en la columna 'variable'
df['variable'] = df['variable'].replace(mapeo)


# In[14]:


df_energia = df_ea_month[df_ea_month['variable'].isin(valores_a_buscar)]
df_energia['variable'] = df_energia['variable'].replace(mapeo)

consumo_maquinas = df_planta[df_planta['variable'].isin(valores_a_buscar)]
consumo_maquinas['variable'] = consumo_maquinas['variable'].replace(mapeo)


# ## Informe Gestión de Energia

# A continuación, encontrarás un resumen de la distribución del consumo de energía por mes correspondiente al monitoreo de energía (kWh) entre agosto a diciembre de 2023.

# In[15]:


import plotly.graph_objects as go
import pandas as pd

# Asumiendo que df_energia está cargado con los datos correctos

# Ordenar el DataFrame por variable y mes de manera descendente
df_energia = df_energia.sort_values(by=['variable', 'month'], ascending=[True, False])

# Redondear y formatear los valores sin decimales
df_energia['value_formatted'] = df_energia['value'].round(0).apply(lambda x: f'{x:,.0f}')

# Crear la tabla
fig = go.Figure(data=[go.Table(
    header=dict(values=['Proceso', 'Consumo Energía (kWh)', 'Mes']),
    cells=dict(values=[df_energia['variable'], 
                       df_energia['value_formatted'],  # Usar los valores formateados
                       df_energia['month']]))
])

# Ajustar el diseño y formato
fig.update_layout(
    title='Datos de Consumo de Energía por Máquina y Mes',
    font=dict(size=12),  # Ajustar el tamaño del texto
    template='plotly_white'  # Cambiar el tema a plotly_white
)

# Mostrar la tabla
fig.show()


# Se representa el consumo acumulado de energía en kWh por máquina durante los meses de agosto a diciembre del 2023:
# 
# - Energía Activa Extrusora: Esta máquina tiene la mayor parte del consumo con un 38% del total.
# - Energía Activa Chiller:: Esta máquina tiene el segundo mayor consumo con un 25% del total.
# - Energía Activa Espumas: Esta máquina tiene el tercer mayor consumo con un 15% del total.
# 
# Las secciones restantes del gráfico representan otras máquinas con porcentajes de consumo menores. Este informe de gestión de energía proporciona una visión clara de cómo se distribuye el consumo de energía entre las diferentes máquinas en estos tres meses.

# In[16]:


# Agrupar por máquina y sumar la energía
df_grouped = df_energia.groupby('variable').sum().reset_index()

# Crear el gráfico de torta
fig = px.pie(df_grouped, values='value', names='variable', 
             title='Distribución del Consumo de Energía por Máquina',
             labels={'variable': 'Máquina', 'value': 'Consumo de Energía'},
             color_discrete_sequence=px.colors.qualitative.Set1)

# Habilitar la interactividad para agregar/quitar máquinas
fig.update_traces(hoverinfo='label+percent', textinfo='value+percent', pull=[0.1]*len(df_grouped))

# Mostrar el gráfico
fig.show()


# In[17]:


df_ea_pivot = df_energia.pivot_table(values='value', index='datetime', columns='variable')


# In[18]:


import calendar
columns_name = ['ea-chiller', 'ea-cvl-bomba-torre', 'ea-espuma', 'ea-extrusora-welex',
       'ea-horno-recocido', 'ea-termoformadora', 'ea-tubos-colapsibles',
       'ea-ventilador-torre']
 
 
# Get the month name from the month number
df_ea_pivot['Mes'] = df_ea_pivot.index.month.map(lambda x: calendar.month_name[x])
 
# Group by month and sum the columns
df_ea_pivot = df_ea_pivot.groupby('Mes').sum([columns_name])
#df_ea_pivot = df_ea_pivot.groupby(df_ea_pivot['Mes']).sum([columns_name])


# In[19]:


df_ea_pivot = df_ea_pivot.reset_index()

df_ea_pivot['Mes'] = df_ea_pivot['Mes'].replace({'August': 'Agosto', 'October': 'Octubre', 'September': 'Septiembre', 'November': 'Noviembre', 'December': 'Diciembre'})

# Definir el nuevo orden de los meses
nuevo_orden_meses = ['Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Cambiar el índice usando reindex
df_ea_pivot = df_ea_pivot.set_index('Mes').reindex(nuevo_orden_meses).reset_index()

# Convertir la columna "Mes" en el índice
df_ea_pivot = df_ea_pivot.set_index('Mes')

# agrego esto:

dt_total = df_ea_pivot.copy()
# Sumar a lo largo de las columnas y agregar una nueva columna "Total"
dt_total['Total'] = df_ea_pivot.sum(axis=1)

# Resetear el índice para tener "variable" como una columna nuevamente
dt_total.reset_index(inplace=True)


# Se presenta el consumo acumulado por proceso mensual, destacando que el mayor consumo de energía ocurrió en Octubre:
# 
# - Agosto: 358,213 kWh/mes
# - Septiembre: 380,615 kWh/mes
# - Octubre: 393,443 kWh/mes"
# - Noviembre: 390,716 kWh/mes"
# - Diciembre: 342,421 kWh/mes"

# In[20]:


fig = px.bar(df_ea_pivot)
fig.update_layout(
        title = "Comsumo por Maquina",
        width=800,
        height=600,
        yaxis_title="Consumo energia (kWh)",
        showlegend = True,
        legend_title="Proceso",
 
)


# In[21]:


ea_bomba_torre_mean['value'] = ea_bomba_torre_mean['value'].round(2)
ea_chiller_mean['value'] = ea_chiller_mean['value'].round(2)
ea_espuma_mean['value'] = ea_espuma_mean['value'].round(2)
ea_extrusora_mean['value'] = ea_extrusora_mean['value'].round(2)
ea_horno_mean['value'] = ea_horno_mean['value'].round(2)
ea_termo_mean['value'] = ea_termo_mean['value'].round(2)
ea_tubos_month['value'] = ea_tubos_month['value'].round(2)
df_ea_month['value'] = df_ea_month['value'].round(2)
df_planta['value'] = df_planta['value'].round(2)
consumo_maquinas['value'] = consumo_maquinas['value'].round(2)
eficiencia_chiller_ok['value'] = eficiencia_chiller_ok['value'].round(2)


# In[22]:


ea_bomba_torre_dia = ea_bomba_torre_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_chiller_dia = ea_chiller_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_espuma_dia = ea_espuma_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_extrusora_dia = ea_extrusora_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_horno_dia = ea_horno_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_termo_dia = ea_termo_mean.groupby(["hour", "dow"])["value"].mean().reset_index()
ea_tubos_dia = ea_tubos_month.groupby(["hour", "dow"])["value"].mean().reset_index()
df_planta = df_planta.groupby(["hour", "dow"])["value"].mean().reset_index()
eficiencia_chiller_ok = eficiencia_chiller_ok.groupby(["hour", "dow"])["value"].mean().reset_index()
consumo_maquinas = consumo_maquinas.groupby(["hour", "variable"])["value"].mean().reset_index()



# #### Consumo Tipico por día Para Carvajal

# Presentamos el análisis del consumo de energía de la planta clasificado por tipo de día. Durante el trimestre examinado, se observa que la planta experimentó un mayor consumo de energía los días viernes y jueves. Asimismo, se destaca una disminución en el consumo durante los fines de semana, siendo el domingo el día con menor consumo, seguido por el sábado.

# In[23]:


fig = px.box(df_planta, x="dow", y="value", color="dow", points='all', category_orders={"dow": ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]})
fig.update_layout(
    title='Consumo por tipo de día',
    width=800,
    height=600,
    yaxis_title="Consumo kWh",
    title_font_size=12,
    xaxis_title="Día"
)


# La gráfica anterior muestra la tendencia de los consumos medidos, en la cual se observa que los domingos tienen una disminución considerable de carga, lo cual puede corresponder a paradas de planta o procesos diferentes que se ejecuten estos días.

# In[24]:


# Gráfico de áreas apiladas
fig = px.area(consumo_maquinas, x='hour', y='value', color='variable', line_group='variable',
              labels={'value': 'Consumo (kWh)', 'hour': 'Hora del día'},
              title='Consumo Horario Planta por Proceso')

fig.update_layout(
    legend_title_text='Día de la Semana',
    xaxis_title='Hora',
    yaxis_title='kWh',
)

fig.show()


# Consumo Horario Planta por Proceso: muestra la distribución del consumo de energía en la planta a lo largo del día, desglosado por proceso. Cada área en el gráfico representa un proceso específico, y la altura de cada área indica la cantidad de energía consumida en ese proceso en cada hora del día.

# #### Consumo por típo de día y proceso

# Consumo semana cada línea en el gráfico representa un día de la semana específico, y la posición de la línea en cada punto indica la cantidad de energía consumida en ese día de la semana en cada hora del día.

# In[25]:


#Planta
fig = px.line(df_planta, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Planta') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Chiller**

# In[26]:


#chiller efici
fig = px.line(eficiencia_chiller_ok, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Eficiencia Chiller por Día de la Semana ') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kW/TR')
fig.show()


#Chiller
fig = px.line(ea_chiller_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Chiller') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Extrusora Welex 2501**

# In[27]:


#Extrusora
fig = px.line(ea_extrusora_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Extrusora Welex 2501') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Espuma**

# In[28]:


#Espumas
fig = px.line(ea_espuma_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Espuma') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Tubos Colapsibles**

# In[29]:


#tubos
fig = px.line(ea_tubos_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Tubos Colapsibles') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Termoformadora Gabler 2**

# In[30]:


#termo
fig = px.line(ea_termo_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Termoformadora Gabler 2') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Horno Recocido linea 7**

# In[31]:


#Horno
fig = px.line(ea_horno_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Horno Recocido linea 7') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Bomba Torre**

# In[32]:


#Bomba de torre

fig = px.line(ea_bomba_torre_dia, x='hour', y='value', color='dow', # line_group='dow',               
	labels={'Consumo': 'Consumo (ejemplo)', 'Hora': 'Hora del día'},               
	title='Consumo horario por Día de la Semana Bomba Torre') 
fig.update_layout(legend_title_text='Día de la Semana',xaxis_title = 'Hora',
                  yaxis_title = 'kWh')
fig.show()


# **Conclusiones:**
# 
# - Distribución del consumo de energía por máquina y mes: El análisis muestra que la máquina "Energía Activa Extrusora" tiene el mayor consumo de energía, seguida por "Energía Activa Chiller" y "Energía Activa Espumas". Estas tres máquinas representan la mayor parte del consumo total de energía.
# 
# - El consumo de energía fue mayor en octubre, seguido por noviembre y agosto. Esto indica que octubre  fue el mes con mayor demanda de energía analizado.
# 
# - Consumo por tipo de día: El análisis muestra que los días jueves y viernes tienen un mayor consumo de energía en comparación con los demás días de la semana. Los fines de semana, especialmente los domingos, tienen un consumo más bajo de energía.
# 
# - Consumo horario de la planta por proceso: El gráfico muestra la distribución del consumo de energía en la planta a lo largo del día, desglosado por proceso. Se observa que el consumo varía a lo largo del día para cada proceso, con picos de consumo en diferentes momentos.
