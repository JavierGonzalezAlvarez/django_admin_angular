# copia de la base de datos

## desde este directorio, exportar:
/back/db
pg_dump -U javier -f pg_copia.sql apiadmin

## desde este directorio, borrar:
-entrar en postgres con otro usuario
psql -d postgres -U javier

-borrar la db
DROP DATABASE apiadmin;

-crear la bd
CREATE DATABASE apiadmin WITH OWNER javier;

## desde este directorio, importar:
/back/db
-entrar en postgres con otro usuario
psql -d postgres -U javier

-borrar la db
DROP DATABASE apiadmin;

-crear la bd
CREATE DATABASE apiadmin WITH OWNER javier;

-importar: es desde $, fuera de postgress
psql -U javier -W -h localhost apiadmin < pg_copia.sql
