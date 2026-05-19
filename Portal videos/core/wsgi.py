"""
WSGI config for the project.
"""
import os
from django.core.wsgi import get_wsgi_application

# Le indicamos a WSGI dónde encontrar tus configuraciones
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()