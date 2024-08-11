"""
WSGI config for postgres_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

from os import environ
from django.core.wsgi import get_wsgi_application

environ.setdefault('DJANGO_SETTINGS_MODULE', 'postgres_api.settings')

application = get_wsgi_application()
