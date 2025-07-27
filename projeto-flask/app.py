from flask import Flask, render_template, request, url_for, redirect
from database import jogos

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", jogos=jogos)


@app.route("/jogos/criar/", methods=["GET", "POST"])
def cadastrar_jogo():
    if request.method == "POST":
        nome = request.form["nome"]
        ano = int(request.form["ano"])
        jogos.append({"nome": nome, "ano": ano})
        return redirect(url_for("listar_jogos"))
    else:
        return render_template("cadastrar_jogo.html")


@app.route("/jogos/")
def listar_jogos():

    # Filtro por ano
    filtro_ano = request.args.get('filtro-ano')
    if filtro_ano:
        jogos_filtrados = []
        for jogo in jogos:
            if jogo['ano'] == int(filtro_ano):
                jogos_filtrados += [jogo]
        return render_template("listar_jogos.html", jogos=jogos_filtrados)
        
    return render_template("listar_jogos.html", jogos=jogos)

