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

# Slide Teste

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris consequat tortor eget lacus lacinia lobortis. Mauris rhoncus fermentum elit, id lobortis leo accumsan non.

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello, world! </h1>"

```