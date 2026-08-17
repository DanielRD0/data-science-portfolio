from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_mysqldb import MySQL
import pickle
import joblib




app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"
jwt = JWTManager(app)

limiter = Limiter(get_remote_address, app=app)




#Configuración de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'arlenedata'

mysql = MySQL(app)





@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    # Simulación de usuario

    # cursor().execute(
    #     "SELECT * from usuarios where username = '{user}' and password = '{password}'".format(
    #         **{'user': username, 'password': password}
    #     )
    # )
    if username == "admin" and password == "1234":
        token = create_access_token(identity=username)
        return jsonify(access_token=token)

    if username == "estudiante" and password == "1234":
        token = create_access_token(identity=username)
        return jsonify(access_token=token)

    return jsonify({"msg": "Credenciales inválidas"}), 401







@app.route("/bearer", methods=["POST"])
@limiter.limit("5 per minute")
@jwt_required()
def predict():
    user = get_jwt_identity()

    return jsonify({
        "usuario": user,
    })


def check_auth(username, password):
    return username == "admin" and password == "1234"


@app.route("/basic-protected")
def basic_protected():
    auth = request.authorization

    print(auth)
    # Validar si no hay credenciales
    if not auth:
        return jsonify({"error": "Autenticación requerida"}), 401

    # Validar usuario y contraseña
    if not check_auth(auth.username, auth.password):
        return jsonify({"error": "Credenciales inválidas"}), 401

    return jsonify({"mensaje": "Acceso permitido"})


@app.route("/predict", methods=['POST'])
def predict_comment():

    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("""
                   SELECT nota FROM comentario a
                   LEFT JOIN productos b ON (a.id_producto = b.id_producto)
                   WHERE lower(b.descripcion) = '{producto}' 
                   """.format(**{'producto': data['producto'].lower()}))
    result = cursor.fetchall()
    print(result)
    cursor.close()


    pipeline = joblib.load('pipeline2.pkl')
    # with open('pipeline.pkl', 'rb') as f:
    #     pipeline = pickle.load(f)

    if not pipeline:
        return jsonify({"error": "Ha ocurrido un error cargando el modelo"})
    

    comment_list = []
    for comment in result:
        comment_list.append(comment[0])

    predict = pipeline.predict(comment_list)

    return jsonify(str(predict))



if __name__ == "__main__":
    app.run(debug=True)