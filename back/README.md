------------------------------------------------------------------------------
# Admin de Django en back, Api - DRF, Django 3.2 y Angular 11 (en desarrollo)
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

#v Desativar entorno virtual
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

## desde el servidor ejecutamos collectstatic
python3 manage.py collectstatic

## desde servidor
python3 manage.py makemigrations
python manage.py makemigrations

## Para ver lo que se migra antes
$ python manage.py showmigrations

## Migrar a la base de datos
$ python manage.py migrate

## crear usuario
python manage.py createsuperuser
javier
89_Lp%wD

o

python manage.py createsuperuser --username=jga --email=javier@gmail.com

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

#v cargar django-admin pluggin
Se añade en requirements.txt
django-admin-interface

## postgres en pc linux
psql -h 127.0.0.1 -U postgres
pss:

## entrar en contenedor postgres
psql -d apiadmin -U javier
-ver la actividad de la bd
SELECT * FROM pg_stat_activity WHERE datname='apiadmin';

## borrar la db para hacer de nuevo migraciones, desde local (no docker)
-entrar en postgres con otro usuario
psql -d postgres -U javier
DROP DATABASE "apiadmin";
-crear la bd
CREATE DATABASE apiadmin WITH OWNER javier;

## exportar db
pg_dump -O --dbname=apiadmin://javier:2525_ap@postgresql.guebs.net:5432/apiadmin > dump.sql


## ver tablas:
\dn+
\dt *.*

## dar permisos al usuario para las tablas
GRANT ALL ON SCHEMA public TO public;
GRANT ALL ON ALL TABLES IN SCHEMA pg_catalog TO javier; 

ver campos de tablas
\dt pg_database
listar valores de la tabla
\d pg_database

## override Admin Template y CSS
------------------------------------
entorno_virtual/lib/python3.8/site-packages/django/contrib/admin
-admin
-registration

# override ADMIN
## cambiar css
copiar fichero base.css en static/admin/css/base.css

en fichero config.py indicar directorio 2static":
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

modificar algún color:
base.css -> 
-linea 21
a. #header
    background: #228a4a;
b. :root 
--header-color:

-linea 50
  /* --default-button-bg: var(--secondary); */
  --default-button-bg: #fa3503 ;

## cambiar html
copiar fichero base.html en templates/admin/base.html
base.html
-linea 43
    {# añadir el email del usuario #}
    - {{ user.email }} -                          


## instalar sphinx en una carpeta creada
$ mkdir docs
$ cd docs
$ docs\pip install sphinx
- index.rst file
- reStructuredText
# configurar el proyecto con sphinx:
preguntas para configurar sphinx
$ docs/sphinx-quickstart
- Separar directorios fuente y compilado (y/n) [n]: y
- ...
- Liberación del proyecto []: 0.1
- Lenguaje del proyecto [en]: en

crea:
-conf.py
-index.rst
-Makefile

# ingresar datos
hacer los cambios de informacion en:
docs/source/index.rst

# crear directorio html, 
docs\ $make html
# install liveserver extension
c docs\build\html\index.html
# change the theme
docs\ $ pip install sphinx_rtd_theme

# source\config.py
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'

cd docs\ $ make html
docs\build\html\index.html

Cada vez que se hacen cambios en  source\index.rst: hacemos
docs\ $make html

# modificar texto en source\index.rst. Documentación:
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
https://docutils.sourceforge.io/docs/user/rst/quickref.html#hyperlink-targets
crear directorio => source\images
ie: Headings => ====





    