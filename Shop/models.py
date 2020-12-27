from django.db import models

# Create your models here.
class Shop(models.Model):
    nome = models.CharField(max_length=600, help_text='Nome del design')
    design = models.ImageField(upload_to='designs/', help_text='Aggiungi l\'immagine che del design')
    
    unisex_tshirt = models.CharField(max_length=2000, help_text='Inserisci il link per la t-shirt unisex', blank=True)
    uomo_tshirt = models.CharField(max_length=2000, help_text='Inserisci il link per la t-shirt uomo', blank=True)
    donna_tshirt = models.CharField(max_length=2000, help_text='Inserisci il link per la t-shirt donna', blank=True)
    
    unisex_felpa = models.CharField(max_length=2000, help_text='Inserisci il link per la felpa unisex', blank=True)
    uomo_felpa = models.CharField(max_length=2000, help_text='Inserisci il link per la felpa uomo', blank=True)
    donna_felpa = models.CharField(max_length=2000, help_text='Inserisci il link per la felpa donna', blank=True)
    

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Design'