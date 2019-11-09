from math import sqrt

from django.db import models as m

from apps.booking.models import City


class Plane(m.Model):
    plane_model = m.CharField(max_length=20, unique=True, default='AirBus A319')
    dep_station = m.ForeignKey("City", on_delete=m.CASCADE, related_name='departure_plane')
    arr_station = m.ForeignKey("City", on_delete=m.CASCADE, related_name='arrival_plane')
    dep_time = m.TimeField()
    arr_time = m.TimeField()

    class Meta:
        verbose_name_plural = "planes"
        ordering = ["dep_station"]

    def __repr__(self):
        return f"Plane №{self.pk}: from {self.dep_station} to {self.arr_station}"

    def __str__(self):
        return f"{self.dep_station} - {self.arr_station}"

    def distance(self):
        degrees = sqrt(
            (self.arr_station.lat - self.dep_station.lat) ** 2 + (self.arr_station.lon - self.dep_station.lon) ** 2
        )
        return degrees * 64.321
