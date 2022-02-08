from django.db import models

# Create your models here.
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

class Insurance(models.Model):
    NNW = 'NNW'
    Autocasco = 'Autocasco'
    Assistance = 'Assistance'
    OC = 'OC'
    policy_type_choices = (
        (NNW, 'NNW'),
        (Autocasco, 'Autocasco'),
        (Assistance, 'Assistance'),
        (OC, 'OC'),

    )
    policy_number = models.CharField(max_length=30)
    policy_type = models.CharField(max_length=10, choices=policy_type_choices, default=OC)
    policy_end_date = models.DateField()


class Car(models.Model):
    mark = models.CharField(max_length=20)
    production_year = models.DateField()
    plate_numbers = models.CharField(max_length=20)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    insurance_policy = models.ForeignKey(Insurance, on_delete=models.CASCADE, null=True, blank=True)








