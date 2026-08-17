# Dashboard de Mercado de Autos Usados

Modelo de datos y dashboard interactivo en Power BI sobre el mercado indio de autos usados, complementado con un ejercicio de modelado y explotación de datos en SQL Server.

## Contexto

Proyecto individual del módulo de Modelado de Datos y Business Intelligence ("Módulo 9"). La consigna pedía construir, a partir de un dataset abierto, un modelo de datos correctamente relacionado y un dashboard funcional en Power BI, aplicando transformaciones, medidas DAX y buenas prácticas de visualización (ver `documento_sin_titulo.pdf` para el enunciado completo de la actividad).

## Objetivo

Explorar el mercado indio de autos usados (200 vehículos) para entender qué factores se relacionan con el precio, la depreciación y el tiempo de venta de un vehículo, y presentar esos hallazgos en un dashboard ejecutivo con KPIs, segmentadores y comparativas por marca/ciudad. En paralelo, se practicó el modelado y la explotación de una base de datos transaccional de ventas en SQL Server.

## Tecnologías

- Power BI Desktop (modelo de datos, Power Query, DAX)
- SQL Server (T-SQL: creación de tablas, carga de datos, consultas de explotación)
- Excel (dataset y práctica de modelado de datos)

## Estructura del proyecto

```
dashboard-mercado-autos-usados/
├── final_indian_used_car_market_dataset.csv  # dataset principal del dashboard (200 autos)
├── Practica_Modelado_Datos.xlsx              # ejercicio de modelado de datos en Excel
├── explotacion.sql                           # script SQL: creación de la tabla Explotacion
├── dataset_ventas_20k_nombres.xls            # datos fuente de ventas usados en el ejercicio SQL
├── documento_sin_titulo.pdf                  # enunciado de la actividad (nombre original mal codificado, renombrado)
├── files/
│   ├── dashboard_used_cars.pbix              # dashboard de Power BI (archivo binario propietario)
│   ├── used_cars_powerbi.xlsx                # dataset/tabla auxiliar usada en el .pbix
│   ├── documentacion_powerbi.docx            # documentación del modelo y las transformaciones
│   └── README.txt                            # notas originales del entregable (ver resumen abajo)
└── README.md
```

## Metodología

1. **Preparación de datos**: importación del dataset de autos usados de la India (fuente abierta) y de un dataset de ventas ficticio (20k registros) para el ejercicio de SQL. Se aplicaron 6 transformaciones en Power Query: conversión del año a texto, creación de etiquetas para tipo de propietario y condición del vehículo, escala de precios a miles de rupias, orden numérico de propietarios y cálculo del porcentaje de depreciación.
2. **Modelado de datos**: modelo en **esquema estrella** con 3 tablas — `fact_cars` (tabla de hechos, 200 registros), `dim_brand` (8 marcas) y `dim_city` (8 ciudades) — relacionadas 1 a muchos mediante `brand_id` y `city_id`.
3. **Medidas DAX**: `Total Autos`, `Precio Promedio`, `KM Promedio`, `Depreciacion Promedio`, `Dias Para Vender`, `Precio Primer Dueno`, `Precio Tercer Dueno` y `Diferencia Por Dueno` (comparativo entre primer y tercer propietario).
4. **Dashboard**: 3 tarjetas KPI (total de autos, precio promedio, días para vender), un gráfico de columnas (precio promedio por marca), un gráfico de líneas (kilometraje promedio por año) y 3 segmentadores (tipo de combustible, ciudad, condición del vehículo).
5. **Explotación en SQL Server**: creación de la tabla `Explotacion` (columnas: Nombre, Apellido, Edad, Producto, Categoría, Cantidad, Precio, Ciudad, CanalVenta, MetodoPago, Descuento, Costo, Fecha) y carga masiva de registros de ventas para practicar consultas de explotación de datos.

## Resultados

Según la documentación original del entregable (`files/README.txt`), el modelo estrella permite comparar el comportamiento de precio y depreciación de los vehículos por marca, ciudad, tipo de combustible y condición, además de calcular cuánto pierde de valor un auto entre su primer y su tercer dueño (`Diferencia Por Dueno`). El dataset muestra, por ejemplo, vehículos con más de 90,000 km recorridos y hasta un 80% de depreciación acumulada frente a otros casi nuevos con menos de un año de antigüedad, lo que se refleja en el gráfico de columnas de precio promedio por marca y en el de kilometraje promedio por año.

## Cómo ejecutar

Este proyecto no requiere un entorno de Python. Para explorarlo:

1. Abre `files/dashboard_used_cars.pbix` con **Power BI Desktop** (gratuito) para ver el modelo de datos y el dashboard interactivo.
2. Revisa `files/documentacion_powerbi.docx` para el detalle de las transformaciones y medidas.
3. `explotacion.sql` y `dataset_ventas_20k_nombres.xls` pueden ejecutarse/importarse en SQL Server (o cualquier motor T-SQL compatible) para reproducir el ejercicio de modelado y explotación.

## Datos

- `final_indian_used_car_market_dataset.csv` (≈24 KB) y `files/used_cars_powerbi.xlsx` (≈35 KB): sí incluidos. Dataset abierto del mercado indio de autos usados.
- `dataset_ventas_20k_nombres.xls` (≈3.8 MB): sí incluido. Datos de ventas ficticios usados como fuente para el ejercicio SQL (`explotacion.sql`).
- **`AMINexplotacion.sql` (≈13.5 MB) NO se incluyó por tamaño** (supera el límite de ~10 MB del portafolio). Es un script generado automáticamente con la misma estructura que `explotacion.sql` (tabla `explotacion`) pero con miles de sentencias `INSERT` de datos de ventas (nombre, apellido, edad, producto, categoría, ciudad, etc.). Se incluyó en su lugar `dataset_ventas_20k_nombres.xls`, que contiene los mismos datos de origen en un formato mucho más liviano.
