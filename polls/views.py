from django.shortcuts import render
from django import forms
from django.urls import reverse_lazy
from .models import Client
from django.views.generic import DetailView, ListView, UpdateView


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('polls:client_LISTA')





