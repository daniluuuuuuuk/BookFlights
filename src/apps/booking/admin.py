from django.contrib import admin

from apps.booking import models

admin.site.register(models.City)
admin.site.register(models.Passenger)
admin.site.register(models.Plane)
admin.site.register(models.Comfort)
