# Create your models here.
from django.db import models


class InsuranceDepartment(models.Model):
    department_name = models.CharField(max_length=50, verbose_name="Department name")

    class Meta:
        verbose_name = "Insurance department"
        verbose_name_plural = "Insurance departments"


class Client(models.Model):
    first_name = models.CharField(max_length=60, verbose_name="First name")
    last_name = models.CharField(max_length=60, verbose_name="Last name")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class DeparmentBoss(models.Model):
    first_name = models.CharField(max_length=60, verbose_name="First name")
    last_name = models.CharField(max_length=60, verbose_name="Last name")
    department = models.ForeignKey(
        InsuranceDepartment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Insurance Department",
    )


class InsuranceAgent(models.Model):
    first_name = models.CharField(max_length=60, verbose_name="First name")
    last_name = models.CharField(max_length=60, verbose_name="Last name")
    department = models.ForeignKey(
        InsuranceDepartment,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Insurance Department",
    )


class Task(models.Model):
    task_content = models.CharField(
        max_length=200,
        verbose_name="The content of the task",
    )
    task_importance = models.IntegerField(
        verbose_name="Priority of task",
    )
    assigned_agent = models.ForeignKey(
        InsuranceAgent,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Assigned agent",
    )


class Damage(models.Model):
    class Meta:
        verbose_name = "Damage"
        verbose_name_plural = "Damage"

    damage_explanation = models.CharField(
        max_length=200,
        verbose_name="Damage explanation",
    )
    damage_date = models.DateField(
        verbose_name="Date the damage was caused",
    )
    damage_cost = models.IntegerField(
        verbose_name="Damage cost",
    )
    assigned_client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Client",
    )


class Notification(models.Model):
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    notification_content = models.CharField(
        max_length=200, verbose_name="Content of notification"
    )
    assigned_client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Client"
    )
    assigned_agent = models.ForeignKey(
        InsuranceAgent,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Assigned agent",
    )
    notification_importance = models.IntegerField(
        verbose_name="Importance of notification"
    )


class Car(models.Model):
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    mark = models.CharField(max_length=20, verbose_name="Car make")
    production_year = models.DateField(verbose_name="Production year")
    plate_numbers = models.CharField(
        max_length=20, verbose_name="License plate numbers"
    )
    owner = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Car owner",
    )


class Insurance(models.Model):
    class Meta:
        verbose_name = "Insurance"
        verbose_name_plural = "Insurance"

    NNW = "NNW"
    Autocasco = "Autocasco"
    Assistance = "Assistance"
    OC = "OC"
    policy_type_choices = (
        (NNW, "NNW"),
        (Autocasco, "Autocasco"),
        (Assistance, "Assistance"),
        (OC, "OC"),
    )
    policy_number = models.CharField(max_length=30, verbose_name="Number of policy")
    policy_type = models.CharField(
        max_length=10,
        choices=policy_type_choices,
        default=OC,
        verbose_name="Type of policy",
    )
    policy_end_date = models.DateField(verbose_name="Policy expiry date")
    insured_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Client")


class Payments(models.Model):
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    amount = models.IntegerField(verbose_name="Amount")
    payment_date = models.DateField(verbose_name="Payment date")
    payment_due_date = models.DateField(verbose_name="Payment due date")
    payment_purpose = models.CharField(max_length=200, verbose_name="Payment purpose")
    payer = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Payer"
    )
