from django.db import models
from apps.bases.models import ClaseModelo
from apps.empresas.models import Empresa
from apps.gdocumental.models import GDocumental
from apps.pgou.models import Pgou

from apps.ibi.models import Ibi
from apps.catastro.models import Catastro
import datetime

from django.conf import settings

'''
class Contabilidad(ClaseModelo):        
    cuenta_contable = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Cuenta contable"
    )            

    def __str__ (self):
        return '{}'.format(self.cuenta_contable)            
    
    def save(self):
        self.cuenta_contable= self.cuenta_contable.upper()
        super(Contabilidad, self).save()

    class Meta:
        verbose_name_plural = "Contabilidad"
'''

class Tasacion(ClaseModelo):        
    descripcion = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Descripción Tasación"
    )  

    fecha_tasacion = models.DateField(verbose_name="Fecha tasación")            

    importe_tasacion=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Importe tasación"
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
        self.descripcion= self.descripcion.upper()
        super(Tasacion, self).save()

    class Meta:
        verbose_name_plural = "Tasaciones"

class RegistroPropiedad(ClaseModelo):        
    numero_finca_registral = models.CharField(
        max_length=50, 
        blank=False,
        null=True,
        unique=True,
        verbose_name="Número finca registral"
    )            
    
    descripcion_registro = models.CharField(
        max_length=50, 
        blank=False,
        verbose_name="Descripcion Registro"
    )    

    observacion_registro=models.TextField(
        max_length=500,
        #null=True,
        blank=True,
        verbose_name="Observaciones"
    )               
    
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Adjuntar Fichero",
        on_delete=models.CASCADE)

    def __str__ (self):
        return '{}'.format(self.numero_finca_registral + " - " + self.descripcion_registro)            
    
    def save(self):
        self.numero_finca_registral= self.numero_finca_registral.upper()
        super(RegistroPropiedad, self).save()

    class Meta:
        verbose_name_plural = "Registro Propiedad"


class Clasificacion(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Clasificacion del inmueble"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Clasificacion, self).save()

    class Meta:
        verbose_name_plural = "Clasificacion"

class TipoFinca(ClaseModelo):    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Clasificacion del inmueble"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(TipoFinca, self).save()

    class Meta:
        verbose_name_plural = "Tipo de Finca"



class Stock(ClaseModelo):    
    pk_empresa = models.ForeignKey(
        Empresa,
        #null=True,
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE)             

    fecha_alta = models.DateField(verbose_name="Fecha alta") #, auto_now_add=True)  
    fecha_baja = models.DateField(blank=True, null=True, verbose_name="Fecha baja")      
    
    cliente_venta=models.CharField(
        max_length=25,                
        blank=True,
        unique=False,
        verbose_name="Cliente Venta")   

    importe_venta=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Importe Venta"
    )

    pk_registro = models.ForeignKey(
        RegistroPropiedad,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Nº de Finca",
        on_delete=models.CASCADE)

    pk_tipoFinca = models.ForeignKey(
        TipoFinca,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Tipo Finca",
        on_delete=models.CASCADE)


    pk_clasificacion = models.ForeignKey(
        Clasificacion,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Clasificacion",
        on_delete=models.CASCADE)

    pk_tasacion = models.ForeignKey(
        Tasacion,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Tasacion",
        on_delete=models.CASCADE)

    pk_pgou = models.ForeignKey(
        Pgou,
        null=True,
        blank=True,
        default = 0,
        verbose_name="PGOU",
        on_delete=models.CASCADE)

    pk_ibi = models.ForeignKey(
        Ibi,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Ibi",
        on_delete=models.CASCADE)    

    parcela=models.CharField(
        max_length=15,                
        blank=True,
        unique=True,
        verbose_name="Parcela"
    )   

    numero_nuevo=models.CharField(
        max_length=15,                
        blank=True,
        verbose_name="Numero parcela interno"
    )   

    metros_cuadrados=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Metros cuadrados"
    )   

    cabida=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Cabida"
    )

    Cuentas_Choices = (
        ('','',),
        ('220','220'),
        ('230', '230'),        
        ('310', '310'),        
    )

    cuenta_terreno = models.CharField(
        max_length=6, 
        choices=Cuentas_Choices, 
        default='220',
        blank=True,
        verbose_name="Cuenta contable terreno"
    )

    '''
    pk_cuenta_terreno = models.ManyToManyField(
        Contabilidad,
        null=True,
        blank=True,
        verbose_name="Cuenta contable terreno"
    )
    '''

    importe_contable_suelo =models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Valor contable terreno "
    )

    '''
    pk_cuenta_construccion = models.ManyToManyField(
        Contabilidad,
        #null=True,
        blank=True,
        verbose_name="Cuenta contable construccion"
    )    
    '''
    cuenta_construccion = models.CharField(
        max_length=6, 
        choices=Cuentas_Choices, 
        default='230',
        blank=True,
        verbose_name="Cuenta contable construccion"
    )

    importe_contable_construccion =models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Valor contable construccion"
    )

    pk_tasacion = models.ForeignKey(
        Tasacion,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Imforme de Tasación",
        on_delete=models.CASCADE)

    observaciones = models.TextField(        
        blank=True,
        max_length=800,                 
        verbose_name="Observaciones"
    )        

    def __str__ (self):
        return '{}'.format(self.parcela)        
    #Para que la descripcion esté en mayusculas

    #Con este método grabo los cambios. si no está este metodo no se graba en la BBDD
    def save(self):
        self.parcela = self.parcela.upper()
        super(Stock, self).save()

    class Meta:
        #Cuando se refiera en plural
        verbose_name_plural = "Stock"

class Segregaciones(ClaseModelo):    
    pk_stock = models.ForeignKey(
        Stock,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Finca Matriz",
        on_delete=models.CASCADE
    )
       
    fecha_segregacion = models.DateField(verbose_name="Fecha segregación")

    parcela_segregada=models.CharField(
        max_length=15,                
        blank=True,
        unique=True,
        verbose_name="Parcela Segregada"
    )

    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Segregaciones"
    )    

    observaciones = models.TextField(        
        blank=True,
        max_length=800,                 
        verbose_name="Observaciones"
    ) 
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Segregaciones, self).save()

    class Meta:
        verbose_name_plural = "Resumen Segregaciones "


class Fotos(ClaseModelo):    
    pk_stock = models.ForeignKey(
        Stock,
        null=True,
        blank=True,
        default = 0,
        verbose_name="Adjuntar Foto",
        on_delete=models.CASCADE)
   

    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Dsescripción Foto"
    )    

    fichero_pdf = models.FileField(
        #upload_to='./staticfiles/pdf',
        upload_to='./fotos',
        blank=False,
        #validators=[valid_extension],        
        verbose_name="Adjuntar foto"                
    )
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Fotos, self).save()

    class Meta:
        verbose_name_plural = "Fotos"