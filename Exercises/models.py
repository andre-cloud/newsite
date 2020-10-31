from django.db import models

# Create your models here.
from django.db import models
from polymorphic.models import PolymorphicModel


# Create your models here.

class Materia(models.Model):
    materia = models.CharField(max_length=250, help_text='Inserire il titolo della materia')
    descrizione = models.TextField(help_text='Scrivere una minima descrizione per spiegare BREVEMENTE la materia')

    def __str__(self):
        return self.materia


class Argomento(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='argomenti')
    argomento = models.CharField(max_length=250, help_text='Inserire il titolo dell\'argomento')
    descrizione = models.TextField(blank=True, help_text='Scrivere una minima descrizione per l\'argomento')

    def __str__(self):
        return self.argomento


class Esercizio(models.Model):

    title = models.CharField(max_length=120, help_text='Inserire un titolo esplicativo')
    text = models.TextField(help_text='Scrivere il testo del problema. Se si è utilizzato il bot che sfrutta la tecnologia OCR controllare la correttezza del teso ricevuto.')
    argomento = models.ForeignKey(Argomento, on_delete=models.CASCADE, related_name='esercizi')
    fig = models.ImageField(upload_to='img/', blank=True, null=True, help_text='Carica un\'eventuale immagine che completi il testo dell\'esercizio')

    grafico = models.ImageField(upload_to='graphs', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente l\'eventuale grafico necessario per la dimostrazione')
    strutture = models.ImageField(upload_to='str/', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente lo schema della reazione')
    meccanismo = models.ImageField(upload_to='mech/', blank=True, help_text='Caricare un file .png/.svg/.jpeg contenente lo schema dell\'eventuale meccanismo di reazione')
    
    risoluzione = models.TextField(help_text='Scrivere la risoluzione del problema in maniera chiara')
    
    commento = models.TextField(help_text='Commentare il processo mentale che ha portato alla scelta di ciò che è stato caricato come "struttura" e nell\'eventuale meccanismo.')
    
    risultato = models.TextField(help_text='Evidenziare il risultato ottenuto dalla risoluzione delle equazioni.')

    referance = models.TextField(help_text='Se è un libro: Cognome N., Titolo del testo, Casa editrice, anno di pubblicazione con edizione, pagina. Se è un sito inserire il link')
    slug = models.SlugField(help_text='NON MODIFICARE a meno di omonimia') #human-friendly URL
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=10, default="Draft", editable=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Esercizio'
        verbose_name_plural = 'Esercizi'




class Teoria(models.Model):
    argomento = models.ForeignKey(Argomento, on_delete=models.CASCADE, related_name='teoria')
    text = models.TextField(help_text='Scrivere il testo del problema. Se si è utilizzato il bot che sfrutta la tecnologia OCR controllare la correttezza del teso ricevuto.')
    slug = models.SlugField(help_text='NON MODIFICARE')
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=10, default="Draft", editable=False)


    def __str__(self):
        return str(self.argomento)

    class Meta:
        verbose_name = 'Teoria'
        verbose_name_plural = 'Teoria'



class ImmaginiTeoria(models.Model):
    teoria = models.ForeignKey(Teoria, on_delete=models.CASCADE, related_name='immagini')
    image = models.ImageField()
    didascalia = models.TextField(help_text='Inserire una breve didascalia per l\'immagine')





# import sys, inspect

# materie = inspect.getmembers(sys.modules[__name__], lambda member: inspect.isclass(member) and member.__module__ == __name__ and member.__name__ != 'Esercizio')

# def get_modello(nome):
#     for materia, modello in materie:
#         if materia == nome:
#             return modello
#     raise Exception("Materia inesistente")