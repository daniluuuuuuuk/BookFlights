from django.db import models as m


class City(m.Model):
    name = m.CharField(max_length=20, unique=True)
    lat = m.FloatField()
    lon = m.FloatField()

    class Meta:
        verbose_name_plural = "cities"
        ordering = ["name"]

    def __repr__(self):
        return f"City #{self.pk}: '{self.name}'"

    def __str__(self):
        return f"{self.name}"
