# Predicción de Riesgo Crediticio

Modelo de clasificación que identifica clientes con riesgo de mora a partir de su historial de pagos de tarjeta de crédito, construido con un pipeline reproducible y validado con `GridSearchCV`.

## Contexto

Proyecto final grupal (Grupo 2) del Módulo 7 de la carrera técnica en Data Science, Python y Machine Learning, enfocado en construcción y evaluación profesional de modelos. Se acompaña de las prácticas individuales del módulo que construyen las bases técnicas usadas en el proyecto final: feature engineering, pipelines con validación cruzada, y evaluación avanzada de modelos de clasificación (ROC/AUC/F1).

## Objetivo

Predecir si un cliente es de alto riesgo (`TARGET = 1`) a partir de su historial de estados de pago (`credit_record.csv`), y evaluar el modelo de forma rigurosa dado un fuerte desbalance de clases (~1.5% de clientes riesgosos).

## Tecnologías

Python, pandas, numpy, scikit-learn (`RandomForestClassifier`, `Pipeline`, `GridSearchCV`, `StandardScaler`, `cross_val_score`), matplotlib.

## Estructura del proyecto

```
notebooks/
├── 01_proyecto_final_riesgo_crediticio.ipynb  # Proyecto final: pipeline completo de clasificación de riesgo
├── 02_feature_engineering.ipynb               # Práctica de creación/transformación de variables
├── 03_pipelines_gridsearch_cv.ipynb           # Práctica de pipelines reproducibles + GridSearchCV
├── 04_evaluacion_roc_auc_f1.ipynb             # Práctica de evaluación avanzada (ROC, AUC, F1)
└── 05_optimizacion_modelo_inmobiliario.ipynb  # Práctica adicional de optimización de modelos (regresión de precios inmobiliarios)
```

## Metodología

1. **Variable objetivo:** a partir del historial de `STATUS` por mes (`credit_record.csv`), se agrupa por cliente (`ID`) calculando el peor estado de mora (`max_status`), promedio, suma y cantidad de meses. Se define `TARGET = 1` si el cliente tuvo alguna vez mora ≥ 2 meses.
2. **Modelado:** `Pipeline` con `StandardScaler` + `RandomForestClassifier`, validado con `cross_val_score` (5 folds).
3. **Ajuste de hiperparámetros:** `GridSearchCV` sobre `n_estimators`, `max_depth` y `min_samples_split`, optimizando F1 (más apropiado que accuracy dado el desbalance de clases).
4. **Evaluación:** `classification_report`, curva ROC y AUC sobre el conjunto de prueba.
5. **Ajuste de umbral (threshold moving):** se investigó bajar el umbral de decisión de 0.5 a 0.3 para priorizar recall sobre la clase minoritaria (clientes riesgosos), una técnica específica para el contexto de detección de riesgo donde no detectar un cliente riesgoso es más costoso que una falsa alarma.

## Resultados

- Validación cruzada (5-fold) sobre el pipeline base: **accuracy promedio ≈ 98.9%** (referencia poco informativa dado el desbalance).
- Mejor combinación de hiperparámetros (GridSearchCV, `scoring='f1'`): `n_estimators=100`, `max_depth=None`, `min_samples_split=2` → **F1 ≈ 0.58** en validación cruzada.
- En el conjunto de prueba, con umbral por defecto (0.5): **precision 0.62 / recall 0.54 / F1 0.57** para la clase de clientes riesgosos.
- Bajando el umbral a 0.3: recall sube a 0.64 a costa de precision (0.49) — trade-off explícito documentado en el notebook entre detectar más clientes riesgosos vs. generar más falsos positivos.

## Cómo ejecutar

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_proyecto_final_riesgo_crediticio.ipynb
```

## Datos

El dataset (`application_record.csv` y `credit_record.csv`, ~66MB combinados) no se incluye en el repositorio por su tamaño. Es el dataset público **"Credit Card Approval Prediction"** disponible en Kaggle; descárgalo y colócalo en una carpeta `data/` en la raíz de este proyecto antes de ejecutar el notebook.
