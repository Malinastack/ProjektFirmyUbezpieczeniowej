from django.contrib import admin

from .models import Client, Car
# Register your models here.


class CreatingClient(admin.ModelAdmin):
    fields = ['first_name', 'last_name']


admin.site.register(Client, CreatingClient)


class CreatingCar(admin.ModelAdmin):
    fields = ['mark', 'production_year', 'plate_numbers']


admin.site.register(Car, CreatingCar)
