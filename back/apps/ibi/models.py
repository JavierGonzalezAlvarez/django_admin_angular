from django.db import models
from apps.bases.models import ClaseModelo
from apps.gdocumental.models import GDocumental
from apps.empresas.models import Empresa
from apps.catastro.models import Catastro

class Concepto(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Concepto tributario"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Concepto, self).save()

    class Meta:
        verbose_name_plural = "Concepto"

class Organismo(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Organismo"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Organismo, self).save()

    class Meta:
        verbose_name_plural = "Organismo"

class Grupo(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Grupo"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Grupo, self).save()

    class Meta:
        verbose_name_plural = "Grupo"


class Subgrupo(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Subgrupo"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Subgrupo, self).save()

    class Meta:
        verbose_name_plural = "Subgrupo"


class Ibi(ClaseModelo):        
    pk_empresa = models.ForeignKey(
        Empresa,
        #null=True,
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE)     
    
    pk_organismo = models.ForeignKey(
        Organismo,
        null=True,
        blank=True,
        verbose_name="Organismo",
        on_delete=models.CASCADE
    )

    pk_concepto = models.ForeignKey(
        Concepto,
        null=True,
        blank=True,        
        verbose_name="Concepto del Tributo",        
        on_delete=models.CASCADE
    )
    
    numero_fijo = models.CharField(
        max_length=25, 
        unique=True,
        blank=False,
        verbose_name="Número fijo"
    )  

    pk_referencia_catastro = models.ForeignKey(
        Catastro,
        null=True,
        blank=True,
        verbose_name="Referencia Catastro",
        on_delete=models.CASCADE
    )
    
    pk_grupo = models.ForeignKey(
        Grupo,
        null=True,
        blank=True,
        verbose_name="Grupo",
        on_delete=models.CASCADE
    )

    pk_subgrupo = models.ForeignKey(
        Subgrupo,
        null=True,
        blank=True,
        verbose_name="Subgrupo",
        on_delete=models.CASCADE
    )

    numero_policia= models.CharField(
        max_length=50, 
        blank=True,
        unique=False,        
        verbose_name="Número policia"
    )      

    bastidor= models.CharField(
        max_length=50, 
        blank=True,
        unique=False,        
        verbose_name="Bastidor"
    )      

    fecha_inicio_devengo = models.DateField(verbose_name="Fecha inicio devengo")  
    #blank=True (for the admin) and null=True (for the database).
    fecha_fin_devengo = models.DateField(blank=True, null=True, verbose_name="Fecha fin devengo")  
    fecha_ultimo_dia = models.DateField(blank=True, null=True, verbose_name="Último día de pago")  

    importe_pago=models.DecimalField(        
        max_digits=8,
        decimal_places=2,        
        default=0,
        blank=True,
        verbose_name="Importe pago anual"
    )  

    descripcion = models.TextField(
        max_length=150,         
        #unique=True,        
        blank=True,
        verbose_name="Observaciones",
    )   

    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        verbose_name="Documento",
        on_delete=models.CASCADE        
        )
    

    #def gett(self):
    #    return self.pk_gestion_documental.fichero_pdf

    def __str__ (self):
        return '{}'.format(self.numero_fijo)            
    
    def save(self):
        self.numero_fijo = self.numero_fijo.upper()
        super(Ibi, self).save()

    class Meta:
        verbose_name_plural = "Suma"
        ordering = ['numero_fijo']

