import os
import sys
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from datacenter.models import Passcard, Visit


if __name__ == "__main__":
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())

    passcards = Passcard.objects.all()
    print('Карточки пропусков:', passcards, "\n")

    passcard = passcards[0]
    print('owner_name:', passcard.owner_name)
    print('passcode:', passcard.passcode)
    print('created_at:', passcard.created_at)
    print('is_active:', passcard.is_active)
