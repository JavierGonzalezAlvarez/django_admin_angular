from django.db import models
from apps.bases.models import ClaseModelo
from apps.empresas.models import Empresa

class Proveedor(ClaseModelo):        
    descripcion=models.CharField(
        max_length=100,
        unique=True
        )
    direccion=models.CharField(
        max_length=250,
        null=True, blank=True
        )
    contacto=models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Proveedor, self).save()

    class Meta:
        verbose_name_plural = "Proveedores"

class Productos(ClaseModelo):            
    codigo = models.CharField(
        max_length=20,
        unique=True
    )
    
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Descripción Producto"
    )        

    precio=models.FloatField(        
        #max_digits=8,
        #decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Precio"
    )     

    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()        
        super(Productos, self).save()

    class Meta:
        verbose_name_plural = "Productos"    


class ComprasEnc(ClaseModelo):
    id = models.AutoField(
        primary_key=True,
        verbose_name="Número Solicitud de Compra"        
    )

    pk_empresa = models.ForeignKey(
        Empresa,        
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE
    )
    fecha_solicitud = models.DateField(verbose_name="Fecha solicitud", blank=False)       
    #fecha_compra=models.DateField(null=True,blank=True)
    observacion=models.TextField(blank=True,null=True)
    #no_factura=models.CharField(max_length=100)
    #fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    pk_proveedor = models.ForeignKey(
        Proveedor,        
        blank=False,
        verbose_name="Proveedor",
        on_delete=models.CASCADE
    )
        
    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"



class ComprasDet(ClaseModelo):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)


    pk_productos = models.ManyToManyField(
        Productos,        
        blank=True,
        verbose_name="Productos"        
    )

    #producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    #cantidad=models.BigIntegerField(default=0)

    unidades=models.BigIntegerField(                      
        default=0,
        blank=True,
        verbose_name="Unidades"
    )
    pk_precio = Productos().precio
    #precio_prv=models.FloatField(default=0)
    importe=models.FloatField(        
        #max_digits=8,
        #decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Importe"
    ) 

    #sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):
        self.importe = float(float(int(self.unidades)) * float(self.pk_precio))
        self.total = self.importe - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalle Solicitud"
        verbose_name="Detalle Solicitud"

