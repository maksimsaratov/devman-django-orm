from django.utils import timezone

from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    # Программируем здесь
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None).all()
    for visit in visits:
        non_closed_visits.append({
            "who_entered": visit.passcard.owner_name,
            "entered_at": timezone.localtime(visit.entered_at),
            "duration": format_duration(get_duration(visit)),
        })
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)


def get_duration(visit):
    duration = timezone.now() - visit.entered_at
    return duration


def format_duration(duration):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    mins = int((total_seconds % 3600) // 60)
    formatted_mins = ('0' + str(mins))[-2:]
    formatted_duration = f"{hours}:{formatted_mins}"
    return formatted_duration
