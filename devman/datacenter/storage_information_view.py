from django.utils import timezone

from datacenter.models import Visit
from django.shortcuts import render

from datacenter.utils import get_duration, format_duration


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
