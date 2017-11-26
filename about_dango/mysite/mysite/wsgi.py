"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
>>>>>>> 4d8e22026e5388c256224a40b4173f3ca4f93392
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_wsgi_application()
