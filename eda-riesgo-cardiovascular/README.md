# EDA de Riesgo Cardiovascular

Limpieza y preparación de un dataset clínico de riesgo cardiovascular (~70,000 registros), junto con ejercicios prácticos adicionales de Análisis Exploratorio de Datos (EDA) sobre datos simulados.

## Contexto
Práctica personal realizada de forma individual, en paralelo a la carrera técnica en Data Science, para reforzar técnicas de limpieza y exploración de datos (EDA) más allá del contenido curricular.

## Objetivo
Dejar el dataset público `cardio_train` en condiciones de ser usado para análisis o modelado posterior: eliminar duplicados, filtrar valores fisiológicamente imposibles (presión arterial, altura, peso, edad) y derivar variables útiles como la edad en años y el índice de masa corporal (IMC).

## Tecnologías
- Python
- pandas, numpy
- scikit-learn (`load_iris`, en el ejercicio de práctica)
- matplotlib, seaborn (en el notebook de ejemplos de EDA)

## Estructura del proyecto
```
eda-riesgo-cardiovascular/
├── practica_EDA.py         # Script principal: limpieza del dataset cardiovascular
├── cardio_train.csv        # Dataset original (crudo)
├── cardio_train_clean.csv  # Dataset resultante tras la limpieza
├── EDAEjemplos.ipynb       # Ejercicios de EDA sobre un dataset simulado de ventas
├── EDA.py                  # Ejercicio de EDA/inspección con el dataset Iris (sklearn)
└── README.md
```

## Metodología
1. **Carga:** `practica_EDA.py` lee `cardio_train.csv` (separado por `;`), que contiene variables clínicas (edad en días, altura, peso, presión sistólica/diastólica, colesterol, glucosa, tabaquismo, alcohol, actividad física y la etiqueta `cardio`).
2. **Eliminación de duplicados:** se identifican y remueven filas duplicadas con `duplicated()`/`drop_duplicates()`.
3. **Conversión de unidades:** la edad, originalmente en días, se convierte a años completos.
4. **Filtrado de valores fisiológicamente inválidos:**
   - Altura > 100 cm, peso > 30 kg, edad < 110 años.
   - Presión sistólica (`ap_hi`) entre 50 y 250, presión diastólica (`ap_lo`) entre 30 y 150.
   - Variables categóricas (`cholesterol`, `gluc`, `smoke`, `alco`, `active`, `cardio`) restringidas a sus valores válidos.
   - Registros donde la presión diastólica es mayor que la sistólica (inconsistencia clínica).
5. **Nulos:** se cuentan y eliminan filas con valores nulos remanentes.
6. **Feature engineering:** se calcula el IMC (`bmi = peso / (altura_m)^2`).
7. **Exportación:** el dataset limpio se guarda como `cardio_train_clean.csv`.
8. **Ejercicios adicionales de EDA** (no aplicados al dataset cardiovascular, incluidos como práctica de técnicas): `EDA.py` carga el dataset Iris de scikit-learn y hace una inspección inicial (forma, `head()`, `describe()`); `EDAEjemplos.ipynb` construye un dataset simulado de ventas (con nulos inyectados intencionalmente) para practicar la configuración de visualizaciones con pandas/matplotlib/seaborn.

## Resultados
`practica_EDA.py` imprime en consola, en cada paso, la cantidad de registros eliminados por duplicados, por rangos fisiológicos inválidos, por categorías inválidas, por inconsistencia sistólica/diastólica y por nulos, permitiendo trazar cuánto se redujo el dataset original en cada etapa del proceso de limpieza. El resultado final (`cardio_train_clean.csv`) es un dataset depurado con una columna adicional de IMC, listo para un análisis exploratorio visual o modelado posterior (no incluidos en este repositorio, ya que el trabajo se centró en la etapa de limpieza).

## Cómo ejecutar
```bash
pip install -r requirements.txt
python practica_EDA.py
```
El script regenera `cardio_train_clean.csv` a partir de `cardio_train.csv`. Para los ejercicios adicionales:
```bash
python EDA.py
jupyter notebook EDAEjemplos.ipynb
```

## Datos
`cardio_train.csv` es el dataset público ["Cardiovascular Disease dataset"](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) (Kaggle), con ~70,000 registros de pacientes. Se incluye completo en este repositorio (~2.9 MB), junto con la versión limpia `cardio_train_clean.csv` (~3.1 MB) generada por `practica_EDA.py`.
