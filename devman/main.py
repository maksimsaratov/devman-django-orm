import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    print('Шаг 1')
    print('Количество пропусков:', Passcard.objects.count(), "\n")

    print('Шаг 2')
    print('Карточки пропусков:', Passcard.objects.all(), "\n")

    print('Шаг 3')
    any_passcard = Passcard.objects.all()[0]
    print('owner_name:', any_passcard.owner_name)
    print('passcode:', any_passcard.passcode)
    print('created_at:', any_passcard.created_at)
    print('is_active:', any_passcard.is_active, "\n")

    print('Шаг 4')
    print('ВСего пропусков:', Passcard.objects.count())
    print('Активных пропусков:', Passcard.objects.filter(is_active=True).count(), "\n")
