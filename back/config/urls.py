from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.staticfiles import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    #ruta de DRF  
    path('', include(('apps.api.urls', 'index'), namespace = 'index')),    
    path('api/', include(('apps.api.urls', 'api'), namespace = 'api')),  
    #ruta de App
    #path('', include(('apps.bases.urls', 'index'), namespace = 'bases')),    

    path('empresas/', include(('apps.empresas.urls', 'emp'), namespace='emp')),
    path('catastro/', include(('apps.catastro.urls', 'cat'), namespace='cat')),
    path('solicitud/', include(('apps.solicitud.urls', 'sol'), namespace='sol')),    

    #path('<path:path>', views.serve),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#django no sirve ficheros en debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Empresas - Promotora"
admin.site.site_title = "Portal de Empresas"
admin.site.index_title = "Backend Admin"

