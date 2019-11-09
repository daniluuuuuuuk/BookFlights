from django.urls import path
from apps.booking import views

urlpatterns = [path("", views.BookingView.as_view(), name="booking")]
