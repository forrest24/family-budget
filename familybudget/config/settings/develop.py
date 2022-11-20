import socket

from .base import *  # noqa
from .base import env  # noqa

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

STATIC_URL = "static/"
STATICFILES_DIRS = [ROOT_DIR / "static"]

SECRET_KEY = "dev_secret_key"
DEBUG = True
ALLOWED_HOSTS = []

THIRD_PARTY_APPS.append("debug_toolbar")
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
