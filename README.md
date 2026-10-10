# MiniTools

Utilitários web em Django: calculadora e validador/gerador de CPF.

## Requisitos

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (recomendado) ou pip

## Setup

```bash
uv sync
cp .env.example .env
uv run python manage.py migrate
uv run python manage.py runserver
```

Sem uv:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -e .
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Abra [http://127.0.0.1:8000/calculator/](http://127.0.0.1:8000/calculator/).

## URLs

| Ferramenta        | Caminho            |
|-------------------|--------------------|
| Calculadora       | `/calculator/`     |
| Validador de CPF  | `/documents/cpf/`  |

## Estrutura

```
Minitools/
├── setup/                 # settings, urls, wsgi/asgi
├── calculator/            # app da calculadora
├── documents_validator/   # app de documentos (CPF)
├── templates/global/      # layout compartilhado
└── static/global/         # CSS/imagens globais
```

Cada app guarda templates em `templates/<app>/pages/`, estáticos em `static/<app>/` e lógica em `utils/`.

## Configuração

Variáveis em `.env` (veja `.env.example`):

- `SECRET_KEY` — obrigatória em produção
- `DEBUG` — `True` só em desenvolvimento
- `ALLOWED_HOSTS` — hosts separados por vírgula

## Desenvolvimento

```bash
uv run python manage.py test
uv run python manage.py check
```
