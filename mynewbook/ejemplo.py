import pandas as pd
import numpy as np

datos = {
    'Nombre': ['Juan', 'Paula', 'Daniela', 'Gaby'],
    'Calificaciones':['80', '100', '98', '95'],
    'Deportes':['Bicileta', 'Natacion', 'Crosfit', 'Patinaje'],
    'Edad':[20, 25, 30, 35]
         }

df = pd.DataFrame(datos)

print(df)
print('\n'*2)
#Datos no validos


datos2 = {
    'Nombre': ['Juan', 'Paula', 'Daniela', 'N/A'],
    'Calificaciones':['80', np.nan, '98', '95'],
    'Deportes':['Bicileta', 'Natacion', 'Crosfit', 'N/A'],
    'Edad':[20, 25, 30, 35]
         }
         
        
df2 = pd.DataFrame(datos2)
print(df2)
print('\n'*2)
#print(df2.info())

"""
#Estadisticas
print('\n'*2)
print(df2.describe())

print('\n'*2)

nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan, "0")
print(nuevo)

print('\n'*2)

nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how='any', inplace=True)
print(nuevo2)


print('\n'*2)

columna = df2[df2['Nombre']!= 'N/A']
print(columna)
"""
#llenar con cero cualquier valor

nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0, inplace=True)
print(nuevo3)


print('\n'*2)


print(nuevo3.describe())

print('\n'*2)

#estadisticas individuales
print("Promedio", nuevo3['Edad'].mean())