from django import forms
from .models import Provincia, Poblacion, Empresa

class PoblacionForm(forms.ModelForm):
    descripcion = forms.CharField(max_length=254)
    class Meta:
        model=Poblacion
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ProvinciaForm(forms.ModelForm):    
    class Meta:
        model=Provincia
        fields=['descripcion']

    #sobreescribo para qe cuando se renderice el formulario haga lo que quiera
    #por ejemplo, la fecha de solo lectura
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        #self.fields['fecha_compra'].widget.attrs['readonly'] = True
        #self.fields['fecha_factura'].widget.attrs['readonly'] = True
        #self.fields['sub_total'].widget.attrs['readonly'] = True
        #self.fields['descuento'].widget.attrs['readonly'] = True
        #self.fields['total'].widget.attrs['readonly'] = True

class EmpresaForm(forms.ModelForm):
    codigoempresa=forms.CharField(max_length=4)  
    descripcion = forms.CharField(max_length=255)
    nif = forms.CharField(max_length=255)
    fecha_creacion = forms.DateInput()
    cnae = forms.CharField()

    class Meta:
        model=Empresa
        exclude = ['um','fm','uc','fc']
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
