import os

import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_mysqldb import MySQL
from flask_jwt_extended import JWTManager, create_access_token
import joblib

app = Flask(__name__)

# Configuracion (lee credenciales desde variables de entorno, ver .env.example)
app.secret_key = os.environ["FLASK_SECRET_KEY"]
app.config["JWT_SECRET_KEY"] = os.environ["JWT_SECRET_KEY"]

# MySQL
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'proyecto_final')

mysql = MySQL(app)
jwt = JWTManager(app)

# Cargar el pipeline
pipeline = joblib.load('pipeline.pkl')


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        clave = request.form['clave']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usuario,))
        existe = cursor.fetchone()

        if existe:
            return render_template('register.html', error="El usuario ya existe")

        cursor.execute(
            "INSERT INTO usuarios (nombre, usuario, clave) VALUES (%s, %s, %s)",
            (nombre, usuario, clave)
        )
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('login'))

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        clave = request.form['clave']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM usuarios WHERE usuario = %s AND clave = %s",
            (usuario, clave)
        )
        user = cursor.fetchone()
        cursor.close()

        if user:
            token = create_access_token(identity=usuario)
            session['token'] = token
            session['usuario'] = usuario
            return redirect(url_for('predict'))
        else:
            return render_template('login.html', error="Credenciales inválidas")

    return render_template('login.html')


# PREDICT
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if 'token' not in session:
        return redirect(url_for('login'))

    resultado = None
    texto = None

    if request.method == 'POST':
        texto = request.form['texto']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT prediccion FROM predicciones WHERE texto = %s", (texto,)
        )
        existente = cursor.fetchone()

        if existente:
            resultado = existente[0]
        else:
            resultado = pipeline.predict([texto])[0]
            cursor.execute(
                "INSERT INTO predicciones (texto, prediccion) VALUES (%s, %s)",
                (texto, resultado)
            )
            mysql.connection.commit()

        cursor.close()

    return render_template('predict.html', resultado=resultado, texto=texto, usuario=session.get('usuario'))


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('token', None)
    session.pop('usuario', None)
    return redirect(url_for('login'))


@app.route('/')
def index():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
