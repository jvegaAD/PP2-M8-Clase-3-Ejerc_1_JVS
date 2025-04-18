"""
Django settings for myproject project.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde .env (localmente)

BASE_DIR = Path(__file__).resolve().parent.parent

# Seguridad: Obtener SECRET_KEY de la variable de entorno
SECRET_KEY = os.environ.get("SECRET_KEY")

# Si no se encuentra SECRET_KEY, levantar una excepción (¡CRÍTICO!)
if not SECRET_KEY:
    raise ValueError("La variable de entorno SECRET_KEY no está definida.")


# Debug
DEBUG = os.environ.get("DEBUG", "False") == "True"  # "False" como string

ALLOWED_HOSTS = [os.environ.get("PRODUCTION_HOST"), "localhost", "127.0.0.1"]


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "rest_framework",
    "myapp.apps.MyappConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "myproject.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "myproject.wsgi.application"


# Configuración de la Base de Datos
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("PGDATABASE"),
        "USER": os.environ.get("PGUSER"),
        "PASSWORD": os.environ.get("PGPASSWORD"),
        "HOST": os.environ.get("PGHOST"),
        "PORT": int(os.environ.get("PGPORT", "5432")),  # PORT as integer!
        "OPTIONS": {"sslmode": "require"},
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Archivos estáticos
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "WARNING",  # Nivel de log según DEBUG
    },
}



# """
# Django settings for myproject project.

# Generated by 'django-admin startproject' using Django 5.2.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.2/ref/settings/
# """
# import os
# from pathlib import Path

# from dotenv import load_dotenv

# load_dotenv()

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = os.environ.get(
#     "SECRET_KEY", "django-insecure-3r4y$y04o#(n+1v0+gdpggwiq!v=g$b*0@b(c1_*uxq3t_5eh^"
# )

# DEBUG = os.environ.get("DEBUG", "True") == "True"

# ALLOWED_HOSTS = [
#     os.environ.get("PRODUCTION_HOST"),
#     "localhost",
#     "127.0.0.1",
# ]

# INSTALLED_APPS = [
#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "whitenoise.runserver_nostatic",
#     "django.contrib.staticfiles",
#     "rest_framework",
#     "myapp.apps.MyappConfig",
# ]

# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "whitenoise.middleware.WhiteNoiseMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "myproject.urls"

# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         "DIRS": [],
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = "myproject.wsgi.application"

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.environ.get("PGDATABASE"),
#         "USER": os.environ.get("PGUSER"),
#         "PASSWORD": os.environ.get("PGPASSWORD"),
#         "HOST": os.environ.get("PGHOST"),
#         "PORT": os.environ.get("PGPORT", 5432),
#         "OPTIONS": {
#             "sslmode": "require",
#         },
#         "DISABLE_SERVER_SIDE_CURSORS": True,
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# USE_I18N = True
# USE_TZ = True

# # ✅ Archivos estáticos (CSS, JS, imágenes)
# STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# if not DEBUG:
#     STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "DEBUG" if DEBUG else "WARNING",
#     },
# }
