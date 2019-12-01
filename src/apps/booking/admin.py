from django.contrib import admin

from apps.booking import models

from apps.booking.models import Flight


class FlightAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'user':
            kwargs['queryset'] = get_user_model().objects.filter(username=request.user.email)
        return super(FlightAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        if obj is not None:
            return self.readonly_fields + ('user',)
        return self.readonly_fields

    def add_view(self, request, form_url="{% url 'flight_add' %}", extra_context=None):
        data = request.GET.copy()
        data['user'] = request.user
        request.GET = data
        return super(NotesAdmin, self).add_view(request, form_url="{% url 'flight_add' %}", extra_context=extra_context)


admin.site.register(Flight, FlightAdmin)

admin.site.register(models.City)
admin.site.register(models.Passenger)
admin.site.register(models.Plane)
admin.site.register(models.Comfort)
# admin.site.register(models.Flight)
