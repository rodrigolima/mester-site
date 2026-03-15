import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mester_site.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@mester.com.br', 'trilhas99')
    print('Superuser "admin" criado!')
else:
    print('Superuser "admin" já existe.')
