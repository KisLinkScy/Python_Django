from django.urls import path
from .import views

urlpatterns = [
    path('', views.svet, name='svet'),
]