from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("category/<int:category_id>/", views.category, name="category"),
]
