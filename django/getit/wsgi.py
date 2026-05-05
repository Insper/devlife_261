"""WSGI config for getit project."""
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "getit.settings")

application = get_wsgi_application()
