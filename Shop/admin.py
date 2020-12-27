from django.contrib import admin
from .models import *

# Register your models here.

def make_visible(modeladmin, request, queryset):
    queryset.update(status='Visible')
make_visible.short_description = "Visualizza i design selezionati"
def make_hidden(modeladmin, request, queryset):
    queryset.update(status='Not visible')
make_hidden.short_description = "Nascondi i design selezionati"

@admin.register(Shop)
class Admin(admin.ModelAdmin):
    list_display = ['nome', 'design']
    list_filter = ['nome']
    search_fields = ['nome']

    actions = [make_visible, make_hidden]

    class Meta():
        model = Shop