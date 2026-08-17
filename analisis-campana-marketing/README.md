# Análisis de Campaña de Marketing

Análisis exploratorio y dashboard interactivo sobre el dataset `marketing_campaign.xlsx` (2,240 clientes), enfocado en entender la relación entre los ingresos de los clientes y su gasto total en productos, con el fin de identificar segmentos de clientes útiles para estrategias de marketing.

## Contexto

Proyecto final del curso, desarrollado en **grupo (Grupo 3)** durante el "Data Scientist Course", en dos entregas:

- **Parte 1**: identificación y comprensión del dataset, limpieza, KPIs iniciales e informe de análisis.
- **Parte 2**: profundización del análisis (KPIs finales, consulta SQL adicional) y construcción de un dashboard interactivo con Streamlit.

Este repositorio incluye el trabajo individual de Daniel (`DanielKPI.ipynb` y los scripts de Streamlit que llevan su nombre) junto con el aporte de un compañero de equipo (`JoelKPI.ipynb`), ya que el entregable final del curso fue conjunto.

## Objetivo

Responder, desde una perspectiva de negocio, si los ingresos de un cliente determinan su nivel de gasto, e identificar patrones de comportamiento (por nivel educativo, estado civil, quintil de ingreso) que permitan a un equipo de marketing segmentar mejor sus campañas en lugar de dirigirse únicamente a los clientes de mayores ingresos.

## Tecnologías

- Python (pandas, numpy)
- matplotlib, seaborn
- Streamlit (dashboard interactivo)
- Plotly (`plotly.express`, `plotly.graph_objects`)
- Pillow (carga de imágenes en el dashboard)
- SQL (script de modelado relacional)
- Jupyter Notebook

## Estructura del proyecto

```
analisis-campana-marketing/
├── data/
│   └── marketing_campaign.xlsx          # dataset original (clientes de una campaña de marketing)
├── parte_1/
│   ├── KPI Datasets.ipynb               # limpieza, KPIs y primer análisis exploratorio
│   ├── Proyecto 1 - Visualizacion.ipynb # visualizaciones del dataset
│   └── INFORME DE ANALISIS DATASET MARKETING.pdf  # diccionario de datos e informe inicial
├── parte_2/
│   ├── DanielKPI.ipynb                  # análisis individual de Daniel (ingresos vs. gasto)
│   ├── JoelKPI.ipynb                    # análisis individual de un compañero de equipo
│   ├── final.sql                        # ejercicio SQL complementario (modelo relacional de ventas)
│   └── streamlit/
│       ├── main.py                      # dashboard grupal completo (Plotly)
│       ├── DanielKPI.py                 # primera versión del dashboard de Daniel
│       ├── DanielKPI_Final.py           # versión final del dashboard de Daniel
│       ├── DanielKPI_Fundamental_Tecnico.py  # variante con verificación de columnas
│       ├── daniel.py                    # script de prueba (chequeo de versión de plotly)
│       └── marketing_campaign.xlsx      # copia del dataset para ejecutar la app directamente
├── requirements.txt
└── README.md
```

## Metodología

1. **Carga y limpieza**: lectura del Excel, revisión de tipos de datos, nulos (24 valores faltantes en `Income`, imputados con 0) y duplicados (no se encontraron).
2. **Preparación de datos**: creación de la variable `TotalGastos`/`GastoTotal` como la suma de las seis categorías de gasto (`MntWines`, `MntFruits`, `MntMeatProducts`, `MntFishProducts`, `MntSweetProducts`, `MntGoldProds`).
3. **Análisis exploratorio**: relación ingresos vs. gasto (scatter + línea de tendencia), distribución de ingresos (histograma), ranking de los 10 mayores y 10 menores consumidores, gasto agregado por nivel educativo y por estado civil.
4. **Segmentación**: gasto total por quintiles de ingreso (Q1 a Q5) para comparar el comportamiento de consumo entre grupos.
5. **Dashboard interactivo**: se construyó una app en Streamlit (pestañas de relación ingresos-gasto, distribución de ingresos y gasto por quintiles) para explorar los hallazgos de forma visual.
6. **Ejercicio SQL complementario** (`final.sql`): diseño de un modelo relacional (clientes, empleados, servicios, ventas) para practicar consultas de agregación (total y promedio de ventas por cliente/empleado, venta máxima/mínima, etc.) sobre una base de datos ficticia ("NovaCruz").

## Resultados

- **Relación ingresos-gasto**: existe una tendencia positiva moderada (a mayor ingreso, mayor gasto), pero con alta variabilidad: hay clientes de ingresos medios (40k-90k) con gasto muy alto, y clientes con ingresos superiores a 150k con gasto relativamente bajo.
- **Gasto por quintiles**: el gasto total crece de forma consistente del Q1 al Q5, con mayor dispersión (comportamientos más heterogéneos) en el quintil de ingresos más altos.
- **Gasto por nivel educativo**: `Graduation` concentra la mayor parte del gasto total (≈698,626), seguido de `PhD` (≈326,791) y `Master` (≈226,359); `Basic` es el grupo con menor gasto (≈4,417).
- **Gasto por estado civil**: `Married` (≈510,453) y `Together` (≈352,865) son los segmentos con mayor gasto agregado.
- **Conclusión de negocio**: los ingresos son un buen predictor del gasto pero no el único factor. Se recomienda segmentar campañas más allá del nivel de ingreso puro, prestando atención a clientes de ingresos medios con alto gasto relativo (oportunidad de fidelización más rentable) y explorando por qué algunos clientes de altos ingresos gastan poco.

## Cómo ejecutar

```bash
pip install -r requirements.txt
```

**Notebooks** (Parte 1 y Parte 2): copia `data/marketing_campaign.xlsx` a la misma carpeta del notebook que vayas a ejecutar (o ajusta la ruta en `pd.read_excel(...)`), y luego:

```bash
jupyter notebook
```

**Dashboard de Streamlit** (recomendado: `DanielKPI_Final.py` o `main.py`):

```bash
cd parte_2/streamlit
streamlit run DanielKPI_Final.py
```

> Nota: `main.py` (el dashboard grupal) carga una imagen de portada con una ruta absoluta local de otro integrante del equipo (`C:\Users\ejbrito\...`), por lo que esa línea fallará o deberá comentarse/ajustarse antes de ejecutarlo fuera de esa máquina. El resto de la lógica del dashboard funciona de forma independiente.

## Datos

El dataset `marketing_campaign.xlsx` sí está incluido (≈300 KB). Contiene 2,240 registros de clientes con variables demográficas (edad, educación, estado civil, hijos), de comportamiento de compra (gasto por categoría de producto, canal de compra, visitas web) y de respuesta a campañas de marketing anteriores. Es un dataset de uso educativo entregado por el curso (dataset tipo "Customer Personality Analysis").
