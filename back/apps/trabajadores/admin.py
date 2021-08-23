from django.contrib import admin, auth
from django.db.models.base import ModelBase
from django_userforeignkey.models.fields import UserForeignKey

from .models import Trabajador, Vacaciones, Categoria
from django.utils.html import format_html
from django.conf import settings

#from apps.bases.models import ClaseModelo
#from django.contrib.auth import authenticate
from django.contrib.auth.models import User
#from apps.empresas.models import Empresa


class VacacionesInline(admin.TabularInline):                
    model = Vacaciones
    #list_display = ('descripcion','fecha_inicio','fecha_final','calculate_dias')    
    readonly_fields = ['dias']
    extra = 0 
    #list_per_page = 2

class TrabajadoresAdmin(admin.ModelAdmin):                    
    model=Trabajador
    inlines = [VacacionesInline]            
    list_display = ( 'nombre','primer_apellido','liquido_mes','fecha_alta','fecha_baja','pk_categoria','dni','pk_empresa', 'foto_img')         

    def get_queryset(self, request):
        qs = super(TrabajadoresAdmin, self).get_queryset(request)                                
        #obtener el nombre del usuario activo
        #user_active = request.user.get_username()
        user_active = request.user.id
        print (user_active, "-" ,request.user.get_username())        
        #if request.user.is_superuser:
        #data = Empresa.objects.get(pk=request.pk_empresa_id)     
        #if user_active == "james":            
        if user_active == 2:  #james          
            return qs.filter(pk_empresa = 2)            
        else:            
            return qs

    '''
    fieldsets = (
        (None, {
            'fields': ('pk_empresa', 'dni')
        }),
        ('Datos Personales', {
            'fields': ('nombre', 'primer_apellido', 'segundo_apellido')
        }),
        ('Varios', {
            'fields': ('pk_categoria', 'foto')
        })
    )
    '''

    #list_editable = ('nombre',)
    search_fields = ('nombre',)
    list_filter = ('nombre','pk_categoria','pk_empresa')

    def foto_img(self, obj):                
        if obj.foto:
            #ruta de la url
            url_media = settings.MEDIA_URL
            #data = GDocumental.objects.get(pk=obj.pk_gestion_documental_id)        
            url_fichero = url_media + str(obj.foto)
            
            #return '<image src="%s" />' % obj.foto
            
            return format_html('<a  class="button" href="{0}" target="_blank">Ver foto</a>&nbsp;',                                                
            #return format_html('<image src="%s">Ver foto</a>&nbsp;',                                    
                    url_fichero
                )                            
            #return '<image src="%s" />' % url_fichero
        else:
           return format_html('<a>No hay foto</a>&nbsp;',)

    foto_img.short_description = 'Ver Foto'
    foto_img.allow_tags = True


class VacacionesAdmin(admin.ModelAdmin):                    
    list_display = ('pk_vacaciones','descripcion','fecha_inicio','fecha_final','dias')

admin.site.register(Trabajador, TrabajadoresAdmin)
admin.site.register(Vacaciones, VacacionesAdmin)
admin.site.register(Categoria)


