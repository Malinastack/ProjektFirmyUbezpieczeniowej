import logging

from django.urls import reverse_lazy
from .models import Car, Client, Insurance
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarForm, ClientForm, InsuranceForm


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super(ClientListView, self).get_context_data(**kwargs)
        dict= {}
        for client in Client.objects.all():
            dict[client.id] = {
                'first_name': client.first_name,
                'last_name': client.last_name,
                'all_cars': client.cars.all()
            }
        context.update({
            'client_list': dict
        })
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class CarListView(LoginRequiredMixin, ListView):
    model = Car

    def get_queryset(self):
        return Car.objects.order_by('insurance__policy_end_date')


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = "cars"


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy("polls:client_list")
    form_class = ClientForm


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("polls:client_list")


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ["mark", "production_year", "plate_numbers", "insurance"]
    success_url = reverse_lazy("polls:car_list")


class InsuranceListView(LoginRequiredMixin, ListView):
    model = Insurance
    context_object_name = "insurance"
    queryset = Insurance.objects.order_by("policy_end_date")


class InsuranceDetailView(LoginRequiredMixin, DetailView):
    model = Insurance


class InsuranceUpdateView(LoginRequiredMixin, UpdateView):
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy("home")


class InsuranceCreateView(LoginRequiredMixin, CreateView):
    model = Insurance
    fields = ["policy_number", "policy_type", "policy_end_date"]
    success_url = reverse_lazy("polls:insurance_list")

