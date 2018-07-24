
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'f#_m9bb2eg2uduwto!t-xj#0x*+n13j)w!%pn!ede4*8&$sp$8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'employeedb',
        'USER': 'db_user',
        'PASSWORD': 'db_-pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
