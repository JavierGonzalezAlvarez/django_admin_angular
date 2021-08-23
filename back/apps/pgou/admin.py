from django.contrib import admin
from .models import Pgou, Sector

class SectorAmin(admin.ModelAdmin):                
    ordering = ['fecha_alta']
    list_display = ('descripcion','fecha_alta')
    #list_editable = ('descripcion',)
    search_fields = ('sector',)    
    list_filter = ('descripcion',)

class PgouAdmin(admin.ModelAdmin):                
    ordering = ['fecha_alta']
    list_display = ('descripcion','fecha_alta')
    #list_editable = ('descripcion',)
    search_fields = ('unidad',)    
    list_filter = ('descripcion',)


admin.site.register(Sector, SectorAmin)
admin.site.register(Pgou, PgouAdmin)

