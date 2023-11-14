Para empezar ingreso a mi carpeta donde se alojara mi proyecto. En este caso cree una nueva llamada 
"Exmen2doParcial".

Para ingresar a nuestro usuario admin debemos escribir la contraseña "admin123".

Desde mi terminal ingrese el siguiente comando "django-admin startproject [nombre del proyecto]" para crear 
un nuevo proyecto y dentro de este ejecute el comando "python manage.py startapp [nombre de la aplicación]"
 para crear mi aplicacion llamada "mynotes".

Como primera accion cree mi modelo "Note" dentro de mi archivo models.py, con los atributos titulo,
contenido y fecha, y con un metoddo que me devolviera el nombre en string.

Dentro de el archivo app.py modificamos el nombre de nuestra App Config por "my notes".

En admin se realizó la importacion del modelo para que el Admin pueda hacer registros a traves del sitio.

La parte de "views" es una de las mas importantes, se encuentra en el archivo views.py y hace referencia 
a lo que se mostrara en esa debida vista. Dentro de esta tenemos las siguientes Views: Lista (donde se muestran 
todos los registro creados), Detalle, Crear (formulario para crear un nuevo rebgistro), Actualizar y Borrar, 
cada uno con su referencia a un respectivo template.

En el archivo urls.py tenemos la urls que se usaran en este proyecto, creamos una para el "index"
(donde se mostraran todos los registros), otra para "detail", que requiere de la primary key para acceder
al respectivo registro, otra para "create", "edit" y  "delete", señalando que estas dos ultimas requieren
de una primary key antes de ir a la respectiva interfaz. Aqui se mandan llamar los view de las respectivas acciones.

A continuacion realizamos la creacion de los Templates, realizamos 4:
note_delete: contiene interfaz donde se muestra un respectivo registro y un boton para eliminar.
note_detail: donde se muestran solo los datos de un registro y puede eliminarse o editarse si asi se requiere.
note_edit: muestra un formulario para ingresar datos actualizados al registro.
note_list: interfaz en la que se muestran todos los registros y la opcion de crear  uno nuevo.


Dentro de settings en la carpeta de "proyect_notes" debemos serciorarnos que este la siguiente linea de codigo:
 "mynotes.apps.MynotesConfig" para que podamos utilizar nuestra app.

Dentro de urls.py de nuestro proyecto incluimos la referencia de las urls de nuestra app.

Para realizarc las pruebas de nuestro proyecto es necesario ejecutar el comando 'python manage.py test mynotes',
con esto se ejecutaran automaticamente y nos dara un resultado. En este cason nuestras pruebas realizan test a 
mostrar la lista de notas, crear, eliminar, actualizar y mostrar los detalles de una nota.

Por ultimo para ejecutar nuestra aplicacion debemos hacerlo con el comando 'python manage.py runserver' y 
buscar en nuestro navegador 'http://127.0.0.1:8000/notas/', esto abrira el sitio ccon nuestra app. 

Esta app se realizo con el fin de crear notas, editarlas, actualizarlas y eliminarlas.




By MelanieGNG
