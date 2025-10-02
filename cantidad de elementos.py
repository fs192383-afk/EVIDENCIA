import numpy as np

datos = np.array([5, 10, 15, 20, 25, 30, 35])

cantidad = datos.size
suma = np.sum(datos)
promedio = np.mean(datos)

print("Datos:", datos)
print("Cantidad de elementos:", cantidad)
print("Suma total:", suma)
print("Promedio:", promedio)