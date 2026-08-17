from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

modelo = joblib.load('modelo_nlp.pkl')

@app.route("/predict", methods=["POST"])
def predecir():
    data = request.get_json(silent=True)
    if not data or 'texto' not in data:
        return jsonify({"error": "Falta el texto"}), 400
    resultado = modelo.predict([data['texto']])
    return jsonify({"prediccion": resultado[0]}), 200

if __name__ == '__main__':
    app.run(port=5000)

