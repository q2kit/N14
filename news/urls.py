from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news'),
    path('add/', views.add, name='add'),
]
