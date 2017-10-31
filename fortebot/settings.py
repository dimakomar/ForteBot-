"""
Django settings for fortebot project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd$f=d0)$$m&*+b#_xe&w2i!fj#5yaee^=%xqsppd=3i1=tz33i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fortebot',
    'after_response',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fortebot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'fortebot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']

SLACK_BOT_TOKEN = ""

PRIVATE_CHANNEL = "G7NUMC5FA"

MIXPANEL_TOKEN = "25d7ff3a1420b04b66b09bf53c7768af"

VOTE_PHRASE = "Hello, pls rate your team temperature from 1 to 10"

TEXT_VOTE_PHRASE = " - rate from 1 to 10"

THANKS_PHRASE = "Thanks"

ALREADY_VOTED_PHRASE = "You already voted :) Thanks again"

NOT_IN_RANGE_PHRASE = "Thats not 1 and eather not a 10, and nothing between :shc:"

NOT_A_NUMBER_PHRASE = "Thats not a number, I'm Sorry"

BAD_CHANNEL_PHRASE = "You're not allowed to start the vote"

HELP = ">`/anon_msg`  *`your_msg`* - Use it to send anonymus feedback, \n> ```example: /anon_msg our last party was too boring, please do something asap ``` \n>`/anon_msg_rangom`  *`your_msg`* - Use it to send anonymus message to *#random*, channel \n>```example: /anon_msg our last party was too boring, please do something asap ```\n>`/start_temperature_vote` - Use it to start default temperature vote \n>```example: /anon_msg our last party was too boring, please do something asap ```\n>`/start_question_vote` *`your_msg`* - Use it to start question vote \n>```example: /anon_msg our last party was too boring, please do something asap ```\n>`/start_rating_vote` *`your_msg`* - Use it to start custom text vote with rating \n>```example: /anon_msg our last party was too boring, please do something asap ```\n>`/get_results` - Use it to get results about last vote \n>`/delivery` - Use it to get list of delivery links \n>```example: /anon_msg our last party was too boring, please do something asap ```\n"

DELIVERY = "".join([">*Tiger Box* 0671550025 :tiger:\n>`https://www.instagram.com/p/BUhD1AGgIbJ/?taken-by=tigerboxternopil`\n>\n",
">*Avokado* 0975427570, 0660861908 :ramen:\n>`http://www.sushi.te.ua`\n>\n",
">*Barbaresco* 0506700400 :pizza:\n>`https://www.facebook.com/barbarescocitycafe/photos/a.1625890031071855.1073741829.1624010187926506/1894674224193433/?type=3&theater`\n>\n", 
">*Pork & chicken* 0677461813 :hamburger: \n>`https://www.facebook.com/burgerspc/photos/a.1734758993429283.1073741829.1662112834027233/1900835830154931/?type=3&theaterl`\n>\n",
">*Сицилія* 0977101033 :pizza:\n>`http://sicilia.te.ua/доставка-піци-тернопіль/`\n>\n",
">*Фламінго* 0983522222 :pizza:\n>`http://www.samogon.org/pizzeria_flamingo/menu-breakfast.php`\n>\n",
">*Ковчег* 0983522222 :spaghetti:\n>`http://www.samogon.org/kovcheg/menu.php`\n>\n",
">*Старий Млин* 0983522222 :stew:\n>`http://www.samogon.org/stary_mlyn/menu.php`\n>\n"]) 

NOONE_VOTED = "Noone voted right now"

PLEASE_REPLY_WITH_ANON = " - please reply with `/anon_msg`"

