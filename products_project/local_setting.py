# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9a4x!xy&eip*-xn(=_ffk=xb7+!=ydwo9w_e(6o=bt5$&^6lj_'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'product_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password',

        }
}