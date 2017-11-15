# demo-python
Demo Python 3.5
#############		Python + Django			##################################################################################################

Hay diferencias a nivel sintático entre Python 2.7 con Python 3.5
Un proyecto que funciona en Python 3.5 SI funciona en Python 2.7. En cambio, uno que funciona en Python 2.7 NO funciona en Python 3.5

# Descarga proyectos Django
https://www.djangopackages.com/

# GitHub Django
https://github.com/montylounge/django-mingus

Los proyectos django suelen tener una estructura similar, con un fichero manage.py y al mismo nivel las "apps". 
Cada app es un paquete de python que contiene toda la logica para dicha app (views, urls, models, etc).
Los proyectos Python siguen una metodologia MVT Model View Template donde:
1.- Model corresponde a Model como MVC Java
2.- View corresponde al Controller de MVC Java
3.- Template corresponde al View de MVC Java

Las urls contienen la definicion de los patrones de url de dicha app junto con la view (el controlador, que en django llamamos view) 
que lo controla.

Las views, definen las clases o las funciones que manejan las peticiones a dichas urls.

Los models, definen los objetos que tenemos en la base de datos. Normalmente se definen los modelos y luego se realizan migraciones, 
transformando ese modelo a una entidad en la base de datos. 
Para ello, Django tiene una serie de commandos propios.
Internamente, cada app tambien dispone de una serie de modulos (se crean manualmente) como:
	1.- las templates (ficheros html que seran las que usemos al renderizar las vistas)
	2.- statics (contiene los ficheros estaticos como css, js etc)
	3.- forms (clases que usamos para definir los formularios de nuestro site), migrations (migraciones que hayamos realizado), etc


##	Comandos
#	Cargar virtualEnv  
C:\Users\CONSULTANT\PycharmProjects\telefonica>..\..\vmenvtelefonica\Scripts\activate

#	Arrancar servidor
(vmenvtelefonica) C:\Users\CONSULTANT\PycharmProjects\telefonica>python manage.py runserver

#	Acceder al proyecto telefonica que contiene la aplicacion applicacion1
https://127.0.0.1/8000		(Falta dar de alta la base de datos. la base de datos por defecto es SQLite

#	Crear un nuevo package o aplicacion dentro del proyecto telefonica
(vmenvtelefonica) C:\Users\CONSULTANT\PycharmProjects\telefonica>python manage.py startapp applicacion2

#	Si añadimos en models.py cualquier class(entidad) debemos ejecutar la migraciones
(vmenvtelefonica) C:\Users\CONSULTANT\PycharmProjects\telefonica>python manage.py makemigrations
(vmenvtelefonica) C:\Users\CONSULTANT\PycharmProjects\telefonica>python manage.py migrate

#   Visualizar administracion
http://localhost:8000/admin with:
User: admin
Pwd: Ni....11

#   Visualziar aplicacion 1
http://localhost:8000/admin/aplicacion1/
