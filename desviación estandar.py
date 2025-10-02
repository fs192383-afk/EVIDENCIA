import numpy as np

# Conjunto de datos
datos = np.array([7, 14, 21, 29, 36, 42])

# Cálculos principales
media = np.mean(datos)
desviacion = np.std(datos)
varianza = np.var(datos)

print("Datos:", datos)
print("Media:", media)
print("Varianza:", varianza)
print("Desviación estándar:", desviacion)