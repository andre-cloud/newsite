from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *

urlpatterns = [
    path('', ListView.as_view(
        queryset=Calendario.objects.all().order_by('giorno'), template_name='calendario.html'), name='calendario')
]