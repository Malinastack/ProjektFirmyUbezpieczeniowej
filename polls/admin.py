from django.contrib import admin

from .models import Person
# Register your models here.


class Test(admin.ModelAdmin):
    fields = ['first_name', 'last_name']


admin.site.register(Person, Test)