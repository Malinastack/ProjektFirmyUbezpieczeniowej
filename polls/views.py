from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Client


def index(request):
   clients_list = Client.objects.order_by('-first_name')[:5]
   context = {
       'clients_list': clients_list,
   }
   return render(request, 'polls/index.html', context)


def client(request, client_id):
    response = "Dane osoby %s."
    return HttpResponse(response % client_id)
