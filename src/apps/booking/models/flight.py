from typing import NamedTuple, Text
from django.db import models as m
from django.urls import reverse
from utils.mixins import StrReprMixin
from django.conf import settings
from . import Plane


class Flight(StrReprMixin, m.Model):
    user = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE, related_name="user_flight")
    booked_plane = m.ForeignKey(Plane, on_delete=m.CASCADE, related_name="user_plane")

    class Meta:
        verbose_name_plural = "flights"
        ordering = ["user"]

    def __repr__(self) -> Text:
        return f'Flight {self.pk}: "{self.user_id}-{self.booked_plane}"'

    def get_absolute_url(self) -> Text:
        return f"{reverse('flight_add', args=[str(self.pk)])}"
