from django.db import models
from apps.bases.models import ClaseModelo
from apps.gdocumental.models import GDocumental
from apps.empresas.models import Empresa

class Catastro(ClaseModelo):        
    pk_empresa = models.ForeignKey(
        Empresa,
        #null=True,
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE)     

    fecha_alta = models.DateField(blank=True, null=True, verbose_name="Fecha alta")  

    descripcion_catastral = models.CharField(
        max_length=50, 
        blank=False,
        #unique=True,
        verbose_name="Gestor del Catastro"
    )            
    
    referencia_catastral = models.CharField(
        max_length=20, 
        blank=False,
        verbose_name="Referencia Catastral"
    )            
    
    valor_suelo=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Valor suelo"
    )  

    valor_construccion=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Valor construccion"
    )  

    valor_catastral=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Valor catastral"
    )  

    metros2_suelo=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Metros² suelo"
    )  

    metros2_construido=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Metros² construidos"
    )      
    
    link_catastro = models.CharField(
        max_length=250, 
        blank=True,
        verbose_name="Link foto catastro"
    )                

    link_googlemaps = models.CharField(
        max_length=250, 
        blank=True,
        verbose_name="Coordenadas Google Maps"
    )                
    
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        verbose_name="Fichero",
        default = 0,
        on_delete=models.CASCADE)
    

    def __str__ (self):
        return '{}'.format(self.referencia_catastral)            
    
    def save(self):
        self.referencia_catastral = self.referencia_catastral.upper()
        super(Catastro, self).save()

    class Meta:
        verbose_name_plural = "Catastro"
        ordering = ['referencia_catastral']

