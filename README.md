Ini adalah sebuah tes project dari suatu company, disini saya disuruh membuat applikasi product management, saya kerjakan dengan Django + HTMX + DaisyUI.

## Tech Stack

- **Backend**: Django 6.0
- **Frontend**: HTMX + TailwindCSS + DaisyUI
- **Database**: PostgreSQL
- **Package Manager**: uv

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (Python package manager)
- Docker atau Podman

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/JiMarchel/test-fast-print.git
cd fast_print
```

### 2. Jalankan Database

Menggunakan Docker:

```bash
docker compose up -d
```

Atau menggunakan Podman:

```bash
podman-compose up -d
```

Database akan berjalan di:

- **PostgreSQL**: `localhost:5432`
- **Adminer** (DB GUI): `localhost:8081`

Kredensial database:
| Key | Value |
|-----|-------|
| Database | fastprint_db |
| User | postgres |
| Password | postgres |

### 3. Install Dependencies

```bash
uv sync
```

### 4. Migrasi Database

```bash
uv run manage.py migrate
```

### 5. Seed Data Produk

Fetch data produk dari API eksternal:

```bash
uv run manage.py seed_products
```

### 6. Jalankan Development Server

```bash
uv run manage.py runserver
```

Buka browser di `http://localhost:8000`

## Project Structure

```
fast_print/
├── config/                 # Django settings
├── product/                # Product app
│   ├── templates/
│   │   ├── index.html      # Main page
│   │   └── partials/       # HTMX partials
│   ├── views.py            # View functions
│   ├── models.py           # Database models
│   ├── forms.py            # Django forms
│   ├── helper.py           # Utility functions & decorators
│   └── urls.py             # URL routes
├── docker-compose.yml      # Database container
├── pyproject.toml          # Python dependencies
└── manage.py               # Django CLI
```
