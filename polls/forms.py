from django import forms
from .models import Car, Client, Insurance
from django.contrib.auth.mixins import LoginRequiredMixin


class CarForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            "mark",
            "plate_numbers",
            "production_year",
        )


class ClientForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = ("first_name", "last_name", "owned_car")


class InsuranceForm(LoginRequiredMixin, forms.ModelForm):
    class Meta:
        model = Insurance
        fields = (
            "policy_number",
            "policy_type",
            "policy_end_date",
            "insured_car",
        )
