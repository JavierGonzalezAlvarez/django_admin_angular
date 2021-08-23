from django.db import models
from apps.bases.models import ClaseModelo
from apps.empresas.models import Empresa
from apps.gdocumental.models import GDocumental

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

class Proveedor(ClaseModelo):        
    descripcion=models.CharField(
        max_length=100,
        unique=True
        )
    direccion=models.CharField(
        max_length=250,
        null=True, blank=True
        )
    codigo_postal=models.CharField(
        max_length=5,
        null=True, blank=True
        )    
    contacto=models.CharField(        
        max_length=100,
        null=True, blank=True
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True
    )
    
    observacion=models.TextField(
        max_length=600,
        #null=True,
        blank=True,
        verbose_name="Observaciones"
    ) 
        

    def __str__(self):
    #def __unicode__(self):        
        return '{}'.format(self.descripcion)
        #lo que quiero ver en el combobox al filtrar
        #return '{}'.format(str(self.id) + " - " + self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"

class IVA(ClaseModelo):        
    descripcion=models.CharField(
        max_length=100,
        unique=True
        )

    porcentaje_iva=models.FloatField(        
        #max_digits=2,
        #decimal_places=2,
        default=0,
        blank=True,
        verbose_name="IVA"
    ) 

    def __str__(self):
    #def __unicode__(self):        
        #return '{}'.format(self.descripcion)
        #lo que quiero ver en el combobox al filtrar
        return '{}'.format(self.porcentaje_iva)
        #return '{}'.format(str(self.porcentaje_iva) + " - " + self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        #self.porcentaje_iva = self.porcentaje_iva.upper()
        super(IVA, self).save()

    class Meta:
        verbose_name_plural = "IVA"

'''
class Precios(ClaseModelo):            
    precio=models.DecimalField(        
        max_digits=2,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Precio"
    ) 

    def __str__(self):
        return '{}'.format(self.precio)        

    def save(self):
        self.precio = self.precio.upper()
        #self.porcentaje_iva = self.porcentaje_iva.upper()
        super(Precios, self).save()

    class Meta:
        verbose_name_plural = "Precios"
'''

class Productos(ClaseModelo):            
    pk_proveedor = models.ForeignKey(
        Proveedor,     
        #null=False,   
        blank=False,
        verbose_name="Proveedor",
        on_delete=models.CASCADE
    )
    
    fecha_alta = models.DateField(blank=True, null=True, verbose_name="Fecha alta")  

    codigo = models.CharField(
        max_length=20,
        unique=False
    )
    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Descripción Producto"
    )        

    '''   
    pk_precio = models.ForeignKey(
        Precios,        
        blank=False,
        verbose_name="Precio",
        on_delete=models.CASCADE
    )
    '''
    precio=models.DecimalField(        
        max_digits=8,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Precio"
    )  
    

    def __str__ (self):
        return  str(self.pk_proveedor) + " - " + '{}'.format(self.descripcion) 
    
    def save(self):
        self.descripcion = self.descripcion.upper()        
        super(Productos, self).save()

    class Meta:
        verbose_name_plural = "Productos"    

class Clasificacion(ClaseModelo):        
    clasificacion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Clasificacion"
    )    

    def __str__ (self):
        return '{}'.format(self.clasificacion)            
    
    def save(self):
        self.clasificacion = self.clasificacion.upper()
        super(Clasificacion, self).save()

    class Meta:
        verbose_name_plural = "Clasificacion Compra"

class ComprasEnc(ClaseModelo):
    id = models.AutoField(
        primary_key=True,
        verbose_name="Nº Solicitud Compra"        
    )

    pk_empresa = models.ForeignKey(
        Empresa,        
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE
    )

    pk_clasificacion = models.ForeignKey(
        Clasificacion,        
        blank=True,
        verbose_name="Clasificación Compra",
        on_delete=models.CASCADE
    )

    fecha_solicitud = models.DateField(verbose_name="Fecha solicitud", blank=False)    
    fecha_fin_contrato = models.DateField(verbose_name="Fecha fin contrato", null= True, blank=True)    

    pk_proveedor = models.ForeignKey(
        Proveedor,        
        blank=False,
        verbose_name="Proveedor",
        on_delete=models.CASCADE
    )

    observacion=models.TextField(blank=True,null=True, verbose_name="Observaciones")
    
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        verbose_name="Añadir documento",
        on_delete=models.CASCADE        
    )

    #no_factura=models.CharField(max_length=100)
    #fecha_factura=models.DateField()
    importe=models.FloatField(default=0, null=True, verbose_name="Total BI (euros)")
    descuento=models.FloatField(default=0, null=True, verbose_name="Total Descuento (euros)")
    total=models.FloatField(default=0, null=True, verbose_name="Total Compra (euros)")   
        
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        #self.total = self.importe - self.descuento                        

        #compra_id => es el pk de CompraDet
        self.total = ComprasDet.objects.filter(compra_id=self.id).aggregate(tot=Sum('total'))['tot']        
        self.importe = ComprasDet.objects.filter(compra_id=self.id).aggregate(tot=Sum('importe'))['tot']        
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Compras"
        verbose_name="Encabezado Compra"


class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)

    pk_productos = models.ForeignKey(
        Productos,     
        null=True,   
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="Productos"        
    )

    #producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    #cantidad=models.BigIntegerField(default=0)

    unidades=models.BigIntegerField(                      
        default=0,
        #blank=True,
        verbose_name="Unidades"
    )

    #precio = Productos().precio
    precio = models.FloatField(default=0)

    pk_iva = models.ForeignKey(
        IVA,     
        null=True,   
        blank=True,
        on_delete=models.CASCADE,
        verbose_name="% Iva"        
    )

    iva=models.DecimalField(        
        max_digits=6,
        decimal_places=2,
        default=0,
        blank=True,
        verbose_name="IVA"
    ) 

    #precio_prv=models.FloatField(default=0)
    importe=models.FloatField(        
        #max_digits=8,
        #decimal_places=2,
        default=0,
        #blank=True,
        verbose_name="Base Imponible"
    ) 

    #sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0, verbose_name="Descuento(euros)")
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.pk_productos)

    def save(self):
        self.importe = float(float(int(self.unidades)) * float(self.precio)) - float(self.descuento)
        #self.iva = IVA(pk=self.pk_iva) #, porcentaje_iva="12")        
        
        #self.pk_iva es el modelo, pues dentro del modelo escojo el campo        
        #print(self.objeto_iva) => reseultado => 0.08
        #print(type(self.objeto_iva))  => resultado => <class 'apps.solicitud.models.IVA'>

        self.objeto_iva = IVA.objects.get(pk=self.pk_iva.id)                                                       
        self.objeto_iva_porcentaje = self.objeto_iva.porcentaje_iva
        
        self.iva = float((self.importe)) * float((self.objeto_iva_porcentaje))                
        self.total = float(self.importe) + float(self.iva)                
        super(ComprasDet, self).save()

        
        #super(ComprasEnc,self).save()
    
    class Mega:
        verbose_name_plural = "Detalle Solicitud"
        verbose_name="Detalle Solicitud"

