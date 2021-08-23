from django.db import models
from apps.bases.models import ClaseModelo
from apps.gdocumental.models import GDocumental
import datetime


class Sector(ClaseModelo):        

    fecha_alta = models.DateField(blank=True, null=True, verbose_name="Fecha alta")  

    descripcion = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Descripción Sector"
    )    

    tipo_suelo = models.CharField(
        max_length=15, 
        blank=False,
        verbose_name="Tipo Suelo"
    )                  

    sector = models.CharField(
        max_length=15, 
        blank=False,
        verbose_name="Sector"
    )          

    zona = models.CharField(
        max_length=15, 
        blank=False,
        verbose_name="Zona"
    )          

    grado_edificabilidad=models.DecimalField(        
        max_digits=4,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Grado Edificabilidad"
    )    

    ocupacion_maxima=models.DecimalField(        
        max_digits=4,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Ocupación Máxima"
    )    

    coeficiente_reduccion=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Coeficiente Reducción"
    )    

    edificacion=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Edificabilidad"
    )    

    altura_maxima = models.CharField(
        max_length=25, 
        blank=True,
        verbose_name="Altura maxima edificación"
    )                  

    planta_sotano = models.BooleanField(        
        blank=False,
        verbose_name="Planta sotano"
    )                  

    condiciones_uso = models.CharField(
        max_length=25, 
        blank=True,
        verbose_name="Condiciones Uso"
    )                  

    observaciones = models.TextField(
        max_length=500, 
        blank=True,
        verbose_name="Observaciones"
    )            

    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Sector, self).save()

    class Meta:
        verbose_name_plural = "Sector"


class Pgou(ClaseModelo):        

    fecha_alta = models.DateField(blank=True, null=True, verbose_name="Fecha alta")  

    descripcion = models.CharField(
        max_length=50, 
        null=True,
        blank=False,
        verbose_name="PGOU"
    )            

    pk_sector = models.ForeignKey(
        Sector,    
        null=True,    
        blank=False,
        default = 0,
        verbose_name="Sector",
        on_delete=models.CASCADE)
    
    unidad = models.CharField(
        max_length=15, 
        blank=True,
        verbose_name="Unidad"
    )            

    tipo = models.CharField(
        max_length=15, 
        blank=True,
        verbose_name="Tipo"
    )    
    
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Adjuntar Fichero",
        on_delete=models.CASCADE)

    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Pgou, self).save()

    class Meta:
        verbose_name_plural = "PGOU"

