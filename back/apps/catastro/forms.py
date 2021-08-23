from django import forms
from .models import Catastro
from apps.gdocumental.models import GDocumental

class CatastroForm(forms.ModelForm):
    #pk_empresa = forms
    #pk_gestion_documental=forms
    descripcion_catastral = forms.CharField(max_length=50)
    referencia_catastral = forms.CharField(max_length=50)    
    class Meta:
        model=Catastro
        exclude = ['usuario_modifica','fecha_modificacion','usuario_crea','fecha_creacion', 'pk_gestion_documental']
        widget={'descripcion castastral': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class CatastroPDFForm(forms.ModelForm):
    #pk_empresa = forms
    #pk_gestion_documental=forms
    #descripcion_catastral = forms.CharField(max_length=50)
    #referencia_catastral = forms.CharField(max_length=50)    
    class Meta:
        model=Catastro        
        exclude = ['usuario_modifica','fecha_modificacion','usuario_crea','fecha_creacion']
        widget={'descripcion castastral': forms.TextInput()}
        fields = ['pk_gestion_documental']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class GDFormPDF(forms.ModelForm):
    #pk_empresa = forms
    #pk_gestion_documental=forms
    
    #form.pk_gestion_documental.queryset=pk_gestion_documental.objects.filter(pk_gestion_documental=1)        
    #self.fields['category'].queryset = models.GDocumental.objects.filter(user=user)
    #form.rate.queryset = Rate.objects.filter(company_id=the_company.id)
    #pk_gestion_documental = forms.pk_gestion_documental(queryset=pk_gestion_documental.objects.all())

    gd = forms.ModelChoiceField(
        queryset = Catastro.objects.filter(pk_gestion_documental=1)
    )

    descripcion = forms.CharField(max_length=50)
    #referencia_catastral = forms.CharField(max_length=50)    
    class Meta:
        model=GDocumental
        exclude = ['um','fm','uc','fc']
        widget={'ficheros': forms.TextInput()}
        fields = ['gd', 'descripcion', 'fichero_pdf']
        #fields = ['descripcion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
