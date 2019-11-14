from collections import defaultdict
from django.views.generic import ListView
from apps.booking.forms import SearchForm
from apps.booking.models import Plane
from django import forms


class BookingView(ListView):
    http_method_names = ("get", "post")
    template_name = "booking/index.html"
    model = Plane

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm()
        if self.request.GET:
            context["form"] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
        if not self.request.GET:
            return[]

        qs = super().get_queryset()

        if self.request.GET:
            f = SearchForm(self.request.GET)
            if f.is_valid():
                if f.cleaned_data["dep_station"]:
                    qs = qs.filter(dep_station=f.cleaned_data["dep_station"])
                if f.cleaned_data["arr_station"]:
                    qs = qs.filter(arr_station=f.cleaned_data["arr_station"])
                if f.cleaned_data["comfort_type"]:
                    qs = qs.filter(comfort_type=f.cleaned_data["comfort_type"])

        return qs

# form = SearchForm(self.request.GET)
        # if not form.is_valid():
        #     return []
        #
        # booking = super().get_queryset()
        #
        # if form.cleaned_data["dep_station"]:
        #     booking = booking.filter(dep_station=form.cleaned_data["dep_station"])
        #
        # if form.cleaned_data["arr_station"]:
        #     booking = booking.filter(arr_station=form.cleaned_data["arr_station"])
        #
        # if form.cleaned_data["comfort_type"]:
        #     booking = booking.filter(comfort_type=form.cleaned_data["comfort_type"])
        #
        # grouped = defaultdict(list)
        # for b in booking:
        #     grouped[b.dep_station].append(b)
        #
        # return grouped.items()
