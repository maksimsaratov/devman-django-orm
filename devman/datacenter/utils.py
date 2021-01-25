from datetime import timedelta

from django.utils import timezone


def get_duration(visit) -> timedelta:
    duration = timezone.now() - visit.entered_at
    return duration


def format_duration(duration: timedelta):
    total_seconds = duration.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    formatted_minutes = ('0' + str(minutes))[-2:]
    formatted_duration = f"{hours}:{formatted_minutes}"
    return formatted_duration
