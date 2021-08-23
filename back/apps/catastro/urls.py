from django.urls import path, include
from .views import CatastroView, CatastroEdit, CatastroNew, GestionDocumentalPdf

from .views import pdf_view_1, pdf_view, pdf_view_2, GeneratePdf
from .reportes import reporte_all, imprimir_one


#from django.conf import settings
#from django.conf.urls.static import static
#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('catastro/',CatastroView.as_view(), name="catastro_list"),
    path('catastro/new',CatastroNew.as_view(), name="catastro_new"),
    path('catastro/pdf/<int:pk>',GestionDocumentalPdf.as_view(), name="catastro_pdf"),
    path('catastro/edit/<int:pk>',CatastroEdit.as_view(), name="catastro_edit"),

    path('pdf/', pdf_view_1, name="pdf"),        

    path('catastro/listado/', reporte_all, name='catastro_pdf_all'),
    
    #path('catastro/<int:compra_id>/imprimir', imprimir_one,name="compras_print_one"),

    #path('pdf_1/', GeneratePdf.as_view(), name="pdf"),   
    #path('catastro/inactivar/<int:id>',provinciaInactivar, name="proveedor_inactivar"),
    
]