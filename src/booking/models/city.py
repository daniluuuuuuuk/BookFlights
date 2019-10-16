from django.db import models as m


class City(m.Model):
    name = m.TextField(unique=True)
    lat = m.FloatField(unique=True)
    lon = m.FloatField(unique=True)
