"""
WSGI config for pizzaking_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# 1. Set Django settings FIRST
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaking_backend.settings')

# 2. Initialize Django application (this sets up everything)
application = get_wsgi_application()

# 3. NOW import and call your startup function (after Django is ready)
from load_pizzas_startup import run as load_pizzas_startup
load_pizzas_startup()