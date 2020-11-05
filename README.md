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
- **No subir pares de llaves a repositorios públicos**.

## Instrucciones

- Para poner el servicio en funcionamiento se debe correr el comando: `docker-compose up -d --build`
- Para revisar los logs de los servicios se puede utilizar el comando: `docker-compose logs -f`
- Para detener el sistema se utiliza el comando: `docker-compose down`

