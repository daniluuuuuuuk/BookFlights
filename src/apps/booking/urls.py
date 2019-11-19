from django.urls import path
from apps.booking import views
from .views import TicketView

urlpatterns = [
    path("", views.BookingView.as_view(), name="booking"),
    path('<int:pk>/', views.TicketView.as_view(), name='plane-detail'),
]
