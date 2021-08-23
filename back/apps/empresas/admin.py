from django.contrib import admin
from django.db.models.base import ModelBase
from .models import Empresa, Provincia, Poblacion

#from apps.gdocumental.models import GDocumental

class EmpresasAdmin(admin.ModelAdmin):                    
    list_display = ('descripcion','codigoempresa','nif','cnae','direccion_fiscal','inscripcion','fecha_creacion','observacion')    
    #exclude = ('pk_gestion_documental',)
    #list_filter =('')
    #search_fields = ('')

admin.site.register(Empresa, EmpresasAdmin)
admin.site.register(Provincia)
admin.site.register(Poblacion)

