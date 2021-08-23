from django.db import models
from apps.bases.models import ClaseModelo
from apps.empresas.models import Empresa, Provincia, Poblacion
from apps.gdocumental.models import GDocumental

#calcular los días
from datetime import date


class Categoria(ClaseModelo):        
    descripcion = models.CharField(
        max_length=50,         
        unique=True,        
        blank=False,
        verbose_name="Descripción"
    )    
    
    def __str__ (self):
        return '{}'.format(self.descripcion)            
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categoria"

class Trabajador(ClaseModelo):  
    pk_empresa = models.ForeignKey(
        Empresa,
        #null=True,
        blank=False,
        verbose_name="Empresa",
        on_delete=models.CASCADE        
    )

    pk_categoria = models.ForeignKey(
        Categoria,
        null=True,
        blank=True,
        verbose_name="Categoria laboral",
        on_delete=models.CASCADE        
    )

    grupo_cotizacion = models.CharField(
        max_length=2,     
        blank=False,
        verbose_name="Grupo Cotizacion"
    )    


    dni = models.CharField(
        max_length=10,     
        blank=False,
        verbose_name="DNI"
    )    

    seguidad_social = models.CharField(
        max_length=14,     
        blank=True,
        verbose_name="Seguridad Social"
    )  

    fecha_alta = models.DateField(verbose_name="Fecha alta")  
    fecha_baja = models.DateField(blank=True, null=True, verbose_name="Fecha baja")      
    
    nombre = models.CharField(
        max_length=20, 
        help_text="Nombre del trabajador",        
        blank=False,
        verbose_name="Nombre"
    )        
    primer_apellido = models.CharField(
        max_length=20, 
        help_text="Primer apellido del trabajador",        
        blank=True,
        verbose_name="Primer apellido"
    )    
    segundo_apellido = models.CharField(
        max_length=20, 
        help_text="Segundo apellido del trabajador",        
        blank=True,
        verbose_name="Segundo apellido"
    )    

    estudios = models.CharField(
        max_length=50,         
        help_text="Estudios Máximos Alcanzados",        
        blank=True,
        verbose_name="Estudios realizados"
    )  

    cuenta_corriente = models.CharField(               
        max_length=24,         
        blank=True,        
        verbose_name="Cuenta Corriente"
    )      

    foto  = models.ImageField(
        #upload_to='./staticfiles/fotos',
        upload_to='./fotos',
        blank=True,
        verbose_name="Adjuntar Foto"
    )    
    direccion_empleado = models.CharField(
        max_length=100, 
        help_text="Dirección de residencia completa del trabajador",        
        blank=True,
        verbose_name="Dirección"
    )    
    codigo_postal = models.CharField(               
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
    telefono = models.CharField(
        max_length=12,         
        blank=True,
        verbose_name="Telefono"
    )    
    movil = models.CharField(
        max_length=12,              
        blank=True,
        verbose_name="Móvil"
    )    
    email = models.EmailField(
        max_length=25, 
        blank=True,
        unique=False,
        verbose_name="Email"
    )    

    salario_bruto = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0, 
        verbose_name="Salario Bruto Anual"
    )

    liquido_mes = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0, 
        verbose_name="Salario Liquido Mes"
    )

    observacion=models.TextField(
        max_length=600,
        #null=True,
        blank=True,
        verbose_name="Observaciones"
    )   
    
    '''
    pk_vacaciones = models.ManyToManyField(Vacaciones,
        blank=True,        
        verbose_name="Vacaciones"
    )
    '''

    '''
    pk_vacaciones = models.ForeignKey(
        Vacaciones, 
        null=True,
        blank=True,        
        verbose_name="Vacaciones",
        on_delete=models.CASCADE
    )    
    '''

    #observacion=models.TextField(
    #    max_length=500,
    #    null=True, 
    #    blank=True
    #)  
    def __str__ (self):
        return '{}'.format(self.nombre)            
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Trabajador, self).save()

    class Meta:
        verbose_name_plural = "Trabajadores"


class Vacaciones(ClaseModelo):    
    pk_vacaciones = models.ForeignKey(
        Trabajador, 
        null=True,
        blank=True,        
        verbose_name="Vacaciones",
        on_delete=models.CASCADE
    )

    descripcion = models.CharField(
        max_length=50, 
        #help_text="Provincia => Provincia",
        #unique=True,        
        blank=False,
        verbose_name="Descripción"
    )    

    fecha_inicio = models.DateField(blank=False)
    fecha_final = models.DateField(blank=True)       
    
    @property
    def calculate_dias(self):
        return (self.fecha_final-self.fecha_inicio).days + 1    
    
    dias=models.IntegerField(        
        #max_digits=2,
        #decimal_places=2,
        default=0,
        blank=True,
        verbose_name="Días"
    )      
    
    pk_gestion_documental = models.ForeignKey(
        GDocumental,
        null=True,
        blank=True,
        verbose_name="Documento",
        default = 0,
        on_delete=models.CASCADE
    )
   
    def __str__ (self):
        #return '{}'.format(str(self.fecha_inicio) + " - " + self.descripcion + " - Días: " + str(self.calculate_dias))
        return '{}'.format(str(self.fecha_inicio) + " - " + self.descripcion)
    
    #@property
    def save(self):
        self.descripcion = self.descripcion.upper()
        self.dias = self.calculate_dias   #self.fecha_final-self.fecha_inicio.days + 1
        super(Vacaciones, self).save()

    class Meta:
        verbose_name_plural = "Vacaciones"

