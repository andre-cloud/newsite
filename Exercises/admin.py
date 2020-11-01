from django.contrib import admin
from .models import *

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='Published')
make_published.short_description = "Pubblica gli esercizi selezionati"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='Draft')
make_draft.short_description = "Non visualizzare gli esercizi selezionati"

class Admin(admin.ModelAdmin):
    
    list_display = ['title', 'date', 'argomento', 'status']
    list_filter = ['date', 'argomento']
    search_fields = ['title', 'text', 'argomento']

    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_draft]

    class Meta():
        model = Esercizio

class AdminTry(admin.ModelAdmin):
    pass

class ImmaginiArgomentoAdmin(admin.TabularInline):
        model = ImmaginiArgomento
        extra = 3

@admin.register(Argomento)
class ArgomentoAdmin(admin.ModelAdmin):
    inlines = [ImmaginiArgomentoAdmin]
    list_display = ['argomento', 'materia']
    list_filter = ['argomento', 'materia']

    class Meta():
        model = Argomento


admin.site.register(Materia, AdminTry)
admin.site.register(Esercizio, Admin)

