from django.shortcuts import render
from django.views import generic
from .models import Event


class IndexView(generic.ListView):
    template_name = "events/index.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.order_by("time")
