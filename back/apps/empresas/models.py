from django.db import models
from apps.bases.models import ClaseModelo
#from apps.gdocumental.models import GDocumental

#from apps.trabajadores.models import Trabajadores

import datetime

from django.conf import settings

#inicio el propietario
class OwnerModel(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,          
        blank=True,
    )
    class Meta:
        abstract=True

class Poblacion(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Description población"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Poblacion, self).save()

    class Meta:
        verbose_name_plural = "Población"

#Hereda de ClaseModelo, y ya tiene todas las propiedades de ClaseModelo
#class Provincia(OwnerModel, ClaseModelo):    
class Provincia(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Description porvincia"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Provincia, self).save()

    class Meta:
        verbose_name_plural = "Provincias"

#class Empresa(OwnerModel, ClaseModelo):    
class Empresa(ClaseModelo):    
    codigoempresa=models.CharField(
        max_length=4,
        #help_text="Codigo de empresa",
        #null=True,
        unique=True,   
        blank=False,
        verbose_name="Código de Empresa"
    )  
    
    descripcion = models.CharField(
        max_length=255,         
        unique=True,
        blank=False,
        verbose_name="Nombre de la empresa"
    )  
    
    nif=models.CharField(
        max_length=12,
        #null=False,
        blank=False,
        verbose_name="NIF"
    )     

    numero_ss=models.CharField(
        max_length=14,
        #null=False,
        blank=False,
        verbose_name="Nº de la Seguridad Social"
    )     

    fecha_creacion = models.DateField(blank=True, null=True, verbose_name="Fecha Creación")
    fecha_liquidacion = models.DateField(blank=True, null=True, verbose_name="Fecha liquidacion")  

    forma_societaria=models.CharField(
        max_length=25,        
        blank=True,
        verbose_name="Forma Societaria"
    )   

    inscripcion=models.CharField(
        max_length=50,        
        blank=True,
        verbose_name="Inscripción"
    )   

    grupo_fiscal_IS=models.CharField(
        max_length=50,        
        blank=True,
        verbose_name="Grupo Fiscal IS"
    )   

    grupo_fiscal_IVA=models.CharField(
        max_length=50,        
        blank=True,
        verbose_name="Grupo Fiscal IVA"
    )   

    cnae=models.CharField(
        max_length=500,
        #null=True,
        blank=True,
        verbose_name="CNAE"
    )            
                   
    direccion_social=models.CharField(
        max_length=200,
        #null=True,
        blank=True,
        verbose_name="Dirección Social"
    )        

    direccion_fiscal=models.CharField(
        max_length=200,
        #null=True,
        blank=True,
        verbose_name="Dirección Fiscal"
    )        

    codigoPostal=models.CharField(
        max_length=5,        
        blank=True,
        verbose_name="Código Postal"
    )        

    pk_poblacion = models.ForeignKey(Poblacion,         
        null=True,
        blank=True,
        verbose_name="Población",
        on_delete=models.CASCADE
    )    

    pk_provincia = models.ForeignKey(Provincia,         
        null=True,
        blank=True,
        verbose_name="Provincia",
        on_delete=models.CASCADE
    )    
           
    observacion=models.TextField(
        max_length=500,
        #null=True,
        blank=True,
        verbose_name="Observaciones"
    )   
    
    '''
    pk_gestion_documental = models.ManyToManyField(
        GDocumental,
        #null=True,
        blank=True,
        verbose_name="Adjuntar Fichero"        
    )
    '''

    '''
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        verbose_name="Adjuntar Fichero",
        on_delete=models.CASCADE)
    '''
    

    #Cuando hagamos referencia a este modelo, Django va a poner un
    # valor hexadecimal por defecto, para transformarlo usamos STR de un campo
    #Todos lo metodos siempre reciebn algo, sino se usa self
    def __str__ (self):
        return '{}'.format(self.descripcion)        
    #Para que la descripcion esté en mayusculas

    #Con este método grabo los cambios. si no está este metodo no se graba en la BBDD
    def save(self):
        self.descripcion = self.descripcion.upper()
        #Para guardar este self.description llamo al metodo save de la clase padre
        #Invocamos al Padre con Super, ¿qué invocamos? => el metodo save
        super(Empresa, self).save()

    #Django añade una "s" a las tablas, para que no sea así, desde Meta lo modificamos
    class Meta:
        #Cuando se refiera en plural
        verbose_name_plural = "Empresas"
        ordering = ['codigoempresa']

