#!/usr/bin/env bash

# Activar modo estricto
set -o errexit
set -o pipefail
set -o nounset

# Comandos para preparación del entorno
echo "✔ Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✔ Aplicando migraciones..."
python manage.py migrate

echo "✔ Recolectando archivos estáticos..."
python manage.py collectstatic --no-input
