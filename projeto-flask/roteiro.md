---
marp: true
paginate: true
size: 16:9
---

- `url_for()`
- `render_template()`

---
# Flask 
## Aplicação inicial
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World!</h1>"

app.run(debug=True)
```
- No terminal
```shell
python main.py
```

---
# Templates
- Criar pasta `templates` na raiz do projeto
- Criar `base.html`
- Criar `index.html`

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
- No `main.py`
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)
```