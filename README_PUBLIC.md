
# 🐍 Proyecto Django - PP2 M8 Clase 3 | Ejercicio 1

Despliegue en la nube de una API REST desarrollada en Django 5.2 para el curso de **Backend Python**.

---

## 🌐 Enlace en línea

🔗 Accede aquí: [pp2-m8-clase-3-ejerc-1-jvs.onrender.com](https://pp2-m8-clase-3-ejerc-1-jvs.onrender.com)

---

## 🚀 Tecnologías utilizadas

- Django 5.2
- Django REST Framework
- Gunicorn + Uvicorn Worker
- PostgreSQL (Supabase)
- Render.com (Despliegue)
- Python-dotenv + WhiteNoise

---

## 📦 Funcionalidades

- CRUD completo de Autores y Libros
- API navegable con Django REST Framework
- Panel de administración Django disponible
- Página de bienvenida personalizada en `/`
- Configuración lista para producción en Render

---

## 📄 Instrucciones de uso

1. Clona el repositorio  
2. Crea entorno virtual  
3. Instala requerimientos  
4. Configura variables en `.env`  
5. Ejecuta migraciones y levanta el servidor local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Variables de entorno requeridas

```env
SECRET_KEY=...
DEBUG=False
PGDATABASE=...
PGUSER=...
PGPASSWORD=...
PGHOST=...
PGPORT=6543
PRODUCTION_HOST=pp2-m8-clase-3-ejerc-1-jvs.onrender.com
```

---

## ✨ Desarrollado por

👤 [jvegaAD](https://github.com/jvegaAD)

---

> Proyecto educativo desarrollado como parte de la formación en backend con Django.  
> ¡Gracias por visitar! ⭐️
