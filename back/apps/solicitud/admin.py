from django.contrib import admin
from .models import ComprasDet, ComprasEnc, Proveedor, Productos, IVA, Clasificacion
#from django.conf.urls import url

from django.utils.html import format_html
from apps.gdocumental.models import GDocumental
from django.conf import settings
from django.db.models import Sum

#class SolicitudAdmin(admin.ModelAdmin):                
class ComprasDetInline(admin.TabularInline):                
    model = ComprasDet
    exclude = ('costo',)    
    readonly_fields = ['importe','iva','total']
    #quitar lineas extra
    extra = 0 
    #show_change_link = False
    #list_display = ('pk_productos')
    #list_editable = ('observacion',)
    #search_fields = ('observacion',)    

class ComprasEncAdmin(admin.ModelAdmin):            
    model = ComprasEnc
    inlines = [ComprasDetInline]
    readonly_fields = ['importe','descuento','total']
    list_display = ('id','fecha_solicitud','fecha_fin_contrato','pk_empresa','pk_clasificacion','pk_proveedor','get_importe','get_total','observacion','link_gd_url',)
    list_filter = ('pk_empresa','pk_proveedor','pk_clasificacion',) 
    #list_editable = ('observacion',)

    def get_total(self, obj):                                                               
        #No funciona si no hay detalle
        #return "{:,.2f} Euros".format(obj.total)    
        return obj.total
    get_total.short_description = 'Total'
    get_total.allow_tags = True          
    
    def get_importe(self, obj):                                                               
        #return "{:,.2f} Euros".format(obj.importe)
        return obj.importe
    get_importe.short_description = 'Base Imponible'
    get_importe.allow_tags = True          
    

    def link_gd_url(self, obj):                
        if obj.pk_gestion_documental:
            #ruta de la url
            url_media = settings.MEDIA_URL
            data = GDocumental.objects.get(pk=obj.pk_gestion_documental_id)        
            url_fichero = url_media + str(data.fichero_pdf)
            return format_html('<a  class="button" href="{0}" target="_blank">Ver documento</a>&nbsp;',                        
                    url_fichero #data.fichero_pdf
                )
        else:
           return format_html('<a>No hay documento</a>&nbsp;',)
    link_gd_url.short_description = 'Ver Documento'
    link_gd_url.allow_tags = True    

#-----------------------------------------------------------

class ProductosInline(admin.TabularInline):                
    model = Productos
    extra = 0 
    #list_display = ('pk_productos')

class ProveedoresAdmin(admin.ModelAdmin):            
    model = Proveedor
    list_display = ('descripcion','direccion','contacto','telefono','email','observacion',)
    inlines = [ProductosInline]

#-----------------------------------------------------------

class ProductosAdmin(admin.ModelAdmin):            
    model = Productos
    list_display = ('descripcion','codigo','precio','pk_proveedor')    
    search_fields = ('descripcion','pk_proveedor',)    
    list_filter = ('descripcion','pk_proveedor',) 

#-----------------------------------------------------------
#class ClasificacionAdmin(admin.ModelAdmin): 
   #list_display = ('clasificacion')    

admin.site.register(ComprasEnc, ComprasEncAdmin)
admin.site.register(Proveedor, ProveedoresAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(IVA)
admin.site.register(Clasificacion)