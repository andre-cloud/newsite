from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *

class HomePageQuerySet(ListView):
    def get_queryset(self):
        return Materia.objects.all()

class ExerciesView(ListView):
    def get_queryset(self):
        return Esercizio.objects.argomento_set.filter(materia=self.kwargs['materia'], argomento=self.kwargs['argomento']).esercizio_set.all().order_by('-date')

urlpatterns = [
    path('', HomePageQuerySet.as_view(template_name='homepage.html'), name='homepagne'), #homepage

    path('<str:materia>/<str:argomento>', ExerciesView.as_view(
        template_name="list.html", paginate_by = 33), name='list'), #lista degli esercizi

    path('<int:id>/<slug:slug>/', DetailView.as_view(
        queryset=Esercizio.objects, template_name="single.html"), name='single'), # Post singoli

    path('contatti/', post_views.contact, name='contacts'), # Sezione contatti
]
