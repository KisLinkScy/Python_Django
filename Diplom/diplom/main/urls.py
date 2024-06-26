from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('login/', views.loging, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registr/', views.registr_user, name='registr'),
]