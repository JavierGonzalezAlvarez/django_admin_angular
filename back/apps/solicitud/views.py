from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy
#inicializar la fecha
import datetime
from django.http import HttpResponse

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum

from .models import Proveedor, Productos, ComprasEnc, ComprasDet
from .forms import ProveedorForm, ProductoForm, ComprasEncForm

from apps.empresas.models import Empresa

from apps.bases.views import SinPrivilegios
#from apps.inv.models import Producto

class ProveedorView(generic.ListView):
    model = Proveedor
    template_name = "sol/html_proveedor_list.html"
    context_object_name = "obj"
    permission_required="apps.solicitud.view_proveedor"

class ProveedorNew(SuccessMessageMixin,generic.CreateView):
    model=Proveedor
    template_name="sol/html_proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("sol:proveedor_list")

    success_message="Proveedor Creado"
    permission_required="apps.solicitud.add_proveedor"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

class ProveedorEdit(SuccessMessageMixin,generic.UpdateView):
    model=Proveedor
    template_name="sol/html_proveedor_form.html"
    context_object_name = 'obj'
    form_class=ProveedorForm
    success_url= reverse_lazy("sol:proveedor_list")
    success_message="Proveedor Editado"
    permission_required="apps.solicitud.change_proveedor"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        #print(self.request.user.id)
        return super().form_valid(form)

class ProductoView(generic.ListView):
    model = Productos
    template_name = "sol/html_producto_list.html"
    context_object_name = "obj"
    permission_required="apps.solicitud.view_producto"

class ProductoNew(SuccessMessageMixin,generic.CreateView):
    model=Productos
    template_name="sol/html_producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("sol:producto_list")

    success_message="Producto Creado"
    permission_required="apps.solicitud.add_producto"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

class ProductoEdit(SuccessMessageMixin,generic.UpdateView):
    model=Productos
    template_name="sol/html_producto_form.html"
    context_object_name = 'obj'
    form_class=ProductoForm
    success_url= reverse_lazy("sol:producto_list")
    success_message="Producto Editado"
    permission_required="apps.solicitud.change_producto"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        #print(self.request.user.id)
        return super().form_valid(form)

'''
@login_required(login_url="/login/")
@permission_required("sol.change_proveedor",login_url="/login/")
def proveedorInactivar(request,id):
    template_name='sol/inactivar_prv.html'
    contexto={}
    prv = Proveedor.objects.filter(pk=id).first()

    if not prv:
        return HttpResponse('Proveedor no existe ' + str(id))

    if request.method=='GET':
        contexto={'obj':prv}

    if request.method=='POST':
        prv.estado=False
        prv.save()
        contexto={'obj':'OK'}
        return HttpResponse('Proveedor Inactivado')

    return render(request,template_name,contexto)
'''

class ComprasView(SinPrivilegios, generic.ListView):
    model = ComprasEnc
    template_name = "sol/html_compras_list.html"
    context_object_name = "obj"
    permission_required="apps.sol.view_comprasenc"


#como hay que cambiar muchas cosas hay que hacer una funcion y 
# no podemos usar una vista de clase
@login_required(login_url='/login/')
@permission_required('apps.sol.view_comprasenc', login_url='bases:sin_privilegios')
def compras(request,compra_id=None):
    template_name="sol/html_compras.html"
    #tendremos todos los productos que se van a renderizar
    #prod=Productos.objects.filter(estado=True)
    prod=Productos.objects.filter(estado=True)

    form_compras={}
    contexto={}

    #enviamos los datos al formulario, en encabezado y el detalle
    if request.method=='GET':
        #formulario de compras con el que trabajamos
        form_compras=ComprasEncForm()
        #filtramos la informacion que viene en una variable, el encabezado
        enc = ComprasEnc.objects.filter(pk=compra_id).first()
        
        #---------------------------------------------------------------------
        #encabezado de proveedor. No funciona porque 
        #id_proveedor = ComprasEnc.objects.filter(pk_proveedor=2).first()
        #---------------------------------------------------------------------

        #si hay encabezado
        if enc:
            #filtro el detalle por el id de cabecera (enc) e id de detalle (compra)
            det = ComprasDet.objects.filter(compra=enc)
            fecha_solicitud = datetime.date.isoformat(enc.fecha_solicitud)

            #---------------------------------------------------------------------
            #filtro de productos con proveedor (pk_proveedor es enla BBDD) es igual a lo que tnego en encabezado
            #det_prod = Productos.objects.filter(pk_proveedor=id_proveedor)
            det_prod = Productos.objects.filter(pk_proveedor=enc.pk_proveedor)
            #---------------------------------------------------------------------

            #fecha_factura = datetime.date.isoformat(enc.fecha_factura)
            #inicalizar lo que vamos a mandar, que son los valores del formulario
            e = {
                'fecha_solicitud':fecha_solicitud,
                'pk_empresa': enc.pk_empresa,
                'pk_proveedor': enc.pk_proveedor,
                'observacion': enc.observacion,
                #'no_factura': enc.no_factura,
                #'fecha_factura': fecha_factura,
                'importe': enc.importe,
                'descuento': enc.descuento,
                'total':enc.total
            }
            #le mandamos todos los campos que tiene el formulario
            form_compras = ComprasEncForm(e)
        else:  #si no existe el encabezado el detalle va vacío
            det=None
            #---------------------------------------------------------------------    
            det_prod=None
            #---------------------------------------------------------------------
            
        #lo que le enviamos a la plantilla
        #contexto={'productos':prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}

        #---------------------------------------------------------------------
        contexto={'productos':det_prod,'encabezado':enc,'detalle':det,'form_enc':form_compras}
        #---------------------------------------------------------------------

    #recibimos los datos del formulario
    if request.method=='POST':
        #capturamos todo con el request, el post y el get (+variable)
        fecha_solicitud = request.POST.get("fecha_solicitud")
        
        #¿?
        #if not fecha_compra:
        #    fecha_compra = '2020-12-31'
        #else:
        #    fecha_compra = request.POST.get("fecha_compra")

        observacion = request.POST.get("observacion")
        #no_factura = request.POST.get("no_factura")
        #fecha_factura = request.POST.get("fecha_factura")
        pk_empresa = request.POST.get("pk_empresa")
        pk_proveedor = request.POST.get("pk_proveedor")
        importe = 0
        descuento = 0
        total = 0

        #si el encabezado no existe no se envia
        if not compra_id:
            #capturo al proveedor
            prov=Proveedor.objects.get(pk=pk_proveedor)
            empresa=Empresa.objects.get(pk=pk_empresa)
            #encabezado. Le mandamos los valores con los ue creamos el objeto
            enc = ComprasEnc(
                fecha_solicitud=fecha_solicitud,
                observacion=observacion,
                #no_factura=no_factura,
                #fecha_factura=fecha_factura,
                pk_empresa=empresa,
                pk_proveedor=prov,
                usuario_crea = request.user 
            )
            #si se creo el objeto
            if enc:
                enc.save()
                #inicializo compra_id
                compra_id=enc.id
        else:
            #si existe en encabezado
            #me devuelve el first
            enc=ComprasEnc.objects.filter(pk=compra_id).first()
            if enc:
                enc.fecha_solicitud = fecha_solicitud
                enc.observacion = observacion
                #enc.no_factura=no_factura
                #enc.fecha_factura=fecha_factura
                #enc.usuario_modifica=request.user.id
                enc.usuario_modifica=request.user
                enc.save()

        #si compra_id no tiene nada
        if not compra_id:
            return redirect("sol:html_compras_list")
        
        #ahora el detalle. capturamos todos los datos del detalle
        producto = request.POST.get("id_id_producto")
        unidades = request.POST.get("id_unidades_detalle")
        precio = request.POST.get("id_precio_detalle")
        importe_detalle = request.POST.get("id_importe_detalle")
        descuento_detalle  = request.POST.get("id_descuento_detalle")
        total_detalle  = request.POST.get("id_total_detalle")

        prod = Productos.objects.get(pk=producto)

        #asigno al modelo de ComprasDet los valores del formulario
        det = ComprasDet(
            compra=enc,
            pk_productos=prod,
            unidades=unidades,
            precio=precio,
            descuento=descuento_detalle,
            costo=0,
            usuario_crea = request.user
        )

        #si se creo el objeto lo guardamos
        if det:
            det.save()
            #filtramos: vamos al modelo ComprasDet y usamos un funcion de agragado
            importe=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('importe'))
            descuento=ComprasDet.objects.filter(compra=compra_id).aggregate(Sum('descuento'))
            #actualizamos el encabezado, el valor sub_total es igual a sub_total que va en un arreglo
            enc.importe = importe["importe__sum"]   #django le pone __sum
            #lo paso a una variable
            enc.descuento=descuento["descuento__sum"]
            enc.save()

        return redirect("sol:compras_edit",compra_id=compra_id)

    return render(request, template_name, contexto)

#para borrar el detalle de la compra una vez grabada
class CompraDetDelete(generic.DeleteView):
    permission_required = "apps.sol.html_delete_comprasdet"  #_comprasdet es el modelo
    model = ComprasDet
    template_name = "sol/html_compras_det_del.html"
    context_object_name = 'obj'
    
    def get_success_url(self):
        #sobre escribimos para regresar a la edicion de la compra
        #compra_id tendrá lo que se mande en la url
        compra_id=self.kwargs['compra_id']  #se recibe desde el fichero urls.py, 
            #lo pasamos con kwargs al ser una funcion
        return reverse_lazy('sol:compras_edit', kwargs={'compra_id': compra_id})
