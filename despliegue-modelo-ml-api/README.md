# Despliegue de un Modelo NLP como API Web con Autenticación

Aplicación web que sirve un modelo de clasificación de sentimiento (NLP) entrenado sobre reseñas de Amazon en español, expuesto a través de una API Flask con registro/login de usuarios, tokens JWT y persistencia de predicciones en MySQL.

## Contexto

Proyecto final individual del Módulo 8 (Despliegue de Modelos y APIs) de la carrera técnica en Data Science, Python y Machine Learning. El módulo avanza desde técnicas de reducción de dimensionalidad y clasificación hasta la construcción de APIs seguras, cerrando con este proyecto que integra todo el flujo: entrenar un modelo, empaquetarlo y servirlo detrás de una aplicación web autenticada.

## Objetivo

Clasificar el sentimiento de una reseña de producto en español (Muy malo / Malo / Regular / Bueno / Excelente) y exponer ese modelo como un servicio web utilizable, en vez de dejarlo solo en un notebook.

## Tecnologías

- **Modelo:** scikit-learn (`TfidfVectorizer` + `LogisticRegression`) sobre el dataset público `KRadim/edit_amazon_reviews_multi_es` (Hugging Face Datasets)
- **API / Backend:** Flask, Flask-JWT-Extended (autenticación), Flask-MySQLdb / PyMySQL
- **Base de datos:** MySQL (usuarios y predicciones)
- **Persistencia del modelo:** joblib (`pipeline.pkl`)

## Estructura del proyecto

```
proyecto_final/
├── proyecto_final_modelo.ipynb   # Entrenamiento: carga de datos, preprocesamiento, TF-IDF + LogisticRegression
├── app.py                        # API Flask: registro, login (JWT), predicción, persistencia en MySQL
├── proyecto_final.sql            # Esquema de la base de datos (tablas usuarios, predicciones)
├── pipeline.pkl                  # Modelo entrenado y serializado (vectorizador + clasificador)
└── templates/                    # Vistas HTML (login, registro, predicción)
practica/                         # Ejercicios previos del módulo que preceden al proyecto final
├── 01_practica_pca.ipynb         # Reducción de dimensionalidad con PCA
├── 02_clasificacion_knn_rf.ipynb # Clasificación con KNN y Random Forest
├── 03_api_autenticacion_jwt.py   # Práctica de API segura con JWT
├── 04_entrenamiento_modelo.py    # Práctica de entrenamiento + serialización de modelo
└── 05_api_prediccion.py          # Práctica de API de predicción simple
```

## Metodología

1. **Carga de datos:** dataset de reseñas de Amazon en español (`review_title`, `stars`) desde Hugging Face.
2. **Preparación de variables:** `review_title` como variable independiente; `stars` (1-5) recodificada a etiquetas de sentimiento (Muy malo → Excelente).
3. **Preprocesamiento de texto:** normalización a minúsculas y eliminación de caracteres especiales/números.
4. **Pipeline de modelado:** `TfidfVectorizer` para vectorizar el texto + `LogisticRegression` (`max_iter=1000`) como clasificador, entrenados juntos en un único `Pipeline` de scikit-learn.
5. **Evaluación:** `classification_report` sobre el conjunto de prueba (20%).
6. **Serialización:** el pipeline completo (vectorizador + modelo) se guarda con `joblib` para reutilizarlo sin reentrenar.
7. **Despliegue:** Flask carga `pipeline.pkl` al iniciar; el flujo web es registro → login (genera JWT y sesión) → formulario de predicción, que guarda cada texto y su predicción en MySQL para no recalcular si ya fue evaluado antes.

## Seguridad

El código original del curso tenía la contraseña de MySQL y las claves de Flask/JWT escritas directamente en `app.py`. En esta versión se movieron a variables de entorno (ver `.env.example`) — nunca subas un archivo `.env` real con credenciales al repositorio.

## Cómo ejecutar

```bash
pip install -r requirements.txt
cp .env.example .env   # y completa tus propias credenciales
mysql -u root -p < proyecto_final/proyecto_final.sql
cd proyecto_final
python app.py
```

## Datos

El dataset de entrenamiento (`KRadim/edit_amazon_reviews_multi_es`) se descarga automáticamente desde Hugging Face al ejecutar el notebook `proyecto_final_modelo.ipynb`; no se incluye en el repositorio. El modelo ya entrenado sí está incluido (`pipeline.pkl`).
