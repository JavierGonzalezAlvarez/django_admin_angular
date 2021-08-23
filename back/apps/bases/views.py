from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404, redirect
from django.views import generic

#from .forms import PaginaForm

#Django necesita que importemos estas clases en views.py
#Las mayusculas y minusculas importan en python
from django.http import HttpResponse  

#Añado Template
#from django.views.generic import TemplateView,

#Con esto me aparece context en el menu inteligente de VSC
from django.template import Template, Context

#import datetime
#Para devolver a una URL despues de una acción
from django.urls import reverse, reverse_lazy

#--------------------------------------------------------------
#Mixins
#Importo la Clase LoginRequiredMixin
#Para que si un suario está logeado, que pase a admin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#--------------------------------------------------------------
#redirect
from django.http import HttpResponseRedirect

# Create your views here.

#Clase que hereda de generic una clase llamada TemplateView
#Ahora le digo a Home que herede de Login... y de TemplateView
#Los mixin deben de colocarse a la izquierda. El orden es importante, para dar prioridad

#class Class_Home(generic.TemplateView):
class Class_Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/.html'        
    login_url = 'bases:html_login'

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:html_login"
    template_name="bases/sin_privilegios.html"    

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin):
    #login_url lo heredaremos de la herencia multiple en views.py de inv
    login_url = 'bases:html_login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        #para que el usuario no pueda entrar a un url si no está logeado
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))



