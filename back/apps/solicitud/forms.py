from django import forms
from .models import Proveedor, ComprasEnc, Productos

class ProveedorForm(forms.ModelForm):
    email = forms.EmailField(max_length=254)
    class Meta:
        model=Proveedor
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Productos
        fields=['pk_proveedor', 'codigo','descripcion','estado', \
                'precio']
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True


class ComprasEncForm(forms.ModelForm):
    fecha_solicitud = forms.DateInput()
    #fecha_factura = forms.DateInput()
    
    class Meta:
        model=ComprasEnc
        fields=['pk_proveedor','pk_empresa','fecha_solicitud','observacion',
            'importe',
            #'no_factura','fecha_factura','sub_total',
            'descuento','total']

    #sobreescribo para que cuando se renderice el formulario haga lo que quiera
    #por ejemplo, la fecha de solo lectura
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['fecha_solicitud'].widget.attrs['readonly'] = True
        #self.fields['fecha_factura'].widget.attrs['readonly'] = True
        self.fields['importe'].widget.attrs['readonly'] = True
        self.fields['descuento'].widget.attrs['readonly'] = True
        self.fields['total'].widget.attrs['readonly'] = True
