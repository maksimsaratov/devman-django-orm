from django.utils import timezone

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

from datacenter.utils import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    # Программируем здесь

    visits = Visit.objects.filter(passcard=passcard).all()
    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append({
            "entered_at": timezone.localtime(visit.entered_at),
            "duration": format_duration(get_duration(visit), include_seconds=True),
            "is_strange": is_visit_long(visit)
        })

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
