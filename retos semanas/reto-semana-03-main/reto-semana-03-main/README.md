# Analizador de Ventas | Reto Semana 3

Este programa agrupa todas las transacciones del mismo producto para calcular el total de unidades vendidas, el ingreso total y el precio promedio[cite: 2]. Los resultados se presentan ordenados de mayor a menor ingreso

## Instrucciones de Uso

### Requisitos Previos
* Asegúrate de tener Python instalado.
* Ejecutar los comandos desde la carpeta raíz del proyecto.

### 1. Ejecución con archivo de entrada
* **Linux / Mac:** `python main.py < tests/entrada.txt`
* **Windows (PowerShell):** `Get-Content "tests\entrada.txt" | python .\main.py`
* **Windows (CMD):** `type "tests\entrada.txt" | python main.py`

### 2. Ejecución manual
Puedes escribir los datos directamente en la terminal, línea por línea, sin necesitar un archivo.
* **Linux / Mac:** `python main.py`
* **Windows (PowerShell):** `python .\main.py`
* Flujo de ingreso de datos:**
* Después de ejecutar el comando, escribe los datos de la cabecera: `fecha,producto,cantidad,precio_unitario` y presiona Enter
* Escribe cada transacción (ej. `2026-01-01,Laptop,2,15000.00`) y presiona Enter.
* Cuando termines de ingresar todos los datos, presiona `Ctrl + D` en Linux / Mac, o `Ctrl + Z` y luego Enter en Windows

### 3. Guardar la salida en un archivo
* **Linux / Mac:** `python main.py < tests/entrada.txt > tests/salida.txt`
* **Windows (PowerShell):** `Get-Content "tests\entrada.txt" | python .\main.py | Out-File -FilePath "tests\salida.txt" -Encoding utf8`
* **Windows (CMD):** `type "tests\entrada.txt" | python main.py > "tests\salida.txt"`
### 4. Generar datos de prueba
* Para generar 100 registros sin errores: `python generar_entrada.py 100 | python main.py`
* Para generar 100 registros con 20% de errores: `python generar_entrada.py 100 20 | python main.py`

---

## Formato de Datos y Ejemplos

La estructura requiere un encabezado específico seguido de las transacciones
**Ejemplo de entrada (`entrada.txt`):**
```csv
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
2026-01-06,Monitor,3,6000.00
2026-01-07,Laptop,2,15500.00
2026-01-08,Audifonos,20,350.00
2026-01-09,Mouse,5,275.00
2026-01-10,Monitor,2,5800.00
```

**Ejemplo de salida (`salida.txt`):**
```csv
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,5,75500.00,15100.00
Monitor,5,29600.00,5920.00
Audifonos,20,7000.00,350.00
Mouse,23,5875.00,255.43
Teclado,5,4000.00,800.00
```

## Lógica de Procesamiento

* El programa toma todas las transacciones del archivo de entrada y las consolida por producto
* Las unidades se suman y el ingreso total se calcula multiplicando cada cantidad por su precio unitario[
* El resultado se ordena de mayor a menor ingreso, colocando los productos más rentables al inicio[
* Las líneas con datos inválidos como columnas faltantes o valores no numéricos se ignoran automáticamente, por lo que no afectan los cálculos ni aparecen en la salida
* El precio promedio no es el promedio simple de los precios, sino el ingreso total dividido entre las unidades vendidas. Esto refleja el valor real promedio por unidad considerando todas las transacciones del producto

---
**Desarrollado por:** Manuel Hernandez Rodriguez
