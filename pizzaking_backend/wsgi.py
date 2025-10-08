"""
WSGI config for pizzaking_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from load_pizzas_startup import run as load_pizzas_startup
load_pizzas_startup()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaking_backend.settings')

application = get_wsgi_application()
