import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Reemplazar la SECRET_KEY que viene por defecto por la del .env
SECRET_KEY = 'a-32001919'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Nuestras Apps
    'cursos',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Videos',
        'USER': 'avnadmin',
        'PASSWORD': 'AVNS_S5T0x2XItRusc6d0nqY',
        'HOST': 'mysql-25bb01e4-sneyeduardo3-04eb.k.aivencloud.com',
        'PORT': '23153',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # AGREGAR BASE_DIR AQUÍ:
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = 'static/'

# Le decimos a Django dónde están nuestros archivos estáticos
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]   

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- ¡AGREGA ESTA LÍNEA AQUÍ!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# Modo desarrollo activado para ver los errores detallados si algo falla
DEBUG = True

# Permitimos que corra en tu servidor local
ALLOWED_HOSTS = ['*']

# Le indica a Django dónde está el archivo principal de rutas
ROOT_URLCONF = 'core.urls'

# También es buena práctica asegurar que tenga la ruta WSGI por si falta
WSGI_APPLICATION = 'core.wsgi.application'

# --- CONFIGURACIÓN DE REDIRECCIONES DE SESIÓN ---
# A dónde ir después de iniciar sesión con éxito (al dashboard)
LOGIN_REDIRECT_URL = '/'

# A dónde enviar a alguien si intenta entrar a una página prohibida sin iniciar sesión
LOGIN_URL = '/login/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Le decimos a Django que use WhiteNoise para comprimir y cachear el CSS de forma ultra rápida
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
