import pandas as pd
import numpy as np
import os

#rutas
input_path = "cardio_train.csv"
output_path = "cardio_train_clean.csv"

#lecturas
if not os.path.exists(input_path):
    raise FileNotFoundError(f"El archivo no está en: {input_path}")

data = pd.read_csv(input_path, sep=";")
print(data.shape)
print(data.info())

#eliminacion de duplicados
duplicados = data.duplicated().sum()
data.drop_duplicates(inplace=True)
print(f"{duplicados} removed")

#edad a años
data["age"] = (data["age"]/365.25).astype(int)
print(data["age"].iloc[0])

#primer filtrado de posibles errores
antes = data.shape[0]

data = data[(data["height"]>100) & (data["weight"]>30) & (data["age"]<110) & (data["ap_hi"]>=50) 
            & (data["ap_hi"]<=250) & (data["ap_lo"]>=30) & (data["ap_lo"]<=150)]

elim = antes - data.shape[0]
print(f"{elim} removed")

#limpieza de datos categoricos
antes2 = data.shape[0]

data = data[(data["cholesterol"].isin([1, 2, 3])) & (data["gluc"].isin([1,2,3]))
            & (data["smoke"].isin([0,1])) & (data["alco"].isin([0,1])) & (data["active"].isin([0,1]))
            & (data["cardio"].isin([0,1]))]

elim2 = antes2 - data.shape[0]
print(f" {elim2} removed")

#elimiacion diastolica > sistolica (no es posible)
antes3 = data.shape[0]
data = data[data["ap_hi"]>data["ap_lo"]]
elim3 = antes3 - data.shape[0]
print(f"{elim3} removed")

#elimiacion de nulos
antes4 = data.shape[0]
nulos = data.isnull().sum().sum()
data.dropna(inplace=True)
elim4 = antes4 - data.shape[0]
print(f"{nulos} nulos eliminados de {elim4} filas")

#imc
data["bmi"] = (data["weight"]/((data["height"]/100)**2)).round(1)

#exportacion
data.to_csv(output_path, index=False)