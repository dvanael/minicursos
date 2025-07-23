from flask import Flask, render_template, request, url_for, redirect
from database import usuarios
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/usuarios/criar/", methods=["GET", "POST"])
def criar_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        usuarios.append({'nome': nome, 'idade': idade})
        return redirect(url_for('listar_usuarios'))
    else:
        return render_template("criar_usuario.html")

@app.route("/usuarios/")
def listar_usuarios():
    return render_template("lista_usuarios.html", usuarios = usuarios)

app.run(debug=True)