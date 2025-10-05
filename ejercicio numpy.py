import numpy as np

datos = np.array([8, 15, 22, 30, 41])

print("Desviación estándar:", np.std(datos))
print("Varianza:", np.var(datos))
print("Suma total:", np.sum(datos))
print("Cantidad de datos:", datos.size)