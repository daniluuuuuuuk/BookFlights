from django import forms as f
from django.utils.translation import ugettext as _
from apps.booking.models import Book, Plane, City


class SearchForm(f.ModelForm):
    dep_station = f.ModelChoiceField(queryset=City.objects.values_list('name', flat=True).distinct())
    arr_station = f.ModelChoiceField(queryset=City.objects.values_list('name', flat=True).distinct())
    comfort_type = f.ModelChoiceField(queryset=Book.objects.values_list('comfort_type', flat=True).distinct())

    class Meta:
        model = Book
        fields = ("dep_station", "arr_station", "comfort_type")
