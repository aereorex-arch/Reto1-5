# reto-semana-01
Aqui se subira el reto de la semana 01
# Procesador de Ventas Diarias

Este programa lee reportes de ventas diarios desde la entrada estándar, limpia los datos "sucios" (espacios extra, caracteres inválidos, líneas vacías) y calcula el total de ventas truncado a número entero. Es una herramienta robusta diseñada para procesar datos inconsistentes de diferentes sucursales.

## Instrucciones de uso

El script está escrito en Python 3 y procesa la información leyendo directamente desde la entrada estándar (`stdin`). 

Para ejecutarlo en una terminal de Linux o Mac, puedes usar cualquiera de estos dos métodos:

**Método 1: Redirección de archivo**
```bash
python3 main.py < entrada.txt

Ejemplo de entrada y salida
 

                 si tienes un archivo entrada.txt con el siguiente contenido:


1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
  5 , 10 , 15

  Al ejecutar el programa, la salida en la terminal será:


6
10
0
6
19
8
30
Autor
[Hernandez Rodriguez Manuel]