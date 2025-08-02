SECRET_KEY = 'dummykey'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'myapp',
]

MIDDLEWARE = []
ROOT_URLCONF = 'myproject.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
TEMPLATES = []
WSGI_APPLICATION = ''
