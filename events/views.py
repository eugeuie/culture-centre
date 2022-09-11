from django.shortcuts import render
from django.views import generic
from .models import Event, Category


class IndexView(generic.ListView):
    template_name = "events/index.html"
    context_object_name = "events"

    def get_queryset(self):
        return Event.objects.order_by("time")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class DetailView(generic.DetailView):
    model = Event
    template_name = "events/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["participants"] = self.object.participants.all()
        return context


def category(request, category_id):
    events = Event.objects.filter(category__pk=category_id)
    context = {
        "events": events,
        "categories": Category.objects.all(),
    }
    return render(request, "events/index.html", context)
