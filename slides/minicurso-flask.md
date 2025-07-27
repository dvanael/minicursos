---
marp: true
size: 16:9
theme: base
paginate: true
title: Introdução ao Desenvolvimento Web com Flask
author: Ana Barbosa, Wenderson Nascimento
style: |
  .title, .sub{
    text-align: center;
    color: #000
  }
  .sub{
    font-size: 1em
  }
  .title{
    font-size: 3em
  }
---

<h1 class="title"> Introdução ao  Desenvolvimento Web com Flask </h1>

<h3 class="sub"> Ana Barbosa, Wenderson Nascimento </h3>

<!-- _footer: ![w:150](./img/written-by-human.svg) -->

---

# A Internet

A Internet é a rede global que conecta computadores de todo mundo.

Com a internet, as pessoas criaram novos hábitos e demandas.

O desenvolvimento web precisa acompanhar essas demandas.

---

# HTML

*Hypertext Markup Language* é a linguagem utilizada para exibição das páginas web.

O HTML é construído por texto e marcadores (*tags*).

Os navegadores interpretam o código do HTML e exibem os resultados.

---

# Exemplo Básico

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Primeiro Site</title>
</head>

<body>
  <h1>Hello, World</h1>
  <p>Texto muito legal</p>
</body>
</html>
```

Acessando o arquivo pelo navegador, é possivel visualizar a página.

---
# CSS

*Cascade Style Sheets* é a linguagem de estilo para páginas web.

CSS determina como os elementos do HTML são renderizados.

---
# Flask
[Documentação](https://flask.palletsprojects.com/en/stable/)
- Framework para aplicações web 
- Escrito em python
- Fácil de usar


---
# Instalação
- Criar pasta para projeto
- Criar ambiente virtual
```shell
python -m venv .venv
```
- Ativar ambiente virtual
```shell
.venv\Scripts\Activate.ps1
```
- Instalar o flask
```shell
pip install flask
```

---
# Primeira aplicação
- Criar arquivo `app.py`

O código pode ser incorporado no HTML, ou exportado de um arquivo externo.

---

## Exemplo. CSS Incorporado

CSS pode ser escrito diretamente no HTML

```html
<head>
  <style>
    body{
      background-color: grey;
      font-size: 32px;
    }
  </style>
</head>
```

Isso pode gerar arquivos com muitas linhas, assim criando um código grande demais.

---

## Exemplo. CSS Exportado

Fazemos um `link` no HTML com o CSS.

```html
<head>
    <link rel="stylesheet" href="main.css">
</head>
```

Escrevemos o código em um arquivo dedicado.

```css
body{
  background-color: grey;
  font-size: 32px;
}
```

Arquivos dedicados para cada linguagem melhoaram a organização do projeto e o torna mais escalavel.

---

# Backend e Frontend

HTML e CSS são reponsaveis apenas pelo visual de páginas web. A aparência e a interface de um sistema são chamados de **frontend**.

O frontend não é lidar com o processamento de dados enviados pelos usuários.

O **backend** roda em um servidor e lida com processamento de dados.

Linguagens usadas: **Python**, Java, PHP, Ruby, etc.

---

# Python

Python é uma liguagem de programação que permite intregação rápida de sistemas.

Possui uma sintáxe simples e fácil de aprender.

## Exemplo

**main.py**

```python
nome = input("Digite aqui: ")
print("Hello", nome)
```

---

# Flask

É um *framework* leve para desenvolvimento web.

Ótimo para aplicações simples e rápidos.

Menos robusto em comparação com outros *frameworks* Python, como o **Django**.

---

## Exemplo

**app.py**
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello, world! </h1>"
```
```shell
flask --app app.py run --debug
```

---
# Nosso projeto
Uma aplicação de jogos digitais
- Cadastrar jogos
- Listar jogos
- Filtrar busca de jogos

---
# Templates
- Criar pasta `templates` na raiz do projeto
- Criar `base.html`
- Criar `index.html`
- Criar pasta `static` na raiz do projeto
- Criar pasta `css` na pasta `static`
- Criar `main.css`

---
- No arquivo `base.html`
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Base{% endblock title %}</title>
</head>
<body>
    {% block header %}
        <header>
            <h1>Base</h1>
        </header>
    {% endblock header %}
    
    {% block content %}
            
    {% endblock content %}
</body>
</html>
```

---
- No `index.html`
```html
{% extends 'base.html' %}

{% block title %}
    Início
{% endblock title %}

{% block header %}
    <header>
        <h1>Início</h1>
    </header>
{% endblock header %}

{% block content %}
    <main>
        <section>
            <h2>Links</h2>
            <ul>
                <li><a href="{{ url_for('criar_usuario') }}">Criar usuário</a></li>
                <li><a href="{{ url_for('listar_usuarios') }}">Listar usuário</a></li>
            </ul>
        </section>
    </main>
{% endblock content %}
```

---
- No `main.css`
```css
body {
  font-family: "Noto Sans";
  margin: 40px auto;
  max-width: 650px;
  line-height: 1.6;
  font-size: 18px;
  color: #333;
  padding: 0 10px
}

h1, h2, h3 {
  line-height:1.2
}
```

---
# Construindo a aplicação
- Criar as rotas das páginas de listar e cadastrar
```python
from flask import render_template, url_for
```

```
@app.route("<URL>", methods=["GET", "POST"])
```

- Criar banco de dados (não é um banco de verdade)

---
- Criar listagem dos jogos
- Criar formulário de cadastro de jogos
- Criar filtragem de busca


---
# Como aprender desenvolvimendo web?
- Entender a história da web
- Construir projetos (pode criar coisas que já existem)

