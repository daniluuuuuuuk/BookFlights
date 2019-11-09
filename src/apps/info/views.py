from django.shortcuts import render, get_object_or_404

from django.views.generic import DetailView

from apps.info.models import Ticket


class TicketView(DetailView):
    template_name = "info/index.html"
    model = Ticket

    #def get_object(self, queryset=None):
        #id_ = self.kwargs.get("id")
        #return get_object_or_404(Ticket, id=id_)

    # def ticket_detail(request, slug):
    #     template = 'info/index.html'
    #
    #     ticket = get_object_or_404(Ticket, slug=slug)
    #     context = {
    #         'ticket': ticket,
    #     }
    #     return render(request, template, context)
