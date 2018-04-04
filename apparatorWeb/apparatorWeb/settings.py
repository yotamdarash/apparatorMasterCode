"""
Django settings for apparatorWeb project.

Generated by 'django-admin startproject' using Django 1.11.11.

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
SECRET_KEY = '719y8alf*3@ixk1)zld9r7-$om3by&eg2h7=-x6)zmf8ebvh8='

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
    'words.apps.WordsConfig',
    'debug_toolbar',
    # 'django_tables2',
    'django.contrib.humanize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'apparatorWeb.urls'

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

WSGI_APPLICATION = 'apparatorWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'app',
        'USER': 'root',
        'PASSWORD': 'ucdsyz',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'TRADITIONAL',
            'charset': 'utf8mb4',
            'init_command': 'SET '
                            'default_storage_engine=INNODB,'
                            'character_set_connection=utf8mb4,'
                            'collation_connection=utf8_bin',
        }
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'OPTIONS': {
            'options': '-c search_path=app'
        },
        'NAME': 'app',
        'USER': 'postgres',
        'PASSWORD': 'ucdsyz',
        'HOST': 'localhost',
        'PORT': '5432',
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

INTERNAL_IPS = ['127.0.0.1']

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# updated list at the bottom of this page: https://affiliate.itunes.apple.com/resources/documentation/linking-to-the-itunes-music-store/
APPLE_APP_STORE_COUNTRY_CODES = {
    'Algeria': 'DZ',
    'Angola': 'AO',
    'Anguilla': 'AI',
    'Antigua & Barbuda': 'AG',
    'Argentina': 'AR',
    'Armenia': 'AM',
    'Australia': 'AU',
    'Austria': 'AT',
    'Azerbaijan': 'AZ',
    'Bahrain': 'BH',
    'Bangladesh': 'BD',
    'Barbados': 'BB',
    'Belarus': 'BY',
    'Belgium': 'BE',
    'Belize': 'BZ',
    'Bermuda': 'BM',
    'Bolivia': 'BO',
    'Botswana': 'BW',
    'Brazil': 'BR',
    'British Virgin Islands': 'VG',
    'Brunei': 'BN',
    'Bulgaria': 'BG',
    'Canada': 'CA',
    'Cayman Islands': 'KY',
    'Chile': 'CL',
    'China': 'CN',
    'Colombia': 'CO',
    'Costa Rica': 'CR',
    'Cote D\'Ivoire': 'CI',
    'Croatia': 'HR',
    'Cyprus': 'CY',
    'Czech Republic': 'CZ',
    'Denmark': 'DK',
    'Dominica': 'DM',
    'Dominican Rep.': 'DO',
    'Ecuador': 'EC',
    'Egypt': 'EG',
    'El Salvador': 'SV',
    'Estonia': 'EE',
    'Finland': 'FI',
    'France': 'FR',
    'Germany': 'DE',
    'Ghana': 'GH',
    'Greece': 'GR',
    'Grenada': 'GD',
    'Guatemala': 'GT',
    'Guyana': 'GY',
    'Honduras': 'HN',
    'Hong Kong': 'HK',
    'Hungary': 'HU',
    'Iceland': 'IS',
    'India': 'IN',
    'Indonesia': 'ID',
    'Ireland': 'IE',
    'Israel': 'IL',
    'Italy': 'IT',
    'Jamaica': 'JM',
    'Japan': 'JP',
    'Jordan': 'JO',
    'Kazakstan': 'KZ',
    'Kenya': 'KE',
    'Korea, Republic Of': 'KR',
    'Kuwait': 'KW',
    'Latvia': 'LV',
    'Lebanon': 'LB',
    'Liechtenstein': 'LI',
    'Lithuania': 'LT',
    'Luxembourg': 'LU',
    'Macau': 'MO',
    'Macedonia': 'MK',
    'Madagascar': 'MG',
    'Malaysia': 'MY',
    'Maldives': 'MV',
    'Mali': 'ML',
    'Malta': 'MT',
    'Mauritius': 'MU',
    'Mexico': 'MX',
    'Moldova, Republic Of': 'MD',
    'Montserrat': 'MS',
    'Nepal': 'NP',
    'Netherlands': 'NL',
    'New Zealand': 'NZ',
    'Nicaragua': 'NI',
    'Niger': 'NE',
    'Nigeria': 'NG',
    'Norway': 'NO',
    'Oman': 'OM',
    'Pakistan': 'PK',
    'Panama': 'PA',
    'Paraguay': 'PY',
    'Peru': 'PE',
    'Philippines': 'PH',
    'Poland': 'PL',
    'Portugal': 'PT',
    'Qatar': 'QA',
    'Romania': 'RO',
    'Russia': 'RU',
    'Saudi Arabia': 'SA',
    'Senegal': 'SN',
    'Serbia': 'RS',
    'Singapore': 'SG',
    'Slovakia': 'SK',
    'Slovenia': 'SI',
    'South Africa': 'ZA',
    'Spain': 'ES',
    'Sri Lanka': 'LK',
    'St. Kitts & Nevis': 'KN',
    'St. Lucia': 'LC',
    'St. Vincent & The Grenadines': 'VC',
    'Suriname': 'SR',
    'Sweden': 'SE',
    'Switzerland': 'CH',
    'Taiwan': 'TW',
    'Tanzania': 'TZ',
    'Thailand': 'TH',
    'The Bahamas': 'BS',
    'Trinidad & Tobago': 'TT',
    'Tunisia': 'TN',
    'Turkey': 'TR',
    'Turks & Caicos': 'TC',
    'Uganda': 'UG',
    'UK': 'GB',
    'Ukraine': 'UA',
    'United Arab Emirates': 'AE',
    'Uruguay': 'UY',
    'USA': 'US',
    'Uzbekistan': 'UZ',
    'Venezuela': 'VE',
    'Vietnam': 'VN',
    'Yemen': 'YE',
}