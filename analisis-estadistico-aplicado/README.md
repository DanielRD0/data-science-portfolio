# Análisis Estadístico Aplicado

Análisis estadístico en Python sobre el rendimiento académico de 30 estudiantes, para determinar si las horas de estudio, la asistencia y las tutorías influyen en la nota final de un curso.

## Contexto

Proyecto final individual del módulo de Estadística y Probabilidad para Data Science ("Módulo 4"). El enunciado planteaba un rol de analista de datos dentro de una institución educativa, que debía aplicar estadística descriptiva, prueba de hipótesis, correlación y regresión lineal sobre un dataset de 30 estudiantes para responder si las tutorías realmente ayudan a mejorar las notas y qué variable pesa más en el rendimiento académico.

## Objetivo

Determinar, con evidencia estadística, si existe una diferencia significativa en la nota final entre estudiantes con y sin tutorías, medir la relación entre horas de estudio/asistencia y la nota final, y construir un modelo simple que permita estimar el impacto de una hora adicional de estudio semanal sobre la calificación.

## Tecnologías

- Python
- pandas (carga y limpieza de datos)
- matplotlib (visualización: histograma, boxplot, dispersión, regresión)
- SciPy (`scipy.stats`, prueba t de Welch)
- scikit-learn (`LinearRegression`)
- numpy

## Estructura del proyecto

```
analisis-estadistico-aplicado/
├── proyecto_estudiantes.csv      # dataset de 30 estudiantes (horas de estudio, asistencia, tutorías, nota final)
├── proyecto_final.py             # script de análisis estadístico completo
├── Informe_Proyecto_Final.pdf    # informe de resultados y conclusiones (2 páginas)
├── Graficas/                     # gráficas generadas por el script
│   ├── Figure_1.png              # histograma de notas finales
│   ├── Figure_2.png              # boxplot de notas según tutorías
│   ├── Figure_3.png              # dispersión: horas de estudio vs. nota
│   ├── Figure_4.png              # dispersión: asistencia vs. nota
│   └── Figure_5.png              # regresión lineal: nota ~ horas de estudio
├── material-apoyo/               # material de referencia del módulo (no es parte del entregable)
│   ├── Estadisticas-CienciadeDatos presentacion 1.pdf
│   ├── Resumen_Estadistica_y_Tendencia.pdf
│   └── presentacion 2.pptx
├── requirements.txt
└── README.md
```

## Metodología

1. **Carga y preparación de datos**: lectura del CSV (codificación `latin-1` por los caracteres acentuados del dataset original), normalización de nombres de columnas y de los valores de la variable `tutorías` (`Sí`/`No`), y conversión de columnas numéricas.
2. **Estadística descriptiva**: distribución de las notas finales (histograma) y estadísticos generales (`describe()`).
3. **Comparación de grupos (prueba t)**: prueba t de Welch entre el grupo con tutorías y el grupo sin tutorías, con boxplot comparativo.
4. **Correlación**: cálculo de la correlación de Pearson entre horas de estudio/nota final y asistencia/nota final, con gráficos de dispersión.
5. **Regresión lineal simple**: modelo `Nota ~ Horas de estudio` con `scikit-learn`, reportando pendiente, intercepto y R².
6. **Conclusiones**: interpretación en lenguaje no técnico de los resultados, con recomendaciones para la institución.

## Resultados

- Las calificaciones se concentran en un rango medio-alto (media aproximada de 75 puntos), sin outliers relevantes; la mayoría de los estudiantes mantuvo una asistencia superior al 70%.
- **Tutorías**: los estudiantes con tutorías obtuvieron notas ligeramente superiores, pero el valor p de la prueba t fue mayor a 0.05 → **no hay evidencia estadísticamente significativa** de que las tutorías, en esta muestra, mejoren la nota final.
- **Correlaciones**: relación positiva moderada entre horas de estudio y nota final; relación positiva pero más débil entre asistencia y nota final.
- **Regresión lineal**: por cada hora adicional de estudio semanal, la nota promedio sube entre 2 y 3 puntos (R² con nivel de ajuste moderado, indicando que otros factores no contemplados también influyen).
- **Conclusión principal**: las horas de estudio son la variable más asociada al rendimiento académico. Se recomienda reforzar hábitos de estudio autónomo, fomentar la asistencia regular y revisar/rediseñar el programa de tutorías para aumentar su efectividad.

## Cómo ejecutar

```bash
pip install -r requirements.txt
python proyecto_final.py
```

> Nota: el script usa una ruta absoluta local (`r"C:\Users\danie\...\proyecto_estudiantes.csv"`) para cargar el dataset, tal como se entregó originalmente. Antes de ejecutarlo, ajusta esa ruta para que apunte a `proyecto_estudiantes.csv` en esta misma carpeta (por ejemplo, `pd.read_csv("proyecto_estudiantes.csv", encoding="latin-1")`).

## Datos

El dataset `proyecto_estudiantes.csv` (30 registros, <1 KB) sí está incluido. Es un dataset sintético/didáctico entregado por el curso con las columnas `Estudiante`, `Horas_Estudio`, `Asistencia (%)`, `Tutorías` y `Nota_Final`.

Se excluyó `Book1.xlsx`, un archivo de práctica/scratch (cálculo manual de desviaciones sobre un ejercicio de 12 filas) que no forma parte del proyecto final entregado y no está relacionado con el dataset de estudiantes.
