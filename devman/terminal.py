import os
from datetime import timedelta

import django

from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from datacenter.models import Passcard, Visit

if __name__ == "__main__":
    # Программируем здесь
    print('Шаг 1')
    print('Количество пропусков:', Passcard.objects.count(), os.linesep)

    print('Шаг 2')
    print('Карточки пропусков:', Passcard.objects.all(), os.linesep)

    print('Шаг 3')
    any_passcard = Passcard.objects.all()[0]
    print('owner_name:', any_passcard.owner_name)
    print('passcode:', any_passcard.passcode)
    print('created_at:', any_passcard.created_at)
    print('is_active:', any_passcard.is_active, os.linesep)

    print('Шаг 4')
    print('Вcего пропусков:', Passcard.objects.count())
    passcards = Passcard.objects.all()
    active_passcards = []
    for passcard in passcards:
        if passcard.is_active:
            active_passcards.append(passcard)
    print('Активных пропусков:', len(active_passcards), os.linesep)

    print('Шаг 5')
    print('Вcего пропусков:', Passcard.objects.count())
    print('Активных пропусков:', Passcard.objects.filter(is_active=True).count(), os.linesep)

    print('Шаг 8')
    print('Визиты:', Visit.objects.all(), os.linesep)

    print('Шаг 9')
    print('Не закрытые визиты:', Visit.objects.filter(leaved_at=None).all(), os.linesep)

    print('Шаг 10')
    open_visits = Visit.objects.filter(leaved_at=None).all()
    for open_visit in open_visits:
        print('Зашёл в хранилище, время по Москве:')
        print(timezone.localtime(open_visit.entered_at), os.linesep)

        print('Находится в хранилище:')
        print(str(timezone.now() - open_visit.entered_at).split('.', 2)[0], os.linesep)


    print('Шаг 11')
    open_visits = Visit.objects.filter(leaved_at=None).all()
    for open_visit in open_visits:
        print(open_visit.passcard.owner_name)
    print(os.linesep, end='')

    print('Шаг 13')
    passcards = Passcard.objects.all()

    for i in range(passcards.count()):
        visits = Visit.objects.filter(passcard=passcards[i]).all()
        if visits.count() > 0:
            print(visits)
            break
    print(os.linesep, end='')


    print('Шаг 14')
    def get_duration(visit: Visit) -> timedelta:
        leaved_at = visit.leaved_at or timezone.now()
        duration = leaved_at - visit.entered_at
        return duration

    def is_visit_long(visit: Visit, minutes=60) -> bool:
        duration = get_duration(visit)
        return duration.total_seconds() > minutes * 60

    visits = Visit.objects.all()
    visits_10_minutes = []
    visits_1000_minutes = []
    for visit in visits:
        duration = get_duration(visit)
        if is_visit_long(visit, minutes=10):
            visits_10_minutes.append(visit)
        if is_visit_long(visit, minutes=1000):
            visits_1000_minutes.append(visit)
    print('Визиты дольше 10 минут: ', len(visits_10_minutes))
    print('Визиты дольше 1000 минут: ', len(visits_1000_minutes))

