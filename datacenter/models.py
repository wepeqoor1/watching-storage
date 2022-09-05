from datetime import datetime, timedelta

from django.db import models
from django.utils.timezone import localtime


def format_values(seconds: float) -> str:
    """Formatting seconds to ISO format"""
    return str(timedelta(seconds=seconds))


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    @property
    def get_duration(self) -> float:
        """Calculate duration visit"""
        entered_at = localtime(self.entered_at).replace(tzinfo=None)
        if not self.leaved_at:
            datetime_now = datetime.now()
            return (datetime_now - entered_at).total_seconds()
        else:
            leaved_at = localtime(self.leaved_at).replace(tzinfo=None)
            return (leaved_at - entered_at).total_seconds()

    @property
    def is_visit_long(self, limit_minutes=60) -> bool:
        seconds_in_minute = 60
        visit_time = self.get_duration
        return visit_time // seconds_in_minute > limit_minutes
