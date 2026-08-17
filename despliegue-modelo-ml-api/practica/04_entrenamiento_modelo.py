import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

X_train = ["me encanta este producto", "esto es horrible", "muy buen servicio", "muy mala experiencia"]
y_train = ["positivo", "negativo", "positivo", "negativo"]

pipeline = Pipeline([
    ('vectorizador', TfidfVectorizer()),
    ('modelo', LogisticRegression())
])

pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "modelo_nlp.pkl")
print("Listo: modelo_nlp.pkl creado.")

