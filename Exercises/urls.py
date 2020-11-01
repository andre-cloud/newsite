from django.urls import path
from . import views as post_views
from django.views.generic import ListView, DetailView
from .models import *


class ExerciesView(ListView):
    context_object_name = 'object'
    template_name = "list.html"

    def get_queryset(self):
        print(Teoria.objects.filter(argomento__argomento=self.kwargs['argomento'], argomento__materia__materia=self.kwargs['materia'], status='Published').query)
        queryset = {'esercizi': Esercizio.objects.filter(argomento__argomento=self.kwargs['argomento'], argomento__materia__materia=self.kwargs['materia'],status='Published').order_by('-date'), 
                    'teoria': Teoria.objects.filter(argomento__argomento=self.kwargs['argomento'], argomento__materia__materia=self.kwargs['materia'], status='Published')}
        return queryset


urlpatterns = [
    path('', ListView.as_view(
        queryset=Materia.objects.all, template_name='homepage.html'), name='homepagne'), #homepage

    path('<str:materia>/<str:argomento>', ExerciesView.as_view(paginate_by=33), name='list'), #lista degli esercizi

    path('<int:id>/<slug:slug>/', DetailView.as_view(
        queryset=Esercizio.objects, template_name="single.html"), name='single'), # Post singoli

    path('contatti/', post_views.contact, name='contacts'), # Sezione contatti
]
