from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *


class ExerciesView(ListView):
    context_object_name = 'esercizi'
    template_name = "list.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teoria'] = Argomento.objects.get(argomento=self.kwargs['argomento'], materia__materia=self.kwargs['materia'])
        return context

    def get_queryset(self):
        return Esercizio.objects.filter(argomento__argomento=self.kwargs['argomento'], argomento__materia__materia=self.kwargs['materia'],status='Published').order_by('-date') #lista degli esercizi con tutti i modelli caricati


urlpatterns = [
    path('', ListView.as_view(
        queryset=Materia.objects.all, template_name='homepage.html'), name='homepagne'), #homepage

    path('<str:materia>/<str:argomento>', ExerciesView.as_view(paginate_by=12), name='list'), #lista degli esercizi

    path('<int:id>/<slug:slug>/', DetailView.as_view(
        queryset=Esercizio.objects, template_name="single.html"), name='single'), # Post singoli

    path('contatti/', post_views.contact, name='contacts'), # Sezione contatti
]
