import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_root.site_root.settings')

application = get_wsgi_application()
