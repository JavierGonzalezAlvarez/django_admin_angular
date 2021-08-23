from django.urls import path, include
from .views import prueba
from .views import getPayments #, getBalanceStripe
from rest_framework import routers
from apps.api import views

#from apps.bases.views import Class_Home, HomeSinPrivilegios

from rest_framework.routers import DefaultRouter
#otra forma de obtener el token
#from rest_framework.authtoken import views

#creamos un enrutamiento y lo inicializamos
router = routers.DefaultRouter()

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

#from rest_framework_swagger.views import get_swagger_view
#schema_view = get_swagger_view(title='RestFul Api DRF')

#from rest_framework.documentation import include_docs_urls

#mapeamos la vista
#router.register(r'docs', DocumentoViewSet)

urlpatterns = [
    #cuando no especifiquen nada, responde router.urls - DRF
    #path => http://localhost:8000/
    #path('',include(router.urls)), 

    path('prueba', prueba, name="prueba"),

    #path => http://127.0.0.1:8000/api/getBalanceStripe
    #path('getBalanceStripe/', views.GetBalanceStripeAPIView.as_view()),
    #path('getBalanceStripe', getBalanceStripe, name="getBalanceStripe"),   
     
    #path => http://localhost:8000/api/getPayments
    path('getPayments', getPayments, name="getPayments"),        

    #path('post', post, name="post"),

    #http://localhost:8000/api/auth/
    path('auth/', views.AuthAPIView.as_view()),
    
    #http://localhost:8000/api/index/
    #entrada desde angular
    path('index/', views.IndexAPIView.as_view()),    

    #http://localhost:8000/api/empresas/
    path('empresas/', views.EmpresaList.as_view()),

    #http://localhost:8000/api/usuarios/
    path('usuarios/', views.UserCreate.as_view(),name='Usuarios'),

    path ('login/', views.LoginView, name="login"),
    
    path('apiauth/', views.CustomAuthToken.as_view()),

    # otra forma de devolver el token por DRF
    #path ("login-drf/", views.obtain_auth_token, name="login_drf"),

    #path ('swagger/', schema_view),

    #coreapi
    #path ("coreapi/", include_docs_urls(title="Documentacion CoreApi DRF")),
    #path('openapi/', get_schema_view(title="Your Project", description="API for all things …"), name='openapi-schema'),
    
    #path ("coreapi-docs/", include_docs_urls(title="Documentacion CoreApi DRF")),

    #para los tokens
    #path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
