DASHBOARD POWER BI — Indian Used Car Market

Datoss:

Dataset de 200 autos usados del mercado indio (fuente abierta).

Se aplicaron 6 transformaciones: conversión del año a texto, creación de etiquetas para tipo de propietario y condición del vehículo, escala de precios a miles de rupias, orden numérico de propietarios y cálculo de porcentaje de depreciación.

Modelo:

Estrella con 3 tablas:

- fact_cars (tabla de hechos, 200 registros)
- dim_brand (8 marcas)
- dim_city (8 ciudades)

Relaciones 1 a muchos entre dim_brand y fact_cars, y entre dim_city y fact_cars, usando brand_id y city_id como llaves.

medidas DAX:

Total Autos, Precio Promedio, KM Promedio, Depreciacion Promedio, Dias Para Vender, Precio Primer Dueno, Precio Tercer Dueno, Diferencia Por Dueno (comparativo).

Dashboard:

- 3 tarjetas KPI: total de autos, precio promedio, días para vender
- Gráfico de columnas: precio promedio por marca
- Gráfico de líneas: kilometraje promedio por año
- 3 segmentadores: tipo de combustible, ciudad, condición del vehículo

Archivos entregados:

- dashboard_used_cars.pbix
- used_cars_powerbi.xlsx
