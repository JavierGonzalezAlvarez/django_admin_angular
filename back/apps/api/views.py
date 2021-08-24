from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

#para empresa
from rest_framework import generics
from apps.empresas.models import Empresa
from apps.api.serializers import EmpresaSerializer, UserSerializer

#para que en las llamadas venga el token
from django.contrib.auth import authenticate
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

#python puro
import requests

#para el JWT
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
#from .models import Formulario

#from .serializer import FormularioSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Auth0
import http.client
import io
import json
#the pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form
from pprint import pprint

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
#from rest_framework.response import Response

#obtengo los datos de un usuario
#desde postman puedo hacer un post. en body/form-data
#http://localhost:8000/api/apiauth/
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'firstname': user.first_name,
            'lastname': user.last_name,
            'user_id': user.pk,
            'email': user.email
        })


#ruta http://127.0.0.1:8000/v1/prueba
def prueba(request):
    return HttpResponse("Primer test de inicio aplicación api")

#no se usa ahora
#desde postman puedo hacer un get. he de meter el token
#headers => Authorization "eltoken"
#con este token me devuelve el usuario y la password encritada
#http://localhost:8000/api/auth/
class AuthAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = {
            #'user': str(request.user.email),  # `django.contrib.auth.User` instance.
            #'auth': '89_Lp%wD', #str(request.auth),  # None
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth), #str(request.auth),  # None
        }
        return Response(content)

#http://localhost:8000/api/index/
class IndexAPIView(APIView):    
    #esto invalida la autenticacion especial.
    #con esto entro desde angular
    authentication_classes= ()
    permission_classes= ()
    def get(self, request, format=None):
        content = {
            'msg': 'Index, bienvenido a la api'            
        }
        return Response(content)

#http://127.0.0.1:8000/api/getPayments
@api_view(['GET', 'POST'])
def getPayments(request):
    #authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]    
    if request.method == 'GET': 
        url = "https://com/api/payments?start=2021-01-01&end=2021-12-31"        
        user = "a@gmail.es"
        key = "weT43_%Pj"
        datos = requests.get(url, auth=(user, key))
        if datos.status_code == 200:            
            return HttpResponse(datos)                    
    else:    
        return HttpResponse('<h4>Datos no correctos</h4>')

#Devuelve todos los registros de empresa
class EmpresaList(generics.ListCreateAPIView):
    #devuelve una lista con todos los valores de empresa
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    #esto me permite dar permisos a ciertas vistas
    permission_classes=([IsAuthenticated, IsOwner])

class UserCreate(generics.CreateAPIView):
    #esto invalida la autenticacion especial
    #authentication_classes= ()
    #permission_classes= ()
    #
    serializer_class = UserSerializer

#verificar que el usuario es ok
class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)    

