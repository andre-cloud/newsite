from django.contrib import admin
from .models import *

# Register your models here.

def make_visible(modeladmin, request, queryset):
    queryset.update(status='Today')
make_visible.short_description = "Oggi è il giorno di questo scienziato, pubblicalo"
def make_hidden(modeladmin, request, queryset):
    queryset.update(status='Not today')
make_hidden.short_description = "Cazzo fai? Nascondi questo scienziato"

# def make_draft(modeladmin, request, queryset):
#     queryset.update(status='Not today')
# make_draft.short_description = "Non visualizzare gli esercizi selezionati"

@admin.register(Calendario)
class Admin(admin.ModelAdmin):
    list_display = ['nome', 'giorno', 'status']
    list_filter = ['giorno']
    search_fields = ['nome', 'giorno']

    actions = [make_visible, make_hidden]

    class Meta():
        model = Calendario