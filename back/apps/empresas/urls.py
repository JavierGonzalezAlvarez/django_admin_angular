'''
from django.urls import path, include
from .views import EmpresaList
from rest_framework import routers

#creamos un enrutamiento y lo inicializamos
#router = routers.DefaultRouter()
#mapeamos la vista
#router.register(r'docs', DocumentoViewSet)

urlpatterns = [
    #cuando no especifiquen nada, responde router.urls - DRF
    #path => http://localhost:8000/
    #path('',include(router.urls)),    

    #http://localhost:8000/api/empresas/
    path('empresas/', views.ListCreateAPIView.as_view()),
    
]
'''

from django.urls import path, include
from .views import PoblacionView, PoblacionEdit, PoblacionNew
from .views import ProvinciaView, ProvinciaEdit, ProvinciaNew
from .views import EmpresaView, EmpresaEdit, EmpresaNew, empresaModal, EmpresaModalView

#from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path('poblacion/',PoblacionView.as_view(), name="poblacion_list"),
    path('poblacion/new',PoblacionNew.as_view(), name="poblacion_new"),
    path('poblacion/edit/<int:pk>',PoblacionEdit.as_view(), name="poblacion_edit"),
    #path('poblacion/inactivar/<int:id>',provinciaInactivar, name="proveedor_inactivar"),

    path('provincia/',ProvinciaView.as_view(), name="provincia_list"),
    path('provincia/new',ProvinciaNew.as_view(), name="provincia_new"),
    path('provincia/edit/<int:pk>',ProvinciaEdit.as_view(), name="provincia_edit"),
    #path('provincia/inactivar/<int:id>',provinciaInactivar, name="proveedor_inactivar"),

    path('empresa/',EmpresaView.as_view(), name="empresa_list"),
    #path('empresa/modal',empresaModal, name="empresa_list_modal"),
    path('empresa/modal',EmpresaModalView.as_view(), name="empresa_list_modal"),
    path('empresa/new',EmpresaNew.as_view(), name="empresa_new"),
    path('empresa/edit/<int:pk>',EmpresaEdit.as_view(), name="empresa_edit"),
    #path('provincia/inactivar/<int:id>',provinciaInactivar, name="proveedor_inactivar"),



    #path('compras/',ComprasView.as_view(), name="compras_list"),
    #path('compras/new',compras, name="compras_new"),
    #path('compras/edit/<int:compra_id>',compras, name="compras_edit"),
    #path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

    #path('compras/listado', reporte_compras, name='compras_print_all'),
    #path('compras/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),
]