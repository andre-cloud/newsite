from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *

urlpatterns = [
    path('', ListView.as_view(
        queryset=Shop.objects.all(), template_name='shop.html'), name='shop')
]