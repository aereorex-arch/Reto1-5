# Validador de Códigos con Expresiones Regulares

**Reto Semana 6 — Programación para Ciencia de Datos**

Script de línea de comandos desarrollado en Python que valida códigos de productos, envíos, empleados y facturas de una empresa de logística usando expresiones regulares.

El código está organizado de forma modular, separando cada responsabilidad en funciones independientes, lo que facilita su mantenimiento y extensión futura.

---

## Requisitos Previos

- Python 3.7 o superior instalado en tu sistema
- Archivo de entrada con un código por línea (formato `.txt`)
- Ejecutar los comandos desde la carpeta raíz del proyecto

---

## Reglas de Validación

| Tipo | Formato | Reglas de Validación |
|------|---------|---------------------|
| **Producto** | `CAT-NNNN-PA` | Categoría y país en MAYÚSCULAS; número de 4 dígitos |
| **Envío** | `ENV-AAAA-MM-DD-NNNNNN` | Año 2020-2030; mes 01-12; día 01-31; número de 6 dígitos |
| **Empleado** | `EMP-DEP-NNNN` | Departamento: VEN, ADM, TEC, LOG o RHH; número no puede empezar con 0 |
| **Factura** | `FAC-S-NNNNNN` | Serie: A, B, C, D o E en MAYÚSCULA; número de 6 dígitos |
| **Desconocido** | Cualquier otro | No coincide con los formatos anteriores; siempre INVALIDO |

---

## Instrucciones de Ejecución

### En Windows (PowerShell)
```powershell
Get-Content tests\codigos.txt | python main.py
```

### En Windows (CMD)
```cmd
python main.py < tests\codigos.txt
```

### En Linux / macOS
```bash
python3 main.py < tests/codigos.txt
```

### Guardar resultados en archivo

**PowerShell:**
```powershell
Get-Content tests\codigos.txt | python main.py | Out-File -Encoding utf8 resultados.csv
```

**CMD:**
```cmd
python main.py < tests\codigos.txt > resultados.csv
```

**Linux / macOS:**
```bash
python3 main.py < tests/codigos.txt > resultados.csv
```

---

## Ejemplo de Uso

### Entrada (`codigos.txt`)
```
TEC-0001-MX
ALI-9999-US
ROB-1234-CA
tec-0001-MX
TEC-001-MX
TECH-0001-MX
ENV-2024-03-15-001234
ENV-2025-12-01-999999
ENV-2019-03-15-001234
ENV-2024-13-15-001234
ENV-2024-03-32-001234
EMP-VEN-1234
EMP-TEC-9999
EMP-ADM-1000
EMP-VEN-0123
EMP-XXX-1234
EMP-VEN-123
FAC-A-123456
FAC-E-000001
FAC-B-999999
FAC-F-123456
FAC-A-12345
FAC-a-123456
XXX-1234
RANDOM-CODE
```

### Salida (`resultados.csv`)
```
codigo,tipo,valido
TEC-0001-MX,producto,VALIDO
ALI-9999-US,producto,VALIDO
ROB-1234-CA,producto,VALIDO
tec-0001-MX,producto,INVALIDO
TEC-001-MX,desconocido,INVALIDO
TECH-0001-MX,desconocido,INVALIDO
ENV-2024-03-15-001234,envio,VALIDO
ENV-2025-12-01-999999,envio,VALIDO
ENV-2019-03-15-001234,envio,INVALIDO
ENV-2024-13-15-001234,envio,INVALIDO
ENV-2024-03-32-001234,envio,INVALIDO
EMP-VEN-1234,empleado,VALIDO
EMP-TEC-9999,empleado,VALIDO
EMP-ADM-1000,empleado,VALIDO
EMP-VEN-0123,empleado,INVALIDO
EMP-XXX-1234,empleado,INVALIDO
EMP-VEN-123,desconocido,INVALIDO
FAC-A-123456,factura,VALIDO
FAC-E-000001,factura,VALIDO
FAC-B-999999,factura,VALIDO
FAC-F-123456,factura,INVALIDO
FAC-A-12345,desconocido,INVALIDO
FAC-a-123456,factura,INVALIDO
XXX-1234,desconocido,INVALIDO
RANDOM-CODE,desconocido,INVALIDO
```

---

## Manejo de Errores

El programa detecta e informa automáticamente:

- **Líneas vacías** — Se ignoran sin producir salida
- **Estructura incorrecta** — Se clasifican como `desconocido`
- **Valores inválidos** — Tipo correcto identificado, pero marcado como `INVALIDO`

---

## Características del Código

- Lectura automática línea por línea desde entrada estándar
- Detección automática del tipo de código
- Salida en formato CSV para fácil análisis posterior
- Sin entrada manual del usuario requerida
- Expresiones regulares optimizadas para cada tipo de código

---

**Autor:** Hernandez Rodriguez Manuel

