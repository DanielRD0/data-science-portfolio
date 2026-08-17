import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import os

# 1. Cargar el dataset desde la librería sklearn
iris_raw = load_iris()

# 2. Convertirlo a un DataFrame de Polars con las etiquetas (target)
# Creamos el DataFrame inicial con las características
df = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)

# Añadimos la columna del objetivo (especie) mapeando los números a nombres reales
target_names = iris_raw.target_names
df["species"] = [target_names[i] for i in iris_raw.target]

# 3. Inspección inicial detallada
print("--- Dataset Iris cargado desde sklearn ---")
print(f"Forma del dataset: {df.shape}")
print(df.head())

print("\n--- Resumen Estadístico ---")
print(df.describe())