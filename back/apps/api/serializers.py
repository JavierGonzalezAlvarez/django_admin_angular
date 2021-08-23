#Creamos este fichero
from rest_framework import serializers
from apps.empresas.models import Empresa, Provincia
from apps.gdocumental.models import GDocumental, GDClasificacion

#importamos usuarios para que solo usuarios permitidos uedan crear usuarios
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class EmpresaSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(
    #    default=serializers.CurrentUserDefault()
    #    )
    class Meta:
        #el modelo es producto
        model=Empresa
        #quiero todos los campos, lo indico así:
        fields='__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(
    #    default=serializers.CurrentUserDefault()
    #    )
    class Meta:
        #el modelo es categoria
        model=Provincia
        #quiero todos los campos, lo indico así:
        fields='__all__'


class GDocumentalSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(
    #    default=serializers.CurrentUserDefault()
    #    )
    class Meta:        
        model=GDocumental        
        fields='__all__'

class GClasificacionSerializer(serializers.ModelSerializer):
    #owner = serializers.HiddenField(
    #    default=serializers.CurrentUserDefault()
    #    )
    class Meta:
        #el modelo es subcategoria
        model=GDClasificacion
        #quiero todos los campos, lo indico así:
        fields='__all__'

#para que solo los usuarios permitidos puedan crear
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        #que no devuelva la contraseña en el response
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user