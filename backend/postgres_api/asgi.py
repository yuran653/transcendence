"""
ASGI config for postgres_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

from os import environ
from django.core.asgi import get_asgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', 'postgres_api.settings')

application = get_asgi_application()
