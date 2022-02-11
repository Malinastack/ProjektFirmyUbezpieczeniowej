from django.urls import path
from .views import ClientDetailView, ClientListView, ClientUpdateView
from . import views
app_name = 'polls'
urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client'),
    path('edit/<int:pk>', view=views.ClientUpdateView.as_view(), name='client_edit'),
]