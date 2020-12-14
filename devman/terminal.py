import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Passcard, Visit

if __name__ == "__main__":
    # Программируем здесь
    print('Шаг 8')
    print('Визиты:', Visit.objects.all(), "\n")
