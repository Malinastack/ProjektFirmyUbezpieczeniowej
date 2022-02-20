from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from .models import Car, Client, Insurance
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_list"] = Car.objects.all()
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_list"] = Car.objects.filter(owner_id=self.kwargs["pk"])
        return context


class ClientForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("first_name", "last_name")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("polls:client_list")


class CarListView(LoginRequiredMixin, ListView):
    model = Car


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = 'cars'


class CarForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            "mark",
            "plate_numbers",
            "production_year",
            "owner",
            "insurance_policy",
        )


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("polls:car_list")


class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    fields = ["mark", "production_year", "plate_numbers", "owner", "insurance_policy"]
    success_url = reverse_lazy("polls:car_list")


class InsuranceListView(LoginRequiredMixin, ListView):
    model = Insurance
    context_object_name = 'insurance'
    queryset = Insurance.objects.all()


class InsuranceDetailView(LoginRequiredMixin, DetailView):
    model = Insurance


class InsuranceForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Insurance
        fields = (
            "policy_number",
            "policy_type",
            "policy_end_date",
        )


class InsuranceUpdateView(LoginRequiredMixin, UpdateView):
    model = Insurance
    form_class = InsuranceForm
    success_url = reverse_lazy("home")


class InsuranceCreateView(LoginRequiredMixin, CreateView):
    model = Insurance
    fields = ["policy_number", "policy_type", "policy_end_date"]
    success_url = reverse_lazy("polls:insurance_list")
