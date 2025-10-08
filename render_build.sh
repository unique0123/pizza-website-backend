#!/usr/bin/env bash
# Exit on error
set -o errexit  

# Install dependencies
pip install -r requirements.txt

# Run migrations automatically
python manage.py migrate

# Collect static files (optional but good practice)
python manage.py collectstatic --noinput