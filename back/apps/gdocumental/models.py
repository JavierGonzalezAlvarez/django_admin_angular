from django.db import models
from django.db.models.fields import DateField, DateTimeField
from apps.bases.models import ClaseModelo
from apps.empresas.models import Empresa

from django.conf import settings

from django.core.exceptions import ValidationError

#inicio el propietario
class OwnerModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,        
        blank=True,
    )
    class Meta:
        abstract=True

#class GDClasificacion(OwnerModel, ClaseModelo):  
class GDClasificacion(ClaseModelo):        
    clasificacion = models.CharField(
        max_length=50, 
        #help_text="Provincia => Provincia",
        unique=True,        
        blank=False,
        verbose_name="Clasificacion"
    )    

    observacion = models.TextField(
        max_length=250,                 
        #unique=True,        
        blank=True,
        verbose_name="Observaciones",
    )  
    
    #fichero_pdf = models.FileField(upload_to='./static/pdf')

    def __str__ (self):
        return '{}'.format(self.clasificacion)            
    
    def save(self):
        self.clasificacion = self.clasificacion.upper()
        super(GDClasificacion, self).save()

    class Meta:
        verbose_name_plural = "Clasificacion Documental"


#class GDocumental(OwnerModel, ClaseModelo):    
class GDocumental(ClaseModelo):    
    id = models.AutoField(
        primary_key=True,
        verbose_name="Número de Registro Documental"        
        #editable=True
    )
    
    pk_empresa = models.ForeignKey(
        Empresa,        
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE)     
    
    fecha_alta = models.DateTimeField(verbose_name="Fecha alta", blank=False, auto_now_add=DateTimeField)    
    
    pk_gdclasificacion = models.ForeignKey(GDClasificacion,         
        null=True,
        blank=False,        
        verbose_name="Clasificacion",
        on_delete=models.CASCADE
    )   

    descripcion = models.CharField(
        max_length=150,                 
        #unique=True,        
        blank=False,
        verbose_name="Descripción",
    )  
    
    observacion = models.TextField(
        max_length=250,                 
        #unique=True,        
        blank=True,
        verbose_name="Observación",
    )  

    '''        
    def valid_extension(value):
        if (not value.name.endswith('.pdf')): #and
            #not value.name.endswith('.jpeg') and 
            #not value.name.endswith('.gif') and
            #not value.name.endswith('.bmp') and 
            #not value.name.endswith('.png')):
    
            raise ValidationError("Archivo permitido: .pdf")
            #raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png, .gif, .bmp")
    '''
    fichero_pdf = models.FileField(
        #upload_to='./staticfiles/pdf',
        upload_to='./pdf',
        blank=False,
        #validators=[valid_extension],        
        verbose_name="Adjuntar documento (.pdf)"                
    )

    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(GDocumental, self).save()

    class Meta:
        verbose_name_plural = "Gestión Documental"
