# Clasificación de Producción Agrícola (KNN / Random Forest)

Comparación de modelos de clasificación supervisada (KNN, Árbol de Decisión y Random Forest) aplicados a un dataset sintético de producción agrícola de República Dominicana, para predecir el nivel de producción y la rentabilidad de un cultivo.

## Contexto
Módulo 6 (Machine Learning con Python) de la carrera técnica en Data Science. Trabajo individual, incluye tanto el material de clase (KNN, Árboles de Decisión y Bosques Aleatorios, Introducción a ML) como la generación propia del dataset usado en los ejercicios.

## Objetivo
Predecir, a partir de variables de siembra (área sembrada, producción total, precio unitario y mes), si un cultivo cae en un nivel de producción "Bajo/Medio/Alto" o de rentabilidad "Baja/Media/Alta", comparando el desempeño de distintos algoritmos de clasificación.

## Tecnologías
- Python
- pandas, numpy
- scikit-learn (`KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `LogisticRegression`, `StandardScaler`, `train_test_split`, `cross_val_score`, `classification_report`, `confusion_matrix`)
- matplotlib, seaborn
- SQL (T-SQL / SQL Server, práctica complementaria)

## Estructura del proyecto
```
clasificacion-produccion-agricola/
├── Agricultura_df.ipynb                          # Primera versión: generación sintética del dataset agrícola
├── DF_agricultura_rd_validado.ipynb              # Versión validada del generador; produce dataset_agro_rd_validado.csv
├── dataset_agro_rd_validado.csv                  # Dataset usado por los notebooks de KNN y Random Forest
├── Clase_2_KNN.ipynb                             # Clasificación con K-Nearest Neighbors
├── Clase_3_Random_Forest.ipynb                   # Árbol de Decisión vs. Random Forest
├── Introduccion_a_ML.ipynb                       # Notas introductorias + ejemplo de regresión lineal
├── Arboles_de_Decision_y_Bosques_Aleatorios.ipynb # Teoría y práctica con datasets Wine / Breast Cancer (sklearn)
├── sql/
│   └── Practica.sql                              # Práctica complementaria de SQL (DDL/DML sobre AdventureWorks)
└── README.md
```

## Metodología
1. **Generación de datos:** `Agricultura_df.ipynb` genera un dataset sintético de 80,000 registros de producción agrícola dominicana (producto, región, clima, preparación de suelo, área sembrada, producción y precio) usando distribuciones controladas (log-normal para el área sembrada, variabilidad por clima y estacionalidad de precios). `DF_agricultura_rd_validado.ipynb` es una versión refinada de ese generador, con una base de rendimientos por producto más realista y validación de consistencia (rendimiento QQ/tarea dentro de rangos esperados); su salida es `dataset_agro_rd_validado.csv`, el dataset efectivamente usado en los notebooks de modelado.
2. **Ingeniería de variables objetivo:** en ambos notebooks de modelado se crean variables categóricas por terciles (`pd.qcut`) sobre `Producción_Total` (nivel de producción) y sobre `Producción_Total * Precio_Unitario` (rentabilidad/ingreso).
3. **KNN (`Clase_2_KNN.ipynb`):** features `Área_Sembrada_Tareas`, `Producción_Total`, `Precio_Unitario`, `Mes`, escaladas con `StandardScaler`. Se entrena un `KNeighborsClassifier(n_neighbors=5)`, se evalúa con matriz de confusión y `classification_report`, se valida con `cross_val_score` (5-fold) y se explora el efecto de distintos valores de `k` sobre la precisión.
4. **Árbol de Decisión y Random Forest (`Clase_3_Random_Forest.ipynb`):** mismas features, comparando un `DecisionTreeClassifier(max_depth=4)` contra un `RandomForestClassifier(n_estimators=100, max_depth=6)`, con análisis de importancia de características (`feature_importances_`) y visualización de la distribución de clases con seaborn.
5. **Material de clase complementario:** `Introduccion_a_ML.ipynb` cubre los componentes básicos de un flujo de ML con un ejemplo de regresión lineal simple; `Arboles_de_Decision_y_Bosques_Aleatorios.ipynb` compara Árbol de Decisión, Random Forest, KNN y Regresión Logística sobre los datasets `load_wine` y `load_breast_cancer` de scikit-learn.
6. **SQL complementario:** `sql/Practica.sql` es una práctica independiente de creación de esquemas, DML y joins sobre la base `AdventureWorks2022`, incluida como evidencia de trabajo con SQL Server durante el módulo (no está relacionada con el dataset agrícola).

## Resultados
- **KNN** (k=5) sobre la variable de rentabilidad: `accuracy` de **0.88** sobre el set de prueba (16,000 registros), con f1-score de 0.99 para la clase "Alto", 0.85 para "Bajo" y 0.82 para "Medio". La validación cruzada (5-fold) sobre el nivel de producción dio un promedio de **0.884**.
- **Random Forest** (`n_estimators=100, max_depth=6`) sobre la variable de rentabilidad: `accuracy` de **0.92**, superando al Árbol de Decisión individual, con f1-score de 0.93-0.95 en todas las clases.
- En el notebook de teoría con datasets de sklearn: Random Forest y Regresión Logística alcanzaron accuracy de 1.00 sobre `load_wine` (dataset pequeño, 178 muestras), el Árbol de Decisión 0.94 y KNN sin escalar 0.74; sobre `load_breast_cancer`, la Regresión Logística obtuvo 0.956 de exactitud.

## Cómo ejecutar
```bash
pip install -r requirements.txt
jupyter notebook
```
Abrir los notebooks en el siguiente orden sugerido: `DF_agricultura_rd_validado.ipynb` (opcional, regenera el CSV) → `Clase_2_KNN.ipynb` → `Clase_3_Random_Forest.ipynb`. `Introduccion_a_ML.ipynb` y `Arboles_de_Decision_y_Bosques_Aleatorios.ipynb` son independientes y no requieren el CSV.

## Datos
`dataset_agro_rd_validado.csv` es un dataset **sintético**, generado por el propio autor con `DF_agricultura_rd_validado.ipynb` (no proviene de una fuente oficial externa); simula producción agrícola por producto, región y año en República Dominicana. Se incluye completo en este repositorio (~6.2 MB). El nombre del archivo se mantuvo sin cambios porque los notebooks `Clase_2_KNN.ipynb` y `Clase_3_Random_Forest.ipynb` lo cargan por ese nombre exacto (`pd.read_csv('dataset_agro_rd_validado.csv')`).
