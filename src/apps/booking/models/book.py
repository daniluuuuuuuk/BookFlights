from math import sqrt
from django.db import models as m
from django.urls import reverse
from typing import Text
from django.utils.translation import ugettext as _
from apps.booking.models import City, Plane


class Book(m.Model):
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

    # dep_station = m.ForeignKey(Plane, on_delete=m.CASCADE, related_name='dep_st')
    # arr_station = m.ForeignKey(Plane, on_delete=m.CASCADE, related_name='arr_st')
    comfort_type = m.CharField(_('title'), max_length=3, choices=CLASSES, default="")

    class Meta:
        verbose_name_plural = "booking"
        ordering = ["pk"]

    def __repr__(self):
        return f"{self.__class__.__name__} №{self.pk}"

    def __str__(self):
        return f"{self.comfort_type }"

    def get_absolute_url(self):
        return f"{reverse('ticket-detail', args=[str(self.pk)])}"

    def price(self):
        real_price = {
            'ЭК': 0.2,
            'КМФ': 0.4,
            'БИЗ':  0.825,
            'ПКЛ': 2,
        }
        p = round(Plane.distance() * real_price[self.comfort_type])
        return p
