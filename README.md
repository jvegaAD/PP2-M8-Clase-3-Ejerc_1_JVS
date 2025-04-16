
# PP2-M8-Clase-3-Ejerc_1_JVS

Proyecto Django para el curso **Backend Python - PP2 Módulo 8 Clase 3**.

Este ejercicio implementa una API REST usando Django REST Framework, conectada a una base de datos PostgreSQL (local o Supabase), con despliegue opcional en [Render.com](https://render.com).

---

## 📦 Características

- Django 5.2
- Django REST Framework
- CRUD de **Autores** y **Libros**
- Vista de bienvenida HTML personalizada
- Configuración para desarrollo y producción
- Compatible con Render + WhiteNoise
- Entorno virtual gestionado vía `requirements.txt`

---

## 🚀 Cómo ejecutar el proyecto en local

### 1. Clona el repositorio

```bash
git clone https://github.com/jvegaAD/PP2-M8-Clase-3-Ejerc_1_JVS.git
cd PP2-M8-Clase-3-Ejerc_1_JVS
```

### 2. Crea el entorno virtual

```bash
python -m venv venv
venv\Scripts\activate  # En Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura el entorno

Copia el archivo de ejemplo:

```bash
copy .env.example .env
```

Edita `.env` y completa los datos si usarás PostgreSQL o Supabase.

### 5. Ejecuta migraciones

```bash
python manage.py migrate --settings=myproject.settings_dev
```

### 6. Inicia el servidor

```bash
python manage.py runserver --settings=myproject.settings_dev
```

---

## 🌐 Rutas principales

| Ruta               | Descripción                      |
|--------------------|----------------------------------|
| `/`                | Página de bienvenida             |
| `/admin/`          | Panel administrativo de Django   |
| `/api/autores/`    | API REST de Autores              |
| `/api/libros/`     | API REST de Libros               |

---

## 📡 Despliegue en Render (opcional)

1. Crear cuenta en [Render](https://render.com/)
2. Subir el proyecto a GitHub
3. Crear servicio tipo **Web Service**
4. Usar:
   - **Build command**: `./build.sh`
   - **Start command**:  
     ```bash
     python -m gunicorn myproject.asgi:application -k uvicorn.workers.UvicornWorker
     ```

5. Configurar variables de entorno en Render:

```
SECRET_KEY
PGDATABASE
PGUSER
PGPASSWORD
PGHOST
PGPORT
DEBUG
PRODUCTION_HOST
```

---

## 📄 Licencia

Proyecto desarrollado como parte del curso de Backend Python. Uso libre con fines educativos.

---
