from django.shortcuts import render
from django import forms
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from .models import Car, Client, Insurance
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["car_list"] = Car.objects.order_by("insurance_policy__policy_end_date")
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtrowanie po id klienta i numerach rejestracyjnych
        # żeby nie wyświetlało listy samochodów tylko jeden
        context["car_list"] = Car.objects.filter(owner_id=self.kwargs["pk"])
        context["car_list"] = Car.objects.filter(id=self.kwargs["car_id"])
        return context


class CarListView(LoginRequiredMixin, ListView):
    model = Car
    ordering = ["-mark"]


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    context_object_name = "cars"


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


class ClientForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("first_name", "last_name")


ClientFormSet = inlineformset_factory(
    Client, Car, fields=("mark", "production_year", "insurance_policy"),
    fk_name="owner", extra=0

)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    success_url = reverse_lazy("polls:client_list")
    form_class = ClientFormSet


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
    context_object_name = "insurance"
    queryset = Insurance.objects.order_by("policy_end_date")


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
