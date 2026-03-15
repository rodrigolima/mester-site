#!/usr/bin/env python
"""Script de inicialização para Railway - roda migrate, loaddata e cria superuser."""
import subprocess
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mester_site.settings')

# Migrate
print("=" * 50)
print("RUNNING MIGRATE")
print("=" * 50)
subprocess.run([sys.executable, 'manage.py', 'migrate', '--noinput'], check=True)

# Collectstatic
print("=" * 50)
print("RUNNING COLLECTSTATIC")
print("=" * 50)
subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)

# Loaddata
print("=" * 50)
print("RUNNING LOADDATA")
print("=" * 50)
try:
    subprocess.run([sys.executable, 'manage.py', 'loaddata', 'initial_data'], check=True)
    print("Fixture loaded successfully!")
except Exception as e:
    print(f"Loaddata error (may be OK): {e}")

# Create superuser
print("=" * 50)
print("CREATING SUPERUSER")
print("=" * 50)
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()

for username in ['admin', 'admin2']:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, f'{username}@mester.com.br', 'trilhas99')
        print(f'Superuser "{username}" criado!')
    else:
        print(f'Superuser "{username}" já existe.')

print("=" * 50)
print("SETUP COMPLETE - Starting gunicorn...")
print("=" * 50)
