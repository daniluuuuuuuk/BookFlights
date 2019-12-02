from collections import defaultdict
from django.views.generic import ListView
from django.views.generic import DetailView
from apps.booking.forms import SearchForm
from apps.booking.models import Plane, Flight
from django import forms
from django.views.generic import CreateView
from utils.aname import a
from django.urls import reverse
import django_filters


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


def get_pk(**kwargs):

    return context


class TicketView(DetailView):
    template_name = "booking/ticket.html"
    model = Plane


class TripAddForm(forms.ModelForm):
    class Meta:
        model = Flight
        # fields = [a(_f) for _f in (Flight.user, Flight.booked_plane)]
        fields = ('booked_plane',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TicketAddView, self).form_valid(form)


class TripAddView(CreateView):
    model = Flight

    form_class = TripAddForm
    template_name_suffix = "_add_form"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TripAddView, self).form_valid(form)

    def get_success_url(self):
        return reverse("flights", args=[str(self.object.pk)])


class FlightView(ListView):
    model = Flight
    template_name = "booking/user_flights.html"

    def get_object_list(self):
        return super().get_object_list().filter(user=self.request.user)
