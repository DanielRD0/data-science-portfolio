# Portafolio de Data Science — Daniel De La Cruz

Proyectos desarrollados durante la **Carrera técnica en Data Science, Python y Machine Learning (10 meses)**, cubriendo el ciclo completo de un proyecto de datos: limpieza y preparación, análisis exploratorio (EDA), modelado con Machine Learning, evaluación rigurosa de modelos, SQL, Business Intelligence (Power BI) y despliegue de modelos como servicios web.

## Proyectos

| Proyecto | Descripción | Tecnologías clave |
| --- | --- | --- |
| [Predicción de Riesgo Crediticio](./prediccion-riesgo-crediticio) | Clasificación de clientes con riesgo de mora a partir de su historial de pagos, con pipeline reproducible y `GridSearchCV`. | scikit-learn, pandas, Pipelines |
| [Despliegue de Modelo NLP como API](./despliegue-modelo-ml-api) | Clasificador de sentimiento sobre reseñas (TF-IDF + Regresión Logística) servido vía Flask con autenticación JWT y persistencia en MySQL. | Flask, scikit-learn, MySQL, JWT |
| [Análisis de Campaña de Marketing](./analisis-campana-marketing) | KPIs, visualización y dashboard interactivo (Streamlit) sobre una campaña de marketing. Proyecto en equipo. | pandas, SQL, Streamlit |
| [Dashboard de Mercado de Autos Usados](./dashboard-mercado-autos-usados) | Modelado de datos y dashboard de Business Intelligence en Power BI sobre el mercado de autos usados en India. | SQL, Power BI |
| [Análisis Estadístico Aplicado](./analisis-estadistico-aplicado) | Proyecto de estadística aplicada con Python: pruebas de hipótesis, correlación y regresión lineal sobre datos de rendimiento estudiantil. | pandas, scipy, statsmodels |
| [Clasificación de Clientes de Restaurante](./clasificacion-clientes-restaurante) | Pipeline SQL → features → modelo (Regresión Logística) para identificar clientes frecuentes. | SQL, scikit-learn |
| [Clasificación de Producción Agrícola](./clasificacion-produccion-agricola) | Comparación de KNN, Árbol de Decisión y Random Forest sobre un dataset agrícola. | scikit-learn, seaborn |
| [Modelos de Clasificación Retail](./modelos-clasificacion-retail) | Serie de modelos KNN/Random Forest sobre datasets de Amazon, Zara y Walmart, incluyendo el proceso de optimización de un modelo. | scikit-learn, pandas |
| [EDA de Riesgo Cardiovascular](./eda-riesgo-cardiovascular) | Limpieza y validación de un dataset clínico de ~70,000 registros. | pandas, numpy |

Cada proyecto incluye su propio `README.md` con contexto, metodología, resultados y su `requirements.txt`.

## Otros repositorios

- **[limpieza-datos-modulo10](https://github.com/DanielRD0/limpieza-datos-modulo10)** — proyecto en equipo de limpieza de un dataset sintético de 600,000 transacciones financieras (Módulo 10), publicado como repositorio independiente.

## Tecnologías generales

Python (pandas, numpy, scikit-learn, matplotlib, seaborn), SQL (MySQL, SQL Server), Power BI, Flask, Streamlit, Jupyter Notebook, Git/GitHub.

## Sobre los datos

Los datasets grandes (>10MB) no se incluyen en este repositorio para mantenerlo liviano; cada proyecto documenta en su propio README el origen del dataset y cómo obtenerlo cuando aplica.
