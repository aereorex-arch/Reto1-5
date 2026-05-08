# Reto Semana 2 - Clasificador de Temperaturas

Programa en Python que lee temperaturas de ciudades desde stdin, las convierte a Celsius y las clasifica.

## Uso

```bash
python main.py < entrada1.txt
```

## Formato de Entrada

La primera línea es el encabezado (se ignora):

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
```

- `ciudad`: nombre de la ciudad
- `temperatura`: número entero o decimal
- `unidad`: `C` (Celsius) o `F` (Fahrenheit)

Las filas con temperatura no numérica, unidad inválida o menos de 3 columnas se ignoran automáticamente.

## Formato de Salida

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
```

La temperatura siempre se muestra con 1 decimal.

## Clasificaciones

| Rango (°C)     | Clasificación |
|----------------|---------------|
| < 0            | Congelante    |
| 0 – 15         | Frio          |
| 16 – 25        | Templado      |
| 26 – 35        | Calido        |
| > 35           | Extremo       |

## Ejemplo

Entrada (`entrada1.txt`):
```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Error,abc,C
```

Salida:
```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
```

## Autor

Hernandez Rodriguez Manuel   
IPN - Programación para Ciencia de Datos 2026
