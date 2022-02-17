from django.contrib import admin

from .models import Client, Car, Damage, Insurance

# Register your models here.


@admin.register(Client)
class CreatingClientAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name"]


@admin.register(Car)
class CreatingCarAdmin(admin.ModelAdmin):
    fields = ["mark", "production_year", "plate_numbers"]


@admin.register(Damage)
class CreatingDamageAdmin(admin.ModelAdmin):
    fields = ["damage_explanation", "damage_date", "damage_cost", "assigned_client"]


@admin.register(Insurance)
class CreatingInsuranceAdmin(admin.ModelAdmin):
    fields = ["policy_number", "policy_type", "policy_end_date"]


