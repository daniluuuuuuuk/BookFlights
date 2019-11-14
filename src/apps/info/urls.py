from django.urls import path
from apps.info import views
from .views import TicketView

urlpatterns = [
    path('booking/<int:pk>/', views.TicketView.as_view(), name='ticket-detail'),
    # url(r'^ticket-detail/(?P<slug>[-\w])/$', ticket_detail, name="ticket_detail")
]
