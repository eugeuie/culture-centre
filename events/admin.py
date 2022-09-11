from django.contrib import admin
from .models import Event, Person, Category, Place


admin.site.register(Event)
admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Place)
