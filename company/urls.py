from django.urls import path
from . import views

urlpatterns = [
    path('company/add/', views.add_company, name='add_company'),
    path('', views.main, name='main'),
    path('company/', views.company, name = 'company'),
    path('company/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]