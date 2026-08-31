import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_main.settings')

import django
django.setup()

from django.core.management import call_command
from django.db.utils import ProgrammingError, OperationalError

try:
    call_command('migrate', interactive=False, verbosity=0)
except (ProgrammingError, OperationalError):
    call_command('migrate', interactive=False, verbosity=0, fake_initial=True)

if os.getenv('DJANGO_SUPERUSER_USERNAME') and os.getenv('DJANGO_SUPERUSER_PASSWORD'):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username=os.getenv('DJANGO_SUPERUSER_USERNAME')).exists():
        User.objects.create_superuser(
            username=os.getenv('DJANGO_SUPERUSER_USERNAME'),
            email=os.getenv('DJANGO_SUPERUSER_EMAIL', ''),
            password=os.getenv('DJANGO_SUPERUSER_PASSWORD'),
        )

from blog_main.wsgi import application

app = application
