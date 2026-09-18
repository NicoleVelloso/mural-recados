import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mural_recados.settings")

application = get_wsgi_application()

# A Vercel usa o nome `app` como handler
app = application
