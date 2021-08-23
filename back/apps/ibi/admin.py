from django.contrib import admin
#from django.db.models.fields import CharField
#from django.db.models.query import QuerySet

from apps.gdocumental.models import GDocumental

#formato a los campos del formulario
from django.db import models
from django.forms import TextInput, Textarea

from .models import Ibi, Organismo, Concepto, Grupo, Subgrupo

class IbiAdmin(admin.ModelAdmin):                    
    list_display = ( 'numero_fijo','pk_empresa','pk_referencia_catastro','numero_policia','get_importe_pago','fecha_inicio_devengo','fecha_fin_devengo','pk_gestion_documental')    
    #list_display = ('pk_empresa', 'numero_policia', 'descripcion', 'numero_fijo','pk_gestion_documental', 'get_ficheropdf')        
    #exclude = ('pk_gestion_documental',)
    list_filter =('numero_fijo', 'fecha_ultimo_dia','pk_referencia_catastro','pk_concepto',)
    search_fields = ('numero_fijo',)

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }


    #class Meta:
        #model = Ibi        
    def get_importe_pago(self, obj):
        return '%.2f Eur' % obj.importe_pago
    get_importe_pago.short_description = 'Importe'    

'''
    def get_ficheropdf(self, obj):                
        return obj.pk_gestion_documental.fichero_pdf
        #return obj.gdocumental.fichero_pdf
    
    get_ficheropdf.admin_order_field = 'pk_gestion_documental__fichero_pdf'    
    get_ficheropdf.short_description = 'Fichero'    
'''
    #def get_queryset(self, request):  
        #model = GDocumental     
    #    QuerySet = super().get_queryset(request)
    #    QuerySet = QuerySet.get_ficheropdf('fichero_pdf')
        
        #result=obj.pk_gestion_documental_set.all()        
        #result = obj.objects.all(pk_gestion_documental='1')
        #return result.get('fichero_pdf')                

admin.site.register(Ibi, IbiAdmin)
admin.site.register(Organismo)
admin.site.register(Concepto)
admin.site.register(Grupo)
admin.site.register(Subgrupo)
