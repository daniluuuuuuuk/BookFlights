from django.utils import timezone
from django.db import models as m
from apps.booking.models import Plane, Passenger
from django.urls import reverse


class Ticket(m.Model):
    date = m.DateField(blank=True, null=True, default=timezone.now)
    flight_number = m.CharField(max_length=6, unique=True)
    plane_info = m.ForeignKey(Plane, on_delete=m.CASCADE, related_name="tickets")
    passenger_info = m.ForeignKey(Passenger, on_delete=m.CASCADE, related_name="tickets")

    class Meta:
        verbose_name_plural = "tickets"
        ordering = ["pk"]

    def __repr__(self):
        return f"{self.__class__.__name__} №{self.pk}"

    def __str__(self):
        return f"Ticket № ({self.pk}): {self.passenger_info.surname}"

    def get_absolute_url(self):
        return f"{reverse('ticket-detail', args=[str(self.pk)])}"


