from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

import sentry_sdk

sentry_sdk.init(
    dsn="https://cc6f7d97e7b73a65a6d68c3e90b5a49b@o4507905759707136.ingest.us.sentry.io/4507905763180544",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w2t9w*&jcj&_$im2tyjnib7sosh#ve@lp&&2+mq!dn3arh0=q*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    "unfold",  # before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'compressor',

    'home',
    'user',
    'utils',

    # all auth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    "allauth.socialaccount.providers.github", # new
    'allauth.socialaccount.providers.openid_connect',

]
COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

# STATICFILES_FINDERS = ('compressor.finders.CompressorFinder',)
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <---- WhiteNoise!
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': '448289515098-mpp8859kia27bsvmrjid3ge7gbo6bquv.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'OAUTH_PKCE_ENABLED': True,
    },
    'github': {
        'SCOPE': [
            'profile',
            'email'
        ],
         'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': 'Ov23lirYDmOOZO4njcKP' ,
            'secret': '7d0a6d320b5f4afd90ecdee75dbbeeaf0a6563a8',
            'key': ''
        },
    },
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "linkedin",
                "name": "LinkedIn",
                "client_id": "77artcyzrcjbg4",
                "secret": "iOCQUAYrlgwXsY8D",
                "settings": {
                    "server_url": "https://www.linkedin.com/oauth",
                },
            }
        ]
    },
   

}
SITE_ID = 1

ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_ON_GET = True


TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

LANGUAGE_CODE = 'uz'
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'uploads'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
