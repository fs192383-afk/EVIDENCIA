import numpy as np

# Arreglo 1D
datos = np.array([3, 7, 11, 15, 19])
print("Datos:", datos)
print("Suma total:", np.sum(datos))

# Matriz 2D
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nMatriz:\n", matriz)
print("Suma total matriz:", np.sum(matriz))
print("Suma por filas:", np.sum(matriz, axis=1))
print("Suma por columnas:", np.sum(matriz, axis=0))