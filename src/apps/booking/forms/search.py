from django import forms as f
from apps.booking.models import Plane, City, Comfort


class SearchForm(f.ModelForm):
    dep_station = f.ModelChoiceField(queryset=City.objects.all(), label="Откуда")
    arr_station = f.ModelChoiceField(queryset=City.objects.all(), label="Куда")
    comfort_type = f.ModelChoiceField(queryset=Comfort.objects.all(), required=False, label="Класс")

    class Meta:
        model = Plane
        fields = ("dep_station", "arr_station", "comfort_type")
