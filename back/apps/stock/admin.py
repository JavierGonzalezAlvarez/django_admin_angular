from django.contrib import admin
from django.db.models.base import ModelBase

from .models import Segregaciones, Stock, RegistroPropiedad, Tasacion, Clasificacion, Fotos, TipoFinca
from django.utils.html import format_html

#from nested_admin import NestedModelAdmin, NestedTabularInline

class FotosInline(admin.TabularInline):  
#class FotosInline(NestedTabularInline):              
    model = Fotos
    extra = 0 

class SegregacionesInline(admin.TabularInline):                
#class SegregacionesInline(NestedTabularInline):
    model = Segregaciones
    extra = 0 
    

class StockAdmin(admin.ModelAdmin): 
#class StockAdmin(NestedModelAdmin):               
    model=Stock
    inlines = [FotosInline, SegregacionesInline]
    #inlines = [SegregacionesInline]

    #exclude = ['id']    
    #readonly_fields = ('id',)
    #fields = ('fecha_grabacion', 'descripcion')
    ordering = ['fecha_alta']
    list_display = ('pk_empresa','pk_clasificacion','fecha_alta','fecha_baja','parcela','pk_pgou','pk_ibi', 'numero_nuevo','print_reporte')
    #list_display = ('pk_empresa','fecha_alta','parcela','pk_pgou','pk_ibi', 'numero_nuevo')
    #list_editable = ('descripcion',)
    search_fields = ('parcela',)    
    list_filter = ('pk_empresa', 'numero_nuevo','pk_clasificacion')    
    
    def print_reporte(self, obj):
        return format_html('<a  class="button" href="{0}" target="_blank">Imprimir</a>&nbsp;',
        #return format_html('<a  href="{0}" target="_blank">{0}</a>&nbsp;',
            obj.parcela
        )
    print_reporte.short_description = 'Imprimir'
    print_reporte.allow_tags = True


admin.site.register(Tasacion)
admin.site.register(Clasificacion)
admin.site.register(RegistroPropiedad)
admin.site.register(Stock, StockAdmin)
admin.site.register(TipoFinca)
admin.site.register(Segregaciones)

