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
    'bot',
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

ROOT_URLCONF = 'bot.urls'

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

WSGI_APPLICATION = 'bot.wsgi.application'


# Databasess
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    #  'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(PROJECT_DIR, 'yourdatabasename.db'),
    # }
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
STATIC_URL = '/static1/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static1'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['*']

SLACK_BOT_TOKEN = ""

PRIVATE_CHANNEL = "G7VKNRPM0"

MIXPANEL_TOKEN = "141c9f4b562b5b604f61bcdea7fd8264"

VOTE_PHRASE = "Hello, please rate your comfort in company"

TEXT_VOTE_PHRASE = " - rate from 1 to 10"

THANKS_PHRASE = "*Thanks! You replied with "

ALREADY_VOTED_PHRASE = "You already voted :) Thanks again"

NOT_IN_RANGE_PHRASE = "Thats not 1 and eather not a 10, and nothing between :sch:"

NOT_A_NUMBER_PHRASE = "Thats not a number, I'm Sorry"

BAD_CHANNEL_PHRASE = "You're not allowed to start the vote"

HELP = ">`/anon_msg`  *`your_msg`* - use it to send anonymus feedback, \n> ```example: /anon_msg our last party was too boring, please do something asap ```\n>`/anon_msg_random`  *`your_msg`* - use it to send anonymus message to *#random*, channel \n>```example: /anon_msg_rangom The event was perfect, tnx everyone```\n>`/start_temperature_vote` - use it to start default temperature vote \n>```example: /start_temperature_vote ```\n>`/start_question_vote` *`your_msg`* - use it to start question vote \n>```example: /start_question_vote What do you think about coffe in the kitchen ? ```\n>`/start_rating_vote` *`your_msg`* - use it to start custom text vote with rating \n>```example: /start_rating_vote How do you like our performance matrix ```\n>`/get_results` - use it to get results about last vote \n>```example: /get_results```\n>`/delivery` - use it to get list of delivery links \n>```example: /delivery ```\n>`/message_from_santa` - use it to reply anonymously as santa \n>```example: /message_from_santa  Ho-Ho-Ho You're welcome ```\n"

DELIVERY = "".join([">*Tiger Box* 0671550025 :tiger:\n>`https://www.instagram.com/p/BUhD1AGgIbJ/?taken-by=tigerboxternopil`\n>\n",
">*Avokado* 0975427570, 0660861908 :ramen:\n>`http://www.sushi.te.ua`\n>\n",
">*Barbaresco* 0506700400 :pizza:\n>`https://www.facebook.com/barbarescocitycafe/photos/a.1625890031071855.1073741829.1624010187926506/1894674224193433/?type=3&theater`\n>\n", 
">*Pork & chicken* 0677461813 :hamburger: \n>`https://www.facebook.com/burgerspc/photos/a.1734758993429283.1073741829.1662112834027233/1900835830154931/?type=3&theaterl`\n>\n",
">*Сицилія* 0977101033 :pizza:\n>`http://sicilia.te.ua/доставка-піци-тернопіль/`\n>\n",
">*Фламінго* 0983522222 :pizza:\n>`http://www.samogon.org/pizzeria_flamingo/menu-breakfast.php`\n>\n",
">*Ковчег* 0983522222 :spaghetti:\n>`http://www.samogon.org/kovcheg/menu.php`\n>\n",
">*Старий Млин* 0983522222 :stew:\n>`http://www.samogon.org/stary_mlyn/menu.php`\n>\n"]) 

NOONE_VOTED = "Noone voted right now"

PLEASE_REPLY_WITH_ANON = " - please reply with `/anon_msg` *`text`*"

CODING_ALGORITHM_NAME = "HS256"