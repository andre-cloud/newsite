from django.db import models

# Create your models here.
class Calendario(models.Model):

    scienziato = models.ImageField(upload_to='cal/', help_text='Foto a colori dello scienziato')
    img_default = models.ImageField(upload_to='cal/', help_text='Non hai ancora sbloccato questo scienziato')
    giorno = models.CharField(max_length=2, help_text='DD, indicare il numero del giorno')
    nome = models.CharField(max_length=600, help_text='Inserire il nome dello scienziato')
    link = models.CharField(max_length=600, blank=True, help_text='Quando è su instagram,  inserire il link al post')
    status = models.CharField(max_length=10, default="Non today", editable=False)

    def __str__(self):
        return self.nome

    class Meta():
        verbose_name = 'Virus'
        verbose_name_plural = 'Virus'

