from math import sqrt
from django.db import models as m
from apps.booking.models import City
from django.urls import reverse
from django.conf import settings


class Plane(m.Model):
    ECONOMY = 'ЭК'
    COMFORT = 'КМФ'
    BUSINESS = 'БИЗ'
    FIRST_CLASS = 'ПКЛ'
    CLASSES = [
        (ECONOMY, "Эконом"),
        (COMFORT, "Комфорт"),
        (BUSINESS, "Бизнес"),
        (FIRST_CLASS, "Первый класс"),
    ]
    user = m.ForeignKey(settings.AUTH_USER_MODEL, on_delete=m.CASCADE, related_name="user_info", default="3")
    plane_num = m.CharField(max_length=5, default='', unique=True)
    plane_model = m.CharField(max_length=20, default='AirBus A319')
    dep_station = m.ForeignKey("City", on_delete=m.CASCADE, related_name='departure_plane')
    arr_station = m.ForeignKey("City", on_delete=m.CASCADE, related_name='arrival_plane')
    dep_time = m.TimeField()
    arr_time = m.TimeField()
    comfort_type = m.CharField(max_length=3, choices=CLASSES, default="")

    class Meta:
        verbose_name_plural = "planes"
        ordering = ["dep_station"]

    def __repr__(self):
        return f"Plane №{self.pk}: from {self.dep_station} to {self.arr_station}"

    def __str__(self):
        return f"{self.dep_station} - {self.arr_station}({self.dep_time}-{self.arr_time}({self.comfort_type}))"

    def distance(self):
        degrees = sqrt(
            (self.arr_station.lat - self.dep_station.lat) ** 2 + (self.arr_station.lon - self.dep_station.lon) ** 2
        )
        return degrees * 64.321

    def price(self):
        real_price = {
            'ЭК': 0.2,
            'КМФ': 0.4,
            'БИЗ':  0.825,
            'ПКЛ': 5.8,
        }
        p = round(self.distance() * real_price[self.comfort_type])
        return f"{p} BYN"

    def get_absolute_url(self):
        return f"{reverse('plane-detail', args=[str(self.pk)])}"
