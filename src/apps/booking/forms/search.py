from django import forms as f
from django.utils.translation import ugettext as _
from apps.booking.models import Plane, City, Comfort


class SearchForm(f.ModelForm):
    dep_station = f.ModelChoiceField(queryset=City.objects.all())
    arr_station = f.ModelChoiceField(queryset=City.objects.all())
    comfort_type = f.ModelChoiceField(queryset=Comfort.objects.all(), required=False)

    class Meta:
        model = Plane
        fields = ("dep_station", "arr_station", "comfort_type")
