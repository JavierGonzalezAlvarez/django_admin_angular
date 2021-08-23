from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey

#para django-userforeignkey.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True, verbose_name="Activo")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # uc = models.ForeignKey(User, on_delete=models.CASCADE)
    # um = models.IntegerField(blank=True,null=True)
    
    #cuando se crea que agrege el usuario activo. 
    #   Con el + django anula el mapeo que tiene que hacer en "reversa"
    #   es decir cuando hacemos una busqueda no asigna un nombre a la busqueda con el modelo user
    usuario_crea = UserForeignKey(auto_user_add=True,related_name='+')
    usuario_modifica = UserForeignKey(auto_user=True,related_name='+')    
    #user = models.ForeignKey(User)
    #author = models.ForeignKey('auth.User')
    #author= UserForeignKey('auth.User')    

    class Meta:
        abstract=True
