'''
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets

from .models import Empresa
from apps.api.serializers import EmpresaSerializer

from django.contrib.auth import authenticate

from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class EmpresaList(generics.ListCreateAPIView):
    #devuelve una lista
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
'''

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import json
from django.db.models import Sum
from .models import Poblacion, Provincia, Empresa
from .forms import PoblacionForm, ProvinciaForm, EmpresaForm
from django.views import generic
from django.urls import reverse_lazy
from apps.bases.views import SinPrivilegios

class PoblacionView(generic.ListView):
    model = Poblacion
    template_name = "emp/html_poblacion_list.html"
    context_object_name = "obj"
    permission_required="apps.emp.view_poblacion"

class PoblacionEdit(SuccessMessageMixin,generic.UpdateView):
    model=Poblacion
    template_name="emp/html_poblacion_form.html"
    context_object_name = 'obj'
    form_class=PoblacionForm
    success_url= reverse_lazy("emp:poblacion_list")
    success_message="Poblacion Editado"
    permission_required="apps.emp.change_poblacion"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

class PoblacionNew(SuccessMessageMixin,generic.CreateView):
    model=Poblacion
    template_name="emp/html_poblacion_form.html"
    context_object_name = 'obj'
    form_class=PoblacionForm
    success_url= reverse_lazy("emp:poblacion_list")
    success_message="Población Nueva"
    permission_required="apps.emp.add_poblacion"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

#----------------------------------------------------------------

class ProvinciaView(generic.ListView):
    model = Provincia
    template_name = "emp/html_provincia_list.html"
    context_object_name = "obj"
    permission_required="apps.emp.view_provincias"

class ProvinciaEdit(SuccessMessageMixin,generic.UpdateView):
    model=Provincia
    template_name="emp/html_provincia_form.html"
    context_object_name = 'obj'
    form_class=ProvinciaForm
    success_url= reverse_lazy("emp:provincia_list")
    success_message="Provincia Editado"
    permission_required="apps.emp.change_provincias"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

class ProvinciaNew(SuccessMessageMixin,generic.CreateView):
    model=Provincia
    template_name="emp/html_provincia_form.html"
    context_object_name = 'obj'
    form_class=ProvinciaForm
    success_url= reverse_lazy("emp:provincia_list")
    success_message="Provincia Nueva"
    permission_required="apps.emp.add_provincias"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

#----------------------------------------------------------------

class EmpresaView(generic.ListView):
    model = Empresa
    template_name = "emp/html_empresa_list.html"
    context_object_name = "obj"
    permission_required="apps.emp.view_empresas"


class EmpresaModalView(generic.ListView):
    model = Empresa
    template_name = "emp/html_empresa_list_modal.html"
    context_object_name = "obj"
    permission_required="apps.emp.view_empresa"


class EmpresaEdit(SuccessMessageMixin,generic.UpdateView):
    model=Empresa
    template_name="emp/html_empresa_form.html"
    context_object_name = 'obj'
    form_class=EmpresaForm
    success_url= reverse_lazy("emp:empresa_list")
    success_message="Empresa Editado"
    permission_required="apps.emp.change_empresa"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        print(self.request.user.id)
        return super().form_valid(form)

class EmpresaNew(SuccessMessageMixin,generic.CreateView):
    model=Empresa
    template_name="emp/html_empresa_form.html"
    context_object_name = 'obj'
    form_class=EmpresaForm
    success_url= reverse_lazy("emp:empresa_list")
    success_message="Empresa Nueva"
    permission_required="apps.emp.add_empresa"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        #print(self.request.user.id)
        return super().form_valid(form)

@login_required(login_url='/login/')
#@permission_required('apps.sol.view_empresa', login_url='bases:sin_privilegios')
def empresaModal(request,id=None):    
    template_name = "emp/html_empresa_list_modal.html"
    if request.method=='GET':
        #formulario de compras con el que trabajamos
        model = Empresa        
        det = Empresa.objects.all()
        contexto={'obj':det}
    if request.method=='POST':
        #capturamos todo con el request, el post y el get (+variable)
        id_empresa = request.POST.get("id_empresa")
        id_empresa = request.POST.get("id_descripcionempresa")
        return render(request, template_name, contexto)
        