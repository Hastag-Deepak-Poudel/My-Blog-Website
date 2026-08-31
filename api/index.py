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

from blog_main.wsgi import application

app = application
