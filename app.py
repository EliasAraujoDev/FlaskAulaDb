from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="loja"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']

    cursor.execute("INSERT INTO clientess (nome, email) VALUES (%s, %s)", (nome, email))
    db.commit()

    cursor.execute("SELECT * FROM clientess")
    clientess = cursor.fetchall()

    mensagem = "Cadastro real"

    return render_template('resultado.html', mensagem=mensagem, clientess=clientess)

if __name__ == '__main__':
    app.run(debug=True)
