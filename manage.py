import os

from django.core.management import execute_from_command_line

from project.settings import env

if not env('DJANGO_SECRET_KEY'):
    raise SystemExit('DJANGO_SECRET_KEY not exist')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 127.0.0.1:8001'.split())
