# Modelos de Clasificación con Datasets Retail

Colección de notebooks de práctica enfocados en Análisis Exploratorio de Datos (EDA) y modelos de clasificación (KNN y Random Forest) aplicados a distintos datasets del sector retail: Amazon, Walmart y Zara. Cada notebook define una variable objetivo de negocio (calidad percibida, éxito de ventas) y evalúa un modelo con métricas estándar de clasificación.

## Contexto

Este material proviene del módulo de **Modelos de Clasificación (KNN y Random Forest)** de la carrera técnica en Data Science (Python y Machine Learning). El mandato práctico integrador pedía a cada grupo elegir un dataset estructurado (agro, economía, producción, ventas, datos sociales), realizar un EDA, definir variables objetivo categóricas y entrenar/evaluar un modelo de clasificación (KNN o Random Forest).

## Objetivo

Practicar el flujo completo de un proyecto de clasificación supervisada:
- Limpieza y preparación de datos (tipos, símbolos de moneda, encoding de categóricas, escalado).
- EDA estructurado (nulos, estadísticas descriptivas, distribuciones, relaciones entre variables).
- Definición justificada de variables objetivo y variables predictoras.
- Entrenamiento y evaluación de modelos KNN y Random Forest (accuracy, precision, recall, F1, matriz de confusión, importancia de variables).
- Iteración y optimización de un modelo (feature selection, ajuste de hiperparámetros).

## Tecnologías

- Python 3
- pandas, numpy
- scikit-learn (`RandomForestClassifier`, `KNeighborsClassifier`, `GridSearchCV`, `StandardScaler`, `LabelEncoder`, métricas de clasificación)
- matplotlib, seaborn

## Estructura del proyecto

```
modelos-clasificacion-retail/
├── README.md
├── requirements.txt
├── amazon.csv
├── zara.csv
├── Walmart_Sales.csv
├── sales_data.csv
├── proyecto amazon.ipynb
├── Proyecto_Dataset_KNN.ipynb
├── Proyecto_Dataset_RF.ipynb
├── Proyecto_Dataset_RF_.ipynb
├── Proyecto_Dataset_RF_Optimizado.ipynb
├── Proyecto_Data_Set_Walmart.ipynb
├── Agro reporte.ipynb
└── images/
    ├── eda_plots.png
    ├── confusion_matrix.png
    └── feature_importance.png
```

## Notebooks

| Notebook | Dataset | Modelo | Qué evalúa |
| --- | --- | --- | --- |
| `proyecto amazon.ipynb` | `amazon.csv` (India) | Random Forest (100 árboles) | Clasifica si un producto tendrá "buen rating" (>4.0) según precio, descuento y popularidad (nº de reseñas) |
| `Proyecto_Dataset_KNN.ipynb` | `zara.csv` | KNN (k=5) | Clasifica si una prenda será "Éxito de Ventas" (ventas por encima de la mediana) según posición en tienda, promoción, temporada, precio y sección |
| `Proyecto_Dataset_RF.ipynb` | `zara.csv` | Random Forest (100 árboles, 5 features) | Misma variable objetivo que el KNN, pero con Random Forest — versión base/línea de partida |
| `Proyecto_Dataset_RF_.ipynb` | `zara.csv` | Random Forest + `GridSearchCV` | Notebook de **experimentación**: prueba distintos subconjuntos de features, búsqueda de hiperparámetros y de semillas (`random_state`) para encontrar la mejor combinación. No es una entrega limpia, es el "cuaderno de trabajo" que llevó al modelo optimizado |
| `Proyecto_Dataset_RF_Optimizado.ipynb` | `zara.csv` | Random Forest (features reducidas: precio + posición en tienda) | **Versión final optimizada**, resultado directo de las pruebas del notebook anterior. Incluye visualización de un árbol de decisión individual |
| `Proyecto_Data_Set_Walmart.ipynb` | `Walmart_Sales.csv` | — (incompleto) | Solo carga el dataset y muestra las primeras filas; el kernel se bloqueó antes de llegar al modelado. Se conserva como evidencia del intento de EDA sobre ventas semanales de Walmart |
| `Agro reporte.ipynb` | `dataset_agro_rd_validado.csv` (no incluido, no se encontró en el material original) | — (no es clasificación) | Notebook de EDA/series de tiempo sobre precios y producción agrícola en República Dominicana (top productos por venta acumulada y por volatilidad de precio). No pertenece estrictamente al eje "retail + clasificación", se incluye como práctica adicional de EDA con pandas/seaborn. Al no contarse con el CSV original, el notebook no es reproducible tal cual está |

### Sobre las 3 versiones del Random Forest sobre Zara

`Proyecto_Dataset_RF.ipynb`, `Proyecto_Dataset_RF_.ipynb` y `Proyecto_Dataset_RF_Optimizado.ipynb` **no son tres proyectos distintos**, sino tres etapas de un mismo proceso de mejora sobre el mismo dataset y la misma pregunta de negocio:

1. **`RF.ipynb`** — modelo base con las 5 variables candidatas (posición, promoción, temporada, precio, sección). Accuracy: **60.78%**.
2. **`RF_.ipynb`** — notebook de experimentación: se prueba `GridSearchCV`, se agregan/quitan features (incluyendo `terms`), se simplifica el modelo y se hace una búsqueda de la semilla de partición (`random_state`) que mejor resultado da. Se descubre que reduciendo el modelo a solo `price` + `Product Position` con `random_state=69` se alcanza el mejor resultado (**70.59%**), superando incluso al Grid Search sobre todas las variables.
3. **`RF_Optimizado.ipynb`** — **versión final**, limpia y comentada, que aplica directamente el hallazgo anterior (solo 2 features, semilla óptima) y agrega una visualización del árbol de decisión para interpretar el modelo. Es la versión recomendada para revisar como entregable.

## Resultados

| Notebook | Dataset | Métrica principal | Detalle |
| --- | --- | --- | --- |
| `proyecto amazon.ipynb` | Amazon | Accuracy: **69.97%** | Clase "Bueno" (rating>4.0): Precision 0.72, Recall 0.82, F1 0.77. Variable más importante: `rating_count` (popularidad) |
| `Proyecto_Dataset_KNN.ipynb` | Zara | Accuracy: **56.86%** | Modelo base con 5 features escaladas (KNN, k=5) |
| `Proyecto_Dataset_RF.ipynb` | Zara | Accuracy: **60.78%** | Random Forest con las mismas 5 features, sin escalado (no es estrictamente necesario en RF) |
| `Proyecto_Dataset_RF_.ipynb` | Zara | Accuracy: hasta **70.59%** | Mejor resultado encontrado durante la experimentación (features reducidas + semilla óptima) |
| `Proyecto_Dataset_RF_Optimizado.ipynb` | Zara | Accuracy: **70.59%** | Versión final con solo `price` + `Product Position`. Variable más determinante: `price` |
| `Proyecto_Data_Set_Walmart.ipynb` | Walmart | — | No se completó: el kernel se bloqueó justo después de cargar los datos, no hay modelo ni métricas |

Las imágenes en `images/` (`eda_plots.png`, `confusion_matrix.png`, `feature_importance.png`) corresponden a las visualizaciones generadas por `proyecto amazon.ipynb`.

## Cómo ejecutar

```bash
pip install -r requirements.txt
jupyter notebook
```

Cada notebook lee su CSV correspondiente desde la misma carpeta (por ejemplo `pd.read_csv('zara.csv', sep=';')`), así que basta con abrirlos y ejecutar las celdas en orden. La excepción es `Agro reporte.ipynb`, que requiere un archivo `dataset_agro_rd_validado.csv` no incluido en este repositorio.

## Datos

- **`amazon.csv`**: catálogo de productos de Amazon India (precio, descuento, rating, nº de reseñas). Usado por `proyecto amazon.ipynb`.
- **`zara.csv`**: catálogo de prendas de Zara (posición en tienda, promoción, temporada, precio, volumen de ventas). Usado por los notebooks de KNN y Random Forest.
- **`Walmart_Sales.csv`**: ventas semanales por tienda de Walmart, con variables macro (temperatura, precio del combustible, CPI, desempleo). Usado (parcialmente) por `Proyecto_Data_Set_Walmart.ipynb`.
- **`sales_data.csv`**: dataset genérico de ventas por representante/región/categoría (muebles, etc.). No llegó a usarse en ningún notebook final; se conserva como material de práctica sin explotar.

### Nota sobre `Grupo 1.zip`

En la carpeta original del curso existía un archivo `Grupo 1.zip` (entrega grupal del proyecto de Amazon). Se revisó su contenido y resultó ser **redundante**: contiene exactamente `amazon.csv`, `proyecto amazon.ipynb` y un `READMEAMAZON.md` con la misma información ya presente suelta en la carpeta del curso. Por eso **no se copió** al portafolio; la información relevante de ese README se integró en este documento.
