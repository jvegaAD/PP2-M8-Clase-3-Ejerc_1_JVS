
# Proyecto: PP2-M8-Clase-3-Ejerc_1

## Descripción
Aplicación Django con conexión a base de datos PostgreSQL en Supabase, desplegada en Render.
Incluye:
- Panel de administración de Django
- API REST para modelos de Autores y Libros
- Interfaz principal con acceso directo a endpoints y admin

---

## Requisitos

- Python 3.11+
- Django 5.2
- PostgreSQL (usando Supabase como proveedor)
- Gunicorn
- Uvicorn
- Render para despliegue gratuito

---

## Instalación local

```bash
python -m venv venv
source venv/bin/activate  # en Linux/Mac
venv\Scripts\activate    # en Windows
pip install -r requirements.txt
```

---

## Variables de entorno `.env`
Crear un archivo `.env` basado en `.env.example`:

```
DB_HOST=aws-0-us-east-1.pooler.supabase.com
DB_PORT=6543
DB_NAME=postgres
DB_USER=postgres.xxxxxxxx
DB_PASSWORD=**********
SECRET_KEY=clave_secreta_django
DEBUG=False
ALLOWED_HOSTS=pp2-m8-clase-3-ejerc-1-jvs.onrender.com,localhost,127.0.0.1
```

---

## Comandos de uso local

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```

---

## Despliegue en Render

### 1. Requisitos
- Repositorio en GitHub
- Cuenta gratuita en Render

### 2. Archivos necesarios
- `render.yaml`
- `requirements.txt`
- `build.sh`

### 3. Variables en Render (copiar desde `.env`)

Agregar en Settings > Environment > Add from .env

### 4. Comando de inicio

```bash
gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

---

## Errores frecuentes y soluciones

### ❌ DisallowedHost
Agregar tu dominio Render a `ALLOWED_HOSTS` en `.env`.

### ❌ Estilos rotos en admin o DRF
Ejecutar:
```bash
python manage.py collectstatic
```
Y confirmar subida al repo:
```bash
git add staticfiles/
git commit -m "🚀 Subir archivos estáticos"
git push
```

---

## Vista final
- Inicio con 3 botones: API Autores, API Libros, Admin 📄
- Endpoints funcionales con DRF 🚀
- Panel Admin estilizado correctamente 📁

---

## Autor
Juan - Curso Backend Python PP2 - Módulo 8 - Clase 3
