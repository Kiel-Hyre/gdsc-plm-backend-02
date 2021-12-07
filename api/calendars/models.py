from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    time_start = models.TimeField()
    time_end = models.TimeField(null=True, blank=True)
    guests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='guests', blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Invite(models.Model):
    STATUS_ACCEPTED = 'accepted'
    STATUS_DENIED = 'denied'
    STATUS_PENDING = 'pending'

    STATUS_CHOICES = [
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_DENIED, 'Denied'),
        (STATUS_PENDING, 'Pending'),
    ]

    event = models.ForeignKey('calendars.Event', on_delete=models.CASCADE)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, default=STATUS_PENDING, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{event} invite to {user}'.format(event=self.event, user=self.to_user.username)


