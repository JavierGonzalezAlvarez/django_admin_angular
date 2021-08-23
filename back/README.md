------------------------------------------------------------------------------
# Admin de Django en back, Api - DRF, Django 3.2 y Angular 11 (en curso)
------------------------------------------------------------------------------
# ENTORNO VIRTUAL
-------------------------------------------------
## Instalar entorno virtual (virtualenv) en linux
sudo apt install python3-virtualenv

## Crear entorno virtual
virtualenv entorno_virtual -p python3
ó
python3 -m venv entorno_virtual
esto crea una carpeta y dentro esta la carpeta /bin

## Activar entorno virtual
source entorno_virtual/bin/activate

# Desativar entorno virtual
deactivate

## install requirements
pip install -r requirements.txt 

## crear proyecto
django-admin startproject apimq

## Configuramos el archivo settings 
bd: apiadmin
base de datos (crear antes)

cambiar el acceso a postgres, quitando sqlite3 en settings

## cambiar el nombre de la apidj a config
en ficheros:
- asgi.py
- manage.py
- settings.py
- wsgi.py
cambiamos el nombre

## la conexion debe ser el puerto correcto de linux:
comprobar puerto de postgresql
$ sudo pg_isready

## crear app
python manage.py startapp stock
python manage.py startapp pgou
python manage.py startapp catastro
python manage.py startapp ibi
python manage.py startapp solicitud

mover a driectorio apps

## Hacer migraciones de tablas de la BBDD. Desde donde esta el fichero manage.py
$ python manage.py makemigrations

# desde el servidor ejecutamos collectstatic
python3 manage.py collectstatic

# desde servidor
python3 manage.py makemigrations
python manage.py makemigrations

## Para ver lo que se migra antes
$ python manage.py showmigrations

## Migrar a una base de datos especifica
$ python manage.py migrate

## crear usuario
python manage.py createsuperuser
javier
89_Lp%wD

## Ejecutar el  servidor
$ python manage.py runserver
http://127.0.0.1:8000/

me dira que solo puedo ir a dos rutas: admin y ...v1/

## consola de la bd
$ python manage.py dbshell
$ psql nombre_base_de_datos
$ \dt

## registrar la api en settings.py
INSTALLED_APPS = [
    ...
    'api',
]

## Instalacion de CORS
pip install django-cors-headers

en fichero settings.py
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ....
]

INSTALLED_APPS = [
    ...
    'corsheaders',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

## acceso a api de prueba
https://.com/admin/login
a@gmail.es
weT43_%Pj

# cargar django-admin pluggin
Se añade en requirements.txt
django-admin-interface

# postgres en pc linux
psql -h 127.0.0.1 -U postgres
pss:

# entrar en contenedor postgres
psql -d apiadmin -U javier
-ver la actividad de la bd
SELECT * FROM pg_stat_activity WHERE datname='apiadmin';

# borrar la db para hacer de nuevo migraciones, desde local (no docker)
-entrar en postgres con otro usuario
psql -d postgres -U javier
DROP DATABASE "apiadmin";
-crear la bd
CREATE DATABASE apiadmin WITH OWNER javier;

# exportar db
pg_dump -O --dbname=apiadmin://javier:2525_ap@postgresql.guebs.net:5432/apiadmin > dump.sql


# ver tablas:
\dn+
\dt *.*

# dar permisos al usuario para las tablas
GRANT ALL ON SCHEMA public TO public;
GRANT ALL ON ALL TABLES IN SCHEMA pg_catalog TO javier; 

ver campos de tablas
\dt pg_database
listar valores de la tabla
\d pg_database

