# Clasificación de Clientes de Restaurante

Modelo de clasificación binaria que predice si un cliente de un restaurante es "frecuente" o "no frecuente" a partir de su historial de consumo, usando regresión logística con scikit-learn.

## Contexto
Proyecto Final del Módulo 5 (SQL y fundamentos de Machine Learning) de la carrera técnica en Data Science. Proyecto individual.

## Objetivo
Identificar, a partir de datos transaccionales de un restaurante ficticio, qué clientes tienen probabilidad de ser "frecuentes" (alto volumen o alto gasto en consumos), para apoyar decisiones de fidelización y marketing dirigido.

## Tecnologías
- Python
- pandas
- scikit-learn (`Pipeline`, `ColumnTransformer`, `StandardScaler`, `OneHotEncoder`, `LogisticRegression`)
- joblib (serialización del modelo)
- SQL (MySQL) para la generación del dataset

## Estructura del proyecto
```
clasificacion-clientes-restaurante/
├── restaurante_dmc.sql               # Script SQL: crea BD, tablas y datos, y genera el dataset de features
├── dataset_clientes_restaurante.csv  # Dataset resultante de la consulta SQL (10 clientes)
├── modelo_restaurante.py             # Entrenamiento, evaluación y guardado del modelo
├── modelo_clientes_restaurante.pkl   # Modelo entrenado (pipeline serializado con joblib)
└── README.md
```

## Metodología
1. **Preparación de datos (SQL):** `restaurante_dmc.sql` crea una base de datos `restaurante_dmc` con tres tablas (`clientes`, `productos`, `ventas`), inserta datos de ejemplo y define, mediante una consulta con `JOIN` y `GROUP BY`, las variables agregadas por cliente: cantidad de consumos, total consumido y días desde el último consumo. También calcula la etiqueta `es_frecuente` directamente en SQL.
2. **Carga y features (Python):** `modelo_restaurante.py` carga el CSV resultante y recalcula `es_frecuente` como variable binaria (1 si `cantidad_consumos >= 20` o `total_consumido >= 250`, 0 en caso contrario).
3. **Preprocesamiento:** las variables numéricas (`cantidad_consumos`, `total_consumido`, `dias_desde_ultimo_consumo`) se escalan con `StandardScaler`, y la variable categórica `sexo` se codifica con `OneHotEncoder(drop="first")`, combinadas en un `ColumnTransformer`.
4. **Modelado:** un `Pipeline` de scikit-learn encadena el preprocesamiento con un clasificador `LogisticRegression`, entrenado sobre un split 80/20 (`train_test_split` con `stratify=y` y `random_state=42`).
5. **Evaluación:** se reporta la matriz de confusión y el `classification_report` sobre el conjunto de prueba.
6. **Persistencia:** el pipeline completo (preprocesamiento + modelo) se guarda con `joblib.dump` en `modelo_clientes_restaurante.pkl`, y se incluye un ejemplo de predicción sobre un cliente nuevo.

## Resultados
El dataset base es pequeño (10 clientes, generados vía SQL como ejercicio didáctico), por lo que las métricas del `classification_report` no son representativas de un caso productivo real; el valor del proyecto está en el flujo completo SQL → features → pipeline de ML → modelo serializado. El script imprime en consola la matriz de confusión y el reporte de clasificación (precisión, recall y f1-score) al ejecutarse.

## Cómo ejecutar
```bash
pip install -r requirements.txt
python modelo_restaurante.py
```
El script vuelve a entrenar el modelo desde `dataset_clientes_restaurante.csv` y regenera `modelo_clientes_restaurante.pkl`.

## Datos
`dataset_clientes_restaurante.csv` se incluye completo (300 bytes, 10 registros): es la salida directa de la consulta SQL en `restaurante_dmc.sql`, que a su vez crea sus propios datos de ejemplo (no proviene de una fuente externa).

> Nota: el archivo original `modelo_restaurante.zip` no se incluyó en este repositorio porque contenía una copia idéntica de los mismos cuatro archivos (`.csv`, `.pkl`, `.py`, `.sql`) ya presentes de forma individual, sin contenido adicional.
