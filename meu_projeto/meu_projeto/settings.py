# Configuração do Django para o projeto 'meu_projeto'
import os
from pathlib import Path

# Caminho base para o projeto
BASE_DIR = Path(os.path.expanduser("~/lida-rpas/meu_projeto"))

# Chave secreta para a aplicação - mantenha-a em segredo em produção
SECRET_KEY = 'django-insecure-z1hrmhjw8t6=5y-u=zfvr0xf=q7=)^i3aj05@0_mtx*y3h^+nk'

# Ative o modo de depuração para desenvolvimento
DEBUG = True

# Defina hosts permitidos para segurança
ALLOWED_HOSTS = []

# Aplicações instaladas no projeto
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'processamento_imagens',  # Aplicativo customizado
]

# Middlewares para requisições HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Arquivo de URL principal
ROOT_URLCONF = 'meu_projeto.urls'

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'processamento_imagens', 'templates')],  # Caminho correto para templates
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

# Aplicação WSGI
WSGI_APPLICATION = 'meu_projeto.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Banco de dados SQLite
    },
}

# Validação de senhas para usuários
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configurações internacionais
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Configuração do URL para arquivos estáticos
STATIC_URL = '/static/'  # Define a URL base para acessar arquivos estáticos

# Diretórios para arquivos estáticos durante o desenvolvimento
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Diretório principal para arquivos estáticos
    os.path.join(BASE_DIR, 'static/imagens'),  # Subdiretório para imagens estáticas
]

# Diretório para arquivos estáticos após o uso do collectstatic (produção)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Diretório para arquivos estáticos em produção

# Campo primário padrão para modelos do Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
