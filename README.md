# Gestión de Socios

El Sistema de Gestión de Información para Socios de San Francisco está diseñado para optimizar y facilitar la gestión de datos relacionados con los miembros de la comunidad.

## Backend 

El backend está construido con Django Rest Framework 4.1 y Python 3.10.

### Pasos para la creación del backend

#### Instalación de [Python 3.10](https://www.python.org/downloads/)
1. Descargar y seguir los pasos de la documentación.

#### Instalación de [Django Rest Framework](https://www.django-rest-framework.org/)
1. Instalar un entorno virtual para el proyecto de Django con `python3.10 -m virtualenv`.
2. Activar el entorno virtual de esta forma: `.\venv\Scripts\activate` o de esta forma: `source env/Scripts/activate`.
3. Ejecutar `pip list` para ver los paquetes por defecto.
4. Instalar Django con `pip install django==4.1.*`, recomendado en la documentación para evitar inconvenientes.
5. Ejecutar `pip list` para verificar los paquetes correctos.
6. Instalar Django Rest Framework con `pip install djangorestframework`.
7. Crear el proyecto Django con `django-admin startproject app`.
8. Iniciar el servidor con `python app/manage.py runserver`.

### Iniciar el Proyecto
1. Activar el entorno virtual de esta forma: `.\venv\Scripts\activate` o de esta forma: `source env/Scripts/activate`.
2. Instalar los paquetes ejecutando `pip install -r requirements.txt`.
3. Ejecutar el backend con `python app/manage.py runserver`.