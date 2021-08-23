from django.urls import path, include

from .views import ProveedorView, ProveedorNew, ProveedorEdit #, proveedorInactivar

from .views import ProductoEdit, ProductoView, ProductoNew

from .views import ComprasView, compras, CompraDetDelete
from .reportes import reporte_compras, imprimir_compra

urlpatterns = [
    path('proveedores/',ProveedorView.as_view(), name="proveedor_list"),
    path('proveedores/new',ProveedorNew.as_view(), name="proveedor_new"),
    path('proveedores/edit/<int:pk>',ProveedorEdit.as_view(), name="proveedor_edit"),
    #path('proveedores/inactivar/<int:id>',proveedorInactivar, name="proveedor_inactivar"),

    path('productos/',ProductoView.as_view(), name="producto_list"),
    path('productos/new',ProductoNew.as_view(), name="producto_new"),
    path('productos/edit/<int:pk>',ProductoEdit.as_view(), name="producto_edit"),

    path('compras/',ComprasView.as_view(), name="compras_list"),
    path('compras/new',compras, name="compras_new"),
    path('compras/edit/<int:compra_id>',compras, name="compras_edit"),
    path('compras/<int:compra_id>/delete/<int:pk>',CompraDetDelete.as_view(), name="compras_del"),

    path('compras/listado', reporte_compras, name='compras_print_all'),
    path('compras/<int:compra_id>/imprimir', imprimir_compra,name="compras_print_one"),


]