# [INF331] Tarea1

Tarea numero 1 de la asignatura INF331-Pruebas de Software, donde se debe crear un programa que compare el largo de dos strings

## Descripcion

El proposito de este programa es comparar 2 strings y mostrar por pantalla si uno es mas largo que el otro o si tienen largos iguales, ademas crea un archivo llamado "log_prueba_tarea1_inf331.txt" donde se agrega una linea con la fecha de ejecución, los strings ingresados y el resultado de la comparacion cada ve que el programa es ejecutado con exito.

Si se ingresan simbolos unicode, estos se escribiran codificados en utf-8 en el documento.




## Ejecucion

Para ocupar correctamente el programa se debe ejecutar en un jupyter notebook en el IDLE de python. Es decir si se quieren incluir simbolos en unicode. 

Si las cadenas pertencen a utf-8 entonces basta con tener una version de python 3.x.x y ejecutar el programa en el ambiente que prefiera.

Como el programa genera un documento se deben tener permisos suficientes para esto al ejecutar el programa.


El codigo fue escrito en python version 3.6.9

En ubuntu se ejecutaria de la siguiente forma estando en el directorio donde se encuentra el archivo "Tarea1.py"

```bash
python3 Tarea1.py
```

## Usage

Luego de ejecutar el programa este pedira primero un string donde se debe escribir la cadena que se desee comparar y luego presionar enter, despues pedira un segundo string donde se debe realizar el mismo procedimiento que para el primer string.

El programa solo recibe cadenas de largo mayor a 0, por lo que si no se ingresa ninguna cadena el programa pedira una hasta que se ingrese alguna

```bash
'ingrese string 1 :'
cadenadeprueba1
'ingrese string 2 :'
cadena de prubea 2
'String 2 es el más largo'
'Para finalizar el programa presione la tecla Enter'

```

* Se suprimio el uso de tildes en este readme
