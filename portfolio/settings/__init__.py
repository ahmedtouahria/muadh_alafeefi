import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__ + "/../")))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-18+^q1qs43x*a#@_^%3zec2)qtu1%#78bo3(@!%fe2d=&7w8pu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_ui.apps.SimpleApp',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'colorfield',
    'django.contrib.admin',
'taggit',
'rest_framework',
    'constance',
    'constance.backends.database',
    'muadh'
]
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.FileField', {}],
    'email_field': ['django.forms.EmailField', {}],
    'file_field': ['django.forms.FileField', {}],
    'api_field': ['django.forms.JSONField', {
    }],
}
CONSTANCE_CONFIG = {
    'SITE_NAME': ("Muaadh alafifee", 'le nom de site Web'),
    'SITE_URL': ("http://localhost:8000", 'site url'),
    'PRIMARY_COLOR': ("#1967ee", 'primary color',),
    'PRIMARY_VIDEO': ("", 'primary video','file_field'),
    'Skills': ("", 'skills tags'),
    'LOGO': ("static/img/myphoto.png", 'Logo du site Web',"image_field"),
    'PRIMARY_IMAGE': ("static/img/myphoto.png", 'Logo du site Web',"image_field"),
    'Google_analytics_id': ('12345678', "l'identifiant de la vue analytics"),
    'Google_analytics_tag': ('UA-xxxxxxxx-1', "Tag de la balise"),
    'Google_analytics_credentials': ('{json}', "Votre clés d'API", 'api_field'),
    'ABOUT_YOUR_SELF':('about','about your self'),
    'INSTAGRAM_URL':('','URL de votre page Instagram'),
    'LINKED_URL':('','URL de votre page Instagram'),
    'TWITTER_URL':('','URL de votre page Instagram'),
    'WHATSAPP_NUMBER':('',' whatsapp number'),
    'CONTACT_NUMBER':('',' contact number'),
    'EMAIL':('',' your mail','email_field'),


}
CONSTANCE_CONFIG_FIELDSETS = {
    'GLOBAL': ('SITE_NAME', 'SITE_URL','PRIMARY_COLOR',),
    'About': ('PRIMARY_VIDEO', 'Skills','LOGO','PRIMARY_IMAGE',"ABOUT_YOUR_SELF"),
    'SOCIAL MEDIA': ('INSTAGRAM_URL','LINKED_URL','TWITTER_URL'),
    'google':('Google_analytics_id','Google_analytics_tag','Google_analytics_credentials'),
    'contact':('CONTACT_NUMBER','WHATSAPP_NUMBER','EMAIL'),


}
# Admin Ui configs

SIMPLEUI_CONFIG = {
    'system_keep':False,
    'menus': [

    {
        'app': 'muadh',
        'name': 'My website',
        'icon': 'fas fa-server',
        'models':[
        {
            'name': 'Utilisateurs',
            'icon': ' fa fa-user-plus',
            'url': 'auth/user'
        },
    {
        'app': 'constance',
        'name': 'Global',
        'icon': 'fas fa-cog',
        'url': 'constance/config/'
    },
        {
            'name': 'Skills',
            'icon': ' fa fa-file-image',
            'url': 'muadh/skill'
        },
        {
            'name': 'Experience',
            'icon': ' fa fa-lightbulb',
            'url': 'muadh/experience'
        },
                {
            'name': 'Education',
            'icon': ' fa fa-book',
            'url': 'muadh/education'
        },
    {
            'name': 'Testimonial',
            'icon': ' fa fa-quote-right',
            'url': 'muadh/testimonial'
        },
            {
            'name': 'Team Member',
            'icon': ' fa fa-users',
            'url': 'muadh/teammember'
        },
         {
            'name': 'Section Accueille',
            'icon': ' fa fa-tasks',
            'url': 'muadh/section'
        },
         {
            'name': 'Section Items',
            'icon': ' fa fa-tasks',
            'url': 'muadh/sectionitem'
        },
                 {
            'name': 'Messages',
            'icon': ' fa fa-envelope',
            'url': 'muadh/message'
        },
        ]
    },
    ]
}
CONSTANCE_IGNORE_ADMIN_VERSION_CHECK = True

SIMPLEUI_HOME_INFO = False
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_HOME_ACTION = False
SIMPLEUI_HOME_QUICK = False
SIMPLEUI_ANALYSIS = True
SIMPLEUI_HOME_TITLE = 'Mouadh alafifee'
# SIMPLEUI_LOGO = '/media/img/logo.png'
SIMPLEUI_DEFAULT_ICON = True
SIMPLEUI_DEFAULT_ICON = True
SIMPLEUI_DEFAULT_THEME = "blue.css"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

"""======================== EMAIL CONFIGURATION ========================"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_USER')  # change it from .env file !
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')


ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR + '/db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'portfolio/static')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # 'data' is my media folder
MEDIA_URL = '/media/'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
