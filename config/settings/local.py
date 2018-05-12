from .base import *
from datetime import timedelta

SECRET_KEY = env('DJANGO_SECRET_KEY', default='(&w$dryiavve#a6vk9hg9nm194lhb$%mn1cs$z-i!i3%pi&w)8')

DEBUG = env.bool('DJANGO_DEBUG', default=True)

TOKEN_EXPIRE = env('ACCESS_TOKEN_LIFETIME', default=5)

ALLOWED_HOSTS = ["*"]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=TOKEN_EXPIRE),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}