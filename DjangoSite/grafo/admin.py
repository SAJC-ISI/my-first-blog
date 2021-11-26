from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import Distance
# Register your models here.
class DistanceAdmin(admin.ModelAdmin):
    list_display = ('R1', 'R2', 'distance')
    list_filter = ('distance',)
    ordering = ('R1',)
    search_fields = ('distance',)

admin.site.register(Distance, DistanceAdmin)