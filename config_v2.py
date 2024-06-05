NIGHT_HOURS = [0, 1, 2, 3, 4, 5, 20, 22, 23]

# date format would be "YYYY-MM-DD"
# last baseline date must be the same
# date as start of study. Basically all
# dates must be mondays.
BASELINE = ['2023-08-01', '2024-03-01']
STUDY = ['2024-03-01', '2024-03-31']  # fechas generar informe
# PAST_WEEK = ['2023-01-30', '2023-02-06']

DATE_INTERVALS_TO_DISCARD = {
}

# variables that make up totalizer measurement
#ENERGY_VAR_LABELS = ('consumo-electricidad-dia')
#POWER_VAR_LABELS = ('consumo-agua-dia')


WHITELISTED_VAR_LABELS = (

    "ea-cvl-bomba-torre",  #general
    "ea-chiller",
    "ea-espuma",
    "ea-extrusora-welex",
    "ea-horno-recocido",
    "ea-termoformadora",
    "ea-tubos-colapsibles",
    "ea-ventilador-torre",
    "tmp-entrada-chiller",
    "tmp-salida-chiller",
    "factor-de-potencia", # chiller
    "factor-carga-chiller",
    "eficiencia-chiller",
    "temperatura-de-entrada",
    "temperatura-de-salida",
    "flujo-instantaneo",
    "potencia-activa",
    "potencia-termica",
    "planta frio", #torres de enfriamiento
    "carga-total-planta",
    "carga-alta-presion",
    "carga-baja-presion",
    "otros-chiller"

)


    #incluir temperaruta api-label : t-out
    #COP_DIA:  cop_dia