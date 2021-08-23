from django.contrib import admin
from django.db.models.base import ModelBase

from .models import GDocumental, GDClasificacion

from django import forms

#para url y pdf
from django.conf.urls import url
from django.utils.html import format_html

from django.conf import settings

class GDocumentalAdmin(admin.ModelAdmin):            
    #exclude = ['id']
    #form = EmpresasForm    
    readonly_fields = ('id',)
    #fields = ('fecha_grabacion', 'descripcion')
    list_display = ('descripcion', 'fecha_alta', 'pk_gdclasificacion', 'observacion', 'get_fichero_pdf', 'pk_empresa','id')
    #list_editable = ('descripcion',)
    search_fields = ('descripcion',)   
    list_filter = ('pk_gdclasificacion',)

    def get_fichero_pdf(self, obj):        
        url_media = settings.MEDIA_URL
        url_fichero = url_media + str(obj.fichero_pdf)
        return format_html('<a  class="button" href="{0}" target="_blank">Ver documento</a>&nbsp;',
        #return format_html('<a  href="{0}" target="_blank">{0}</a>&nbsp;',
            url_fichero #obj.fichero_pdf
        )
    get_fichero_pdf.short_description = 'Fichero'
    get_fichero_pdf.allow_tags = True


admin.site.register(GDocumental, GDocumentalAdmin)
admin.site.register(GDClasificacion)


