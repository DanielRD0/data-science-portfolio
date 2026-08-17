# Proyecto Final - Estadística Aplicada con Python
# Objetivo: analizar si horas de estudio, asistencia y tutorías influyen en la nota final.

# Pasos:

# 1) Cargar datos y ver un vistazo generaal
# 2) Descriptiva y gráficas
# 3) Comparar notas con/sin tutorías (prueba t)
# 4) Ver relación (correlación) de horas y asistencia con la nota
# 5) Regresión lineal simple (nota ~ horas_estudio) e interpretación

#Cargar datos y librerías

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

df = pd.read_csv("proyecto_estudiantes.csv", encoding="latin-1")

# Renombrar columnas a las que usa el script
df = df.rename(columns={
    "Horas_Estudio": "horas_estudio",
    "Asistencia (%)": "asistencia",
    "Tutorías": "tutorias",
    "Nota_Final": "nota_final"
})


# Si la columna "tutorías" tiene acento, la normalizamos a "tutorias" para evitar errores de nombbre.
if "tutorías" in df.columns and "tutorias" not in df.columns:
    df["tutorias"] = df["tutorías"]

# Renombrar columnas si vienen con otros nombres
if "Horas_Estudio" in df.columns: df = df.rename(columns={"Horas_Estudio": "horas_estudio"})
if "Asistencia (%)" in df.columns: df = df.rename(columns={"Asistencia (%)": "asistencia"})
if "Nota_Final" in df.columns: df = df.rename(columns={"Nota_Final": "nota_final"})

# Normalizar valores de tutorías
if "tutorias" in df.columns:
    df["tutorias"] = df["tutorias"].astype(str).str.strip()
    df["tutorias"] = df["tutorias"].replace({"Sí": "Si", "SI": "Si", "si": "Si", "NO": "No", "no": "No"})

# Asegurar tipos numéricos
for c in ["horas_estudio", "asistencia", "nota_final"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

# Vistazo rápido para confirmar columnas y tipos
print("\n--- Primeras filas ---")
print(df.head())

print("\n--- Descriptiva (numérica) ---")
print(df[["horas_estudio", "asistencia", "nota_final"]].describe())

#Gráficas exploratorias

#Histograma de notas para ver cómo se distribuyen
plt.figure()
plt.hist(df["nota_final"], bins=10)
plt.title("Distribución de notas finales")
plt.xlabel("Nota final")
plt.ylabel("Frecuencia")
plt.show()

#Boxplot notas según tutorías para comparar visualmente los grupos
plt.figure()
notas_si = df[df["tutorias"] == "Si"]["nota_final"]
notas_no = df[df["tutorias"] == "No"]["nota_final"]
plt.boxplot([notas_si, notas_no], labels=["Con tutorías", "Sin tutorías"])
plt.title("Notas según tutorías")
plt.ylabel("Nota final")
plt.show()

#Dispersión horas vs nota para ver la tendencia
plt.figure()
plt.scatter(df["horas_estudio"], df["nota_final"])
plt.title("Horas de estudio vs Nota final")
plt.xlabel("Horas de estudio (por semana)")
plt.ylabel("Nota final")
plt.show()

#Dispersión asistencia vs nota para ver la tendencia
plt.figure()
plt.scatter(df["asistencia"], df["nota_final"])
plt.title("Asistencia (%) vs Nota final")
plt.xlabel("Asistencia (%)")
plt.ylabel("Nota final")
plt.show()

# Hacemos una prueba t para comparar las medias de dos grupos independientes (Si vs No)
t_stat, p_val = stats.ttest_ind(notas_si, notas_no, equal_var=False)  # Welch por seguridad
print("\n--- Prueba t (Tutorías) ---")
print("t =", round(t_stat, 3), "| p =", round(p_val, 4))
if p_val < 0.05:
    print("Interpretación: p < 0.05 → hay evidencia de diferencia entre grupos (las tutorías probablemente ayudan).")
else:
    print("Interpretación: p ≥ 0.05 → no hay evidencia clara de diferencia (efecto no concluyente).")

#Correlaciones

#La correlación (de -1 a 1) indica fuerza y dirección de la relación lineal.
corr_horas = df["horas_estudio"].corr(df["nota_final"])
corr_asist = df["asistencia"].corr(df["nota_final"])
print("\n--- Correlaciones ---")
print("Horas de estudio ↔ Nota:", round(corr_horas, 3))
print("Asistencia ↔ Nota:", round(corr_asist, 3))

#Regresión lineal simple: Nota ~ Horas
# Usamos un modelo lineal para estimar cuánto cambia la nota por cada hora extra.
X = df[["horas_estudio"]]
y = df["nota_final"]

modelo = LinearRegression()
modelo.fit(X, y)

pendiente = modelo.coef_[0]        # cuanto cambia la nota por 1 hora extra
intercepto = modelo.intercept_     # valor de nota cuando horas_estudio = 0
r2 = modelo.score(X, y)            # qué proporción de la variación de la nota explica el modelo

print("\n--- Regresión (Nota ~ Horas) ---")
print("Pendiente:", round(pendiente, 2))
print("Intercepto:", round(intercepto, 2))
print("R^2:", round(r2, 3))
print("Interpretación: si un estudiante estudia 1 hora más por semana, la nota cambia en promedio",
        round(pendiente, 1), "puntos (según este modelo y estos datos).")

# Línea de regresión sobre el scatter para visualizar
import numpy as np
x_vals = np.array(sorted(X["horas_estudio"]))
y_pred = intercepto + pendiente * x_vals

plt.figure()
plt.scatter(df["horas_estudio"], df["nota_final"])
plt.plot(x_vals, y_pred)
plt.title("Regresión lineal: Nota ~ Horas de estudio")
plt.xlabel("Horas de estudio (por semana)")
plt.ylabel("Nota final")
plt.show()

#Cierre breve (impreso)

print("\n--- Conclusiones (resumen) ---")
if p_val < 0.05:
    print("• Tutorías: se observa diferencia entre grupos (posible impacto positivo).")
else:
    print("• Tutorías: no se observa diferencia estadísticamente clara.")

mas_fuerte = "horas de estudio" if abs(corr_horas) >= abs(corr_asist) else "asistencia"
print("• Variable más relacionada con la nota:", mas_fuerte)
print("• Regla práctica: +1 hora/semana → ~", round(pendiente, 1), "puntos más de nota (en promedio).")
print("• Recomendación: reforzar hábitos de estudio y monitorear asistencia; revisar/optimizar tutorías si es necesario.")
