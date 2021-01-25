from datetime import timedelta

from django.utils import timezone

from datacenter.models import Visit


def get_duration(visit: Visit) -> timedelta:
    leaved_at = visit.leaved_at or timezone.now()
    duration = leaved_at - visit.entered_at
    return duration


def format_duration(duration: timedelta, include_seconds=False) -> str:
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    formatted_minutes = ('0' + str(minutes))[-2:]
    formatted_duration = f"{hours}:{formatted_minutes}"

    if include_seconds:
        seconds = int(total_seconds % 60)
        formatted_seconds = ('0' + str(seconds))[-2:]
        formatted_duration = f"{formatted_duration}:{formatted_seconds}"

    return formatted_duration


def is_visit_long(visit: Visit, minutes=60) -> bool:
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60
