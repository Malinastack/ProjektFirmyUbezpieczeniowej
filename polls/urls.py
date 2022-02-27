from django.urls import path
from .views import (
    CarListView,
    CarUpdateView,
    ClientDetailView,
    ClientListView,
    ClientUpdateView,
    InsuranceListView,
    InsuranceUpdateView,
    InsuranceCreateView,
    CarCreateView,
)

app_name = "polls"
urlpatterns = [
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/<int:pk>/<car_id>/", ClientDetailView.as_view(), name="client_detail"),
    path("clients/<int:pk>/<car_id>/edit", view=ClientUpdateView.as_view(), name="client_edit"),
    # cars urls
    path("cars/", view=CarListView.as_view(), name="car_list"),
    path("cars/create", view=CarCreateView.as_view(), name="car_create"),
    path("cars/<int:pk>/", view=CarUpdateView.as_view(), name="car_edit"),
    # insurance urls
    path("insurance/", InsuranceListView.as_view(), name="insurance_list"),
    path(
        "insurance/<int:pk>",
        view=InsuranceUpdateView.as_view(),
        name="insurance_edit",
    ),
    path("insurance/create", InsuranceCreateView.as_view(), name="insurance_create"),



]
