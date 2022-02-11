# Create your models here.
from django.db import models



class InsuranceDepartment(models.Model):
    department_name = models.CharField(max_length=50)


class Client(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class DeparmentBoss(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    department = models.ForeignKey(InsuranceDepartment, on_delete=models.CASCADE, null=True, blank=True)


class InsuranceAgent(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    department = models.ForeignKey(InsuranceDepartment, on_delete=models.CASCADE, null=True, blank=True)


class Task(models.Model):
    task_content = models.CharField(max_length=200)
    task_importance = models.IntegerField()
    assigned_agent = models.ForeignKey(InsuranceAgent, on_delete=models.CASCADE, null=True, blank=True)


class Damage(models.Model):
    damage_explanation = models.CharField(max_length=200)
    damage_date = models.DateField()
    damage_cost = models.IntegerField()
    assigned_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)


class Notification(models.Model):
    notification_content = models.CharField(max_length=200)
    assigned_client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    assigned_agent = models.ForeignKey(InsuranceAgent, on_delete=models.CASCADE, null=True, blank=True)
    notification_importance = models.IntegerField()


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


class Payments(models.Model):
    amount = models.IntegerField()
    payment_date = models.DateField()
    payment_due_date = models.DateField()
    payment_purpose = models.CharField(max_length=200)
    payer = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)








