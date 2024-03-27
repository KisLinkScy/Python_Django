from django.urls import path
from .import views

urlpatterns = [
    path('', views.voda, name='voda'),
]