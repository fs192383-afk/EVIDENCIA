import pandas as pd

datos = pd.Series([12, 18, 24, 30, 36])

print("Desviación estándar:", datos.std())
print("Varianza:", datos.var())
print("Cantidad:", datos.count())
print("Suma:", datos.sum())
print("Tamaño:", datos.size)