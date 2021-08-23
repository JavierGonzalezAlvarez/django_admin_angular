from django.contrib import admin
from .models import Catastro
from django.urls import reverse
from django.utils.html import format_html

from apps.gdocumental.models import GDocumental
from django.conf import settings

from .reportes import reporte_all, imprimir_one
#from .urls import reporte_all
from django.urls import path

class CatastroAdmin(admin.ModelAdmin):            
    #exclude = ['id']    
    #readonly_fields = ('id',)
    #fields = ('fecha_grabacion', 'descripcion')
    ordering = ['referencia_catastral']
    list_display = ('referencia_catastral','descripcion_catastral','link_catastro_url','link_googlemaps_url','valor_construccion','valor_suelo','valor_catastral','pk_gestion_documental','link_gd_url','fecha_alta','print')
    #list_display_links = ('link_catastro',)
    list_editable = ('valor_construccion','valor_suelo','valor_catastral',)
    list_filter = ('referencia_catastral', 'descripcion_catastral')    
    search_fields = ('referencia_catastral',)   
    
    '''
    def print(self, obj):
        urls = super().get_urls()
        my_urls = [
            path('catastro/listado/', self.changelist_view),
        ]
        return my_urls + urls
    '''
    def print(self, obj):
        return format_html('<a  class="button" href="{0}" target="_blank">Imprimir</a>&nbsp;',                        
            #template = 'cat/html_catastro_formPdf.html'
            #reporte_all(HttpRequest.path('catastro/listado/'))
            #imprimir_one(obj.id)
            reporte_all('listado')
        )
        '''
        return format_html('<a href={"% url 'cat:catastro_pdf_all' %}">Report</a>',
            #imprimir_compra
            #{%url 'reporte_all' %}
            #reporte_all
            #{% url 'cat:catastro_pdf_all' %}
            #cat:catastro_pdf_all
               #<a class="collapse-item" href="{% url 'sol:compras_list' %}">Compras</a>
            #obj.Catastro
             #  <a class="collapse-item" href="{% url 'reporte_all' %}">Compras</a>
        )        
        ''' 
    print.short_description = 'Imprimir'
    print.allow_tags = True


    def link_googlemaps_url(self, obj):
        if obj.link_googlemaps:
            return format_html('<a  class="button" href="{0}" target="_blank">Google Maps</a>&nbsp;',                        
                obj.link_googlemaps
            )            
        else:
            return format_html('<a>No hay Google Maps</a>&nbsp;',                         
            )            
    link_googlemaps_url.short_description = 'Goolge Maps'
    link_googlemaps_url.allow_tags = True

    def link_catastro_url(self, obj):
        if obj.link_catastro:            
            return format_html('<a  class="button" href="{0}" target="_blank">Ver plano catastral</a>&nbsp;',                        
            #target="popup" 
            #return format_html('<a  href="{0}" target="_blank">{0}</a>&nbsp;',
                obj.link_catastro
            )
            #onclick="window.open('http://kanishkkunal.com','popup','width=600,height=600,scrollbars=no,resizable=no'); return false;">
        else:
            return format_html('<a>No hay plano</a>&nbsp;',)
            
    link_catastro_url.short_description = 'Plano Catastro'
    link_catastro_url.allow_tags = True

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

admin.site.register(Catastro, CatastroAdmin)