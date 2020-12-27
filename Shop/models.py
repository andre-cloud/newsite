from django.db import models

# Create your models here.
class Shop(models.Model):
    nome = models.CharField(max_length=600, help_text='Nome del design')
    design = models.ImageField(upload_to='designs/', help_text='Aggiungi l\'immagine che del design')
    link_tshirt = models.CharField(max_length=600, blank=True, help_text='Quando è pronto il design inserire il link, inserire il link alla maglietta')
    link_felpa = models.CharField(max_length=600, blank=True, help_text='Quando è pronto il design inserire il link, inserire il link alla felpa')
    link_cover = models.CharField(max_length=600, blank=True, help_text='Quando è pronto il design inserire il link, inserire il link alla cover')
    status = models.CharField(max_length=10, default="Non visibile", editable=False)

    class Meta:
        verbose_name = 'Design'
        verbose_name_plural = 'Design'