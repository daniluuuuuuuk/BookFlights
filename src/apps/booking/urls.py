from django.urls import path
from apps.booking import views
from .views import TicketView

urlpatterns = [
    path("", views.BookingView.as_view(), name="booking"),
    path('<int:pk>/', views.TicketView.as_view(), name='plane-detail'),
    path("add/", views.TripAddView.as_view(), name="flight_add"),
    # path("my_flights/", views.FlightView.as_view(), name="user_flights"),
    # path("<int:pk>/", views.TripAddView.as_view(), name="flight"),
]
