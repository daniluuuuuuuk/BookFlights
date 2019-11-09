from django.views.generic import ListView
from apps.booking.forms import SearchForm
from apps.booking.models import Book


# def booking(request):
#     return render(request, "booking/index.html", context={
#         "cities": City.objects.all(),
#         "passengers": Passenger.objects.all(),
#         "planes": Plane.objects.all(),
#         "types": Plane.CLASSES,
#     })

class BookingView(ListView):
    http_method_names = ("get", "post")
    template_name = "booking/index.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = SearchForm()
        if self.request.GET:
            context["form"] = SearchForm(self.request.GET)

        return context

    def get_queryset(self):
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
                if f.cleaned_data["name"]:
                    qs = qs.filter(comfort_type=f.cleaned_data["name"])

        return qs
