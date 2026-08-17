import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# Cargar el dataset
df = pd.read_csv("dataset_clientes_restaurante.csv")

# Recalcular es_frecuente para tener 0 y 1
df["es_frecuente"] = (
    (df["cantidad_consumos"] >= 20) |
    (df["total_consumido"] >= 250)
).astype(int)

print("Clases en es_frecuente:")
print(df["es_frecuente"].value_counts())

# Separar variables (X) y etiqueta (y)
X = df[[
    "cantidad_consumos",
    "total_consumido",
    "dias_desde_ultimo_consumo",
    "sexo"
]]
y = df["es_frecuente"]  # 0 = no frecuente, 1 = frecuente

# Definir columnas numéricas y categóricas
numeric_features = ["cantidad_consumos", "total_consumido", "dias_desde_ultimo_consumo"]
categorical_features = ["sexo"]

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop="first")  # convierte 'M'/'F' a 0/1

preprocess = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# Modelo
classifier = LogisticRegression()

# Pipeline
model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("classifier", classifier),
])

# Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y 
)

# Entrenar
model.fit(X_train, y_train)

# Evaluar
y_pred = model.predict(X_test)

print("MATRIZ DE CONFUSIÓN:")
print(confusion_matrix(y_test, y_pred))

print("\nREPORTE DE CLASIFICACIÓN:")
print(classification_report(y_test, y_pred))

# Guardar modelo
joblib.dump(model, "modelo_clientes_restaurante.pkl")
print("\nModelo guardado en: modelo_clientes_restaurante.pkl")

# Ejemplo de predicción
nuevo_cliente = pd.DataFrame({
    "cantidad_consumos": [3],
    "total_consumido": [50.0],
    "dias_desde_ultimo_consumo": [15],
    "sexo": ["M"]
})

prediccion = model.predict(nuevo_cliente)
print("\nPredicción para nuevo cliente (1 = frecuente, 0 = no frecuente):", prediccion[0])