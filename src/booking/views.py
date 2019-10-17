from django.shortcuts import render
from booking.models import City


def booking(request):
    return render(request, "booking/index.html", context={
        "cities": City.objects.all(),
    })

