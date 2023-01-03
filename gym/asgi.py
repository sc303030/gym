"""
ASGI config for gym project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from get_setting import get_setting

setting = get_setting()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", setting)

application = get_asgi_application()
