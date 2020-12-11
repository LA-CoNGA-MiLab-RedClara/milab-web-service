# Servicio Web - MiLAB 

Este repositorio provee tanto los archivos para configurar los contenedores que conforman el servicio web como el servicio web en sí.

## Archivos de variables de entorno

- `env`: Variables de entorno que se utilizan para configurar Django.
- `env.db`: Variables de entorno que se utilizan para configurar la base de datos.
- `env.proxy-companion`: Variables de entorno que se utilizan para la generación de certificados de Let's Encrypt

## Archivos de configuracion de los contenedores

- `docker-compose.yml`: Archivo que define y coordina los contenedores, mapeos de puertos y volúmenes de datos.
- `app/Dockerfile`: Configura el contenedor en el que reside la aplicación web.
- `nginx/Dockerfile`: Configura el contenedor del proxy inverso.

## Consideraciones

- En el archivo `app/milab_web_service/settings.py` se encuentra la configuración de los metadatos del SP, incluyendo datos de contacto y de la organización.
- El servicio en producción debe de usar otro servicio de generacion de certificados digitales, el que está configurado actualmente es especial para desarrollo.
- Se provee el script `app/generate_pair.sh` para generar un par de llaves para la firma de los metadatos del SP. Cuando el sistema entre a producción es necesario usar un par de llaves que no hayan sido autogenerados.
- Para cambiar entre utilizar certificados de producción se debe de comentar la opción `ACME_CA_URI` del archivo `env.proxy-companion`. Hacer esto una vez que no se tenga que estar subiendo y bajando el sitio.
- **No subir pares de llaves a repositorios públicos**.

## Instrucciones

- Para poner el servicio en funcionamiento se debe correr el comando: `docker-compose up -d --build`
- Para revisar los logs de los servicios se puede utilizar el comando: `docker-compose logs -f`
- Para detener el sistema se utiliza el comando: `docker-compose down`

## Explicación de los parámetros del archivo `env`

- `DEBUG`: Cuando este valor es 1 la aplicación está en modo de Debug, cuando hay errores estos se imprimen en el navegador y se redespliega la base de datos cada vez que se redespliega la aplicación, causando pérdida de datos. Hacer un backup antes de activar esta opción.
- `SECRET_KEY`: Sirve para generar ciertos valores criptográficos para Django. Cambiar por algo seguro. (Pero no ponerlo en un repositorio público).
- `SQL_ENGINE`: La biblioteca de Django que utiliza para la base de datos que se está utilizando.
- `SQL_DATABASE`: El nombre de la base de datos.
- `SQL_USER`: El usuario de la base de datos. Cambiar por algo que tenga sentido.
- `SQL_PASSWORD`: La contraseña de la base de datos. Cambiar por algo seguro. (Pero no ponerlo en un repositorio público).
- `SQL_HOST`, `SQL_PORT`: El host y el puerto donde está la base de datos, en este caso corresponden con los creados por Docker, no es necesario cambiar estas opciones.
- `DATABASE`: La base de datos que se está usando.
- `VIRTUAL_HOST`, `VIRTUAL_PORT`: El host y el puerto donde está la aplicación web, en este caso corresponden con los creados por Docker, no es necesario cambiar estas opciones.
- `LETSENCRYPT_HOST`: El host que se le pasa a Let's Encrypt para generar certificados, no es necesario cambiar esta opción.
- `IDP_METADATA_LOCATION`: Sitio donde se alberga la metadata del IdP.
