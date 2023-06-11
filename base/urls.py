from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='chatbot'),
    path('refresh', views.refresh, name='refresh_func'),
]

