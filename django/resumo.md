---
title: Resumo Django
subtitle: Conceitos e exemplos
---

# Resumo: Desenvolvimento Web com Django

Este documento consolida os principais conceitos e exemplos presentes nos handouts da trilha de sistemas web com Django.

---

## 1. Conceitos Gerais da Web

### Endereço IP e Porta

Cada computador na internet possui um **endereço IP** (ex: `192.168.0.1`) e cada programa que usa a rede ocupa uma **porta** (ex: `8080`). Juntos, identificam um programa específico em um computador específico: `192.168.0.1:8080`.

### URL

Uma URL como `http://192.168.0.1:8080/caminho/do/recurso` é composta por:

- **Protocolo**: `http`
- **Endereço**: `192.168.0.1`
- **Porta**: `8080`
- **Caminho**: `/caminho/do/recurso`

### Requisição e Resposta (Request/Response)

O navegador envia uma **requisição** (*request*) ao servidor, que processa e devolve uma **resposta** (*response*), geralmente em HTML. Imagens, CSS e JavaScript são carregados via requisições adicionais.

---

## 2. O Framework Django

### O que é um framework?

Um framework possui uma **estrutura de código pronta que chama as suas funções**, ao invés de você chamar as funções da biblioteca. No Django, você define as funções e classes; o framework decide quando chamá-las.

### Fluxo de uma requisição no Django (MVT)

```
Navegador → Servidor → Porta → Django → urls.py → views.py → [models.py / templates] → Resposta HTTP
```

1. Navegador faz requisição ao servidor
2. Django recebe na porta configurada
3. `urls.py` mapeia o caminho para uma função de view
4. `views.py` executa a lógica de negócios
   - Pode consultar o banco via `models.py`
   - Pode renderizar HTML via templates
5. Resposta é devolvida ao navegador

A arquitetura é chamada **MVT (Model-View-Template)**:
- **Model**: interação com o banco de dados
- **View**: lógica de negócios
- **Template**: geração do HTML

---

## 3. Configuração do Projeto

### Ambiente Virtual (venv)

Isola as dependências de cada projeto Python.

```bash
# Criar venv
python3 -m venv .venv --prompt .

# Ativar (macOS/Linux)
. .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### Criar projeto Django

```bash
django-admin startproject getit .
```

Arquivos gerados:

| Arquivo | Descrição |
|---|---|
| `manage.py` | Utilitário de comandos do projeto |
| `getit/settings.py` | Configurações do projeto (BD, apps, etc.) |
| `getit/urls.py` | Roteamento de URLs do projeto |
| `getit/wsgi.py` / `asgi.py` | Interface para servidores de produção |

### Executar o servidor de desenvolvimento

```bash
python manage.py runserver
# Acesse: http://localhost:8000
```

### Criar um app

No Django, **projeto** é o sistema completo; **app** é uma parte responsável por uma funcionalidade específica.

```bash
python manage.py startapp notes
```

Após criar, registrar o app em `getit/settings.py`:

```python
INSTALLED_APPS = [
    'notes.apps.NotesConfig',  # adicionar esta linha
    'django.contrib.admin',
    # ...
]
```

---

## 4. URLs e Views

### Arquivo `getit/urls.py` (URLs do projeto)

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # delega para o app notes
]
```

> A lista é percorrida **em ordem**. A string vazia `''` corresponde a qualquer caminho, por isso deve vir depois das rotas mais específicas.

### Arquivo `notes/urls.py` (URLs do app)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### View básica (`notes/views.py`)

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo!")
```

Uma **view** é uma função que recebe um objeto `request` e retorna uma `HttpResponse`.

---

## 5. Modelos (Models)

### Definindo um modelo (`notes/models.py`)

```python
from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}. {self.title}"
```

**Tipos de campo comuns:**

| Tipo | Uso |
|---|---|
| `CharField(max_length=N)` | Texto curto (limite de caracteres) |
| `TextField()` | Texto longo |
| `DateTimeField(auto_now_add=True)` | Data/hora, preenchida automaticamente na criação |
| `ForeignKey(Model, on_delete=...)` | Chave estrangeira (relacionamento) |

> O campo `id` é criado automaticamente pelo Django.

### Migrações

```bash
# Gerar arquivos de migração a partir dos modelos
python manage.py makemigrations

# Aplicar as migrações no banco de dados
python manage.py migrate
```

---

## 6. Django Admin

### Criar superusuário

```bash
python manage.py createsuperuser
```

### Registrar modelo no admin (`notes/admin.py`)

```python
from django.contrib import admin
from .models import Note

admin.site.register(Note)
```

Acesse em `http://localhost:8000/admin/`. O método `__str__` do modelo determina como cada objeto é exibido na lista.

---

## 7. QuerySets — Interação com o Banco de Dados

Toda classe de modelo possui um atributo `objects` para interagir com o banco:

```python
from .models import Note

# Todos os registros
all_notes = Note.objects.all()

# Filtrar
notes_by_user = Note.objects.filter(author=request.user)

# Excluir
other_notes = Note.objects.exclude(author=request.user)

# Ordenar (prefixo '-' para decrescente)
sorted_notes = Note.objects.order_by('-created_at')

# Encadeamento
notes = Note.objects.filter(author=request.user).order_by('-created_at')

# Buscar um único objeto
note = Note.objects.get(id=note_id)
```

**Criando e salvando objetos:**

```python
note = Note(title=title, content=content, author=request.user)
note.save()
```

**Apagando um objeto:**

```python
note = Note.objects.get(id=note_id)
note.delete()
```

---

## 8. Templates

### Estrutura de pastas

```
notes/
    templates/
        notes/
            base.html
            index.html
        registration/
            login.html
```

### Template base (`notes/templates/notes/base.html`)

```html
<!DOCTYPE html>
<html>
<head><title>Get-it</title></head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

### Template filho (`notes/templates/notes/index.html`)

```html
{% extends "notes/base.html" %}

{% block content %}
  <ul>
    {% for note in notes %}
      <li>{{ note.title }}</li>
    {% empty %}
      <li>Nenhuma anotação encontrada.</li>
    {% endfor %}
  </ul>
{% endblock %}
```

**Elementos do template Django:**

| Elemento | Sintaxe | Uso |
|---|---|---|
| Variável | `{{ variavel }}` | Exibe valor do contexto |
| Tag | `{% tag %}` | Lógica (`for`, `if`, `block`, etc.) |
| Filtro | `{{ var\|filtro }}` | Transforma valores |
| Comentário | `{# comentário #}` | Ignorado na renderização |

### Renderizando template na view

```python
from django.shortcuts import render
from .models import Note

def index(request):
    all_notes = Note.objects.order_by('-created_at')
    return render(request, 'notes/index.html', {'notes': all_notes})
```

O dicionário de contexto (`{'notes': all_notes}`) disponibiliza as variáveis no template.

---

## 9. Método POST — Formulários

### Verbos HTTP

- **GET**: solicita uma informação ao servidor (navegar para uma URL, clicar em link)
- **POST**: envia dados ao servidor (submeter formulário)

### Formulário HTML com POST e CSRF

```html
<form method="post" action="/">
  {% csrf_token %}
  <label for="titulo">Título</label>
  <input id="titulo" type="text" name="titulo" />

  <label for="detalhes">Detalhes</label>
  <textarea id="detalhes" name="detalhes"></textarea>

  <input type="submit" />
</form>
```

> `{% csrf_token %}` é obrigatório para proteção contra o ataque **Cross-Site Request Forgery (CSRF)**.

### View tratando GET e POST

```python
from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')

        note = Note(title=title, content=content)
        note.save()

        return redirect('index')  # PRG pattern: evita resubmissão
    else:
        all_notes = Note.objects.order_by('-created_at')
        return render(request, 'notes/index.html', {'notes': all_notes})
```

> O padrão **Post-Redirect-Get (PRG)** evita que o recarregamento da página reenvie o formulário.

---

## 10. Parâmetros de URL

Permitem capturar valores dinâmicos do caminho:

```python
# notes/urls.py
path('anotacoes/<int:note_id>/apagar', views.delete_note, name='delete-note')
```

```python
# notes/views.py
def delete_note(request, note_id):
    note = Note.objects.get(id=note_id)
    note.delete()
    return redirect('index')
```

`<int:note_id>` extrai um inteiro do caminho e o passa como argumento `note_id` para a view.

---

## 11. Arquivos Estáticos

Imagens, CSS e JavaScript são **arquivos estáticos** servidos pelo app `django.contrib.staticfiles`.

### Estrutura de pastas

```
notes/
    static/
        notes/
            img/
            style/
```

### Usando no template

```html
{% load static %}

<img src="{% static 'notes/img/logo-getit.png' %}" width="100" />
<link rel="stylesheet" href="{% static 'notes/style/main.css' %}" />
```

---

## 12. Autenticação

O Django inclui o app `django.contrib.auth` com modelos de usuário e views de autenticação prontas.

### Configurar URLs de autenticação (`getit/urls.py`)

```python
# Adicionar ANTES do include do app notes
path("accounts/", include("django.contrib.auth.urls"))
```

### Template de login (`notes/templates/registration/login.html`)

```html
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Entrar</button>
</form>
```

### Redirecionar após login/logout (`getit/settings.py`)

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

### Mostrar usuário logado no template

```html
<p>Olá, {{ user.first_name }} {{ user.last_name }}</p>
```

### Botão de logout (requer POST + CSRF)

```html
<form method="post" action="/accounts/logout/">
  {% csrf_token %}
  <button type="submit">Sair</button>
</form>
```

### Forçar login em uma view (`@login_required`)

```python
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    # Só executa se o usuário estiver autenticado
    ...
```

Se não autenticado, o usuário é redirecionado automaticamente para a página de login.

---

## 13. Relacionamentos Entre Modelos (ForeignKey)

### Definindo a chave estrangeira

```python
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
```

- `on_delete=models.CASCADE`: apaga as anotações quando o usuário for removido.

### Gerar e aplicar migrações após alteração

```bash
python manage.py makemigrations
python manage.py migrate
```

### Criando nota com autor

```python
Note.objects.create(title=title, content=content, author=request.user)
```

### Filtrando por relacionamento

```python
# Apenas anotações do usuário logado, ordenadas por data
notes = Note.objects.filter(author=request.user).order_by('-created_at')
```

> Filtrar antes de ordenar é mais eficiente, pois reduz o número de comparações na ordenação.

---

## 14. Deploy (Heroku)

### Dependências necessárias

```bash
pip install gunicorn whitenoise dj-database-url psycopg2-binary
pip freeze > requirements.txt
```

### `Procfile`

```
release: python manage.py migrate
web: gunicorn getit.wsgi
```

### Configurações em `settings.py` para produção

```python
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['seu-app.herokuapp.com', 'localhost', '127.0.0.1']

# WhiteNoise para arquivos estáticos
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Banco de dados com suporte a Postgres
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:////{(BASE_DIR / "db.sqlite3").absolute()}',
        conn_max_age=600,
        ssl_require=not DEBUG
    )
}
```

### Fazer o deploy

```bash
heroku login
heroku create
heroku git:remote -a nome-do-app
git push heroku main
```

---

## Referência Rápida: Comandos `manage.py`

| Comando | O que faz |
|---|---|
| `python manage.py runserver` | Inicia o servidor de desenvolvimento |
| `python manage.py startapp nome` | Cria a estrutura de um novo app |
| `python manage.py makemigrations` | Gera arquivos de migração a partir dos modelos |
| `python manage.py migrate` | Aplica as migrações no banco de dados |
| `python manage.py createsuperuser` | Cria um usuário administrador |
| `python manage.py collectstatic` | Coleta arquivos estáticos para produção |

---

## Sequência de Desenvolvimento (Checklist)

1. **Configuração**: criar venv → `startproject` → `startapp` → registrar app em `INSTALLED_APPS`
2. **Modelos**: definir classes em `models.py` → `makemigrations` → `migrate`
3. **Admin**: registrar modelos em `admin.py` → `createsuperuser` → adicionar dados pelo admin
4. **URLs e Views**: definir rotas em `urls.py` → implementar funções em `views.py`
5. **Templates**: criar arquivos HTML em `templates/` → usar `render()` na view
6. **Formulários POST**: adicionar `<form method="post">` + `{% csrf_token %}` → tratar `request.POST` na view
7. **Parâmetros de URL**: usar `<tipo:nome>` no `path()` → adicionar argumento na view
8. **Arquivos estáticos**: colocar em `static/` → usar `{% load static %}` e `{% static '...' %}` no template
9. **Autenticação**: incluir `django.contrib.auth.urls` → criar template de login → configurar redirecionamentos → usar `@login_required`
10. **Relacionamentos**: adicionar `ForeignKey` → migrations → filtrar QuerySets por relacionamento
