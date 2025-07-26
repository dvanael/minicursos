---
marp: true
size: 4:3
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
</body>
</html>
```

Acessando o arquivo pelo navegador, é possivel visualizar a página.

---

# CSS

*Cascade Style Sheets* é a linguagem de estilo para páginas web.

CSS determina como os elementos do HTML são renderizados.

---

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello, world! </h1>"

```