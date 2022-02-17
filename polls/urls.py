from django.urls import path
from .views import (
    CarListView,
    CarUpdateView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
)
from . import views

app_name = "polls"
urlpatterns = [
    path("", ClientListView.as_view(), name="client_list"),
    path("<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("<int:pk>/edit", view=ClientUpdateView.as_view(), name="client_edit"),
    path("cars/", view=CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>", view=CarUpdateView.as_view(), name="car_edit"),
]
