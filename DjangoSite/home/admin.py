from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import Paciente, Tessiu

# Register your models here.

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Paciente, PacienteAdmin)


class TessiueAdmin(admin.ModelAdmin):
    list_display = ('color', 'temperatura', 'inflammation', 'name')
    list_filter = ('color','name',)
    #readonly_fields = ('color',)
    ordering = ('color',)
    search_fields = ('color',)

admin.site.register(Tessiu, TessiueAdmin)