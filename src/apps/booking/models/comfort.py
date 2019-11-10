from django.db import models as m


class Comfort(m.Model):
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
    comfort_type = m.CharField(max_length=3, choices=CLASSES, default="")

    class Meta:
        verbose_name_plural = "comfort_types"
        ordering = ["pk"]

    def __repr__(self):
        return f"{self.comfort_type}({self.name})"

    def __str__(self):
        return f"{self.comfort_type}"
