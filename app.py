# Instalar "pip install flask"
# instalar "pip install mysql-connector-python"

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

@app.route('/resultado')
def resultado():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return render_template('resultado.html', clientes=clientes)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    email = request.form['email']

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
    db.commit()

    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    mensagem = "Cadastro realizado"

    return render_template('resultado.html', mensagem=mensagem, clientes=clientes)

@app.route('/atualizar/<int:id>', methods=['GET', 'POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cursor.execute("UPDATE clientes SET nome = %s, email = %s WHERE id = %s", (nome, email, id))
        db.commit()

        return redirect(url_for('resultado'))
    cursor.execute("SELECT * FROM clientes WHERE id = %s", (id,))
    cliente = cursor.fetchone()

    return render_template('atualizar.html', cliente=cliente)

if __name__ == '__main__':
    app.run(debug=True)
