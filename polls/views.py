from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from .models import Car, Client
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


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
