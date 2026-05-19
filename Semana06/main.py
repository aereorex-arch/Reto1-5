import sys
import re

# Constantes de validación
DEPARTAMENTOS_VALIDOS = {'VEN', 'ADM', 'TEC', 'LOG', 'RHH'}
SERIES_VALIDAS = {'A', 'B', 'C', 'D', 'E'}

# Patrones regex consolidados
PATRONES = {
    'producto': {
        'deteccion': re.compile(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$'),
        'validacion': re.compile(r'^([A-Z]{3})-(\d{4})-([A-Z]{2})$'),
    },
    'envio': {
        'deteccion': re.compile(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$'),
        'validacion': re.compile(r'^ENV-(\d{4})-(\d{2})-(\d{2})-(\d{6})$'),
    },
    'empleado': {
        'deteccion': re.compile(r'^EMP-[A-Za-z]{3}-\d{4}$'),
        'validacion': re.compile(r'^EMP-([A-Z]{3})-(\d{4})$'),
    },
    'factura': {
        'deteccion': re.compile(r'^FAC-[A-Za-z]-\d{6}$'),
        'validacion': re.compile(r'^FAC-([A-Z])-(\d{6})$'),
    },
}


def detectar_tipo(codigo: str) -> str:
    """Detecta el tipo de código basado en su estructura."""
    # Detectar ENV, EMP, FAC primero (más específicos)
    for tipo in ['envio', 'empleado', 'factura', 'producto']:
        if PATRONES[tipo]['deteccion'].match(codigo):
            return tipo
    return 'desconocido'


def validar_producto(match) -> bool:
    """Valida que categoría y país estén en mayúsculas."""
    return match is not None


def validar_envio(match) -> bool:
    """Valida rango de año, mes y día."""
    if not match:
        return False
    
    anio, mes, dia = int(match.group(1)), int(match.group(2)), int(match.group(3))
    return 2020 <= anio <= 2030 and 1 <= mes <= 12 and 1 <= dia <= 31


def validar_empleado(match) -> bool:
    """Valida departamento válido y número sin cero inicial."""
    if not match:
        return False
    
    departamento, numero = match.group(1), match.group(2)
    return departamento in DEPARTAMENTOS_VALIDOS and numero[0] != '0'


def validar_factura(match) -> bool:
    """Valida que la serie esté en el conjunto válido."""
    if not match:
        return False
    
    serie = match.group(1)
    return serie in SERIES_VALIDAS


# Mapeo de funciones de validación por tipo
VALIDADORES = {
    'producto': validar_producto,
    'envio': validar_envio,
    'empleado': validar_empleado,
    'factura': validar_factura,
    'desconocido': lambda m: False,
}


def validar_codigo(codigo: str) -> tuple:
    """Detecta tipo y valida el código."""
    tipo = detectar_tipo(codigo)
    
    if tipo == 'desconocido':
        return tipo, False
    
    match = PATRONES[tipo]['validacion'].match(codigo)
    es_valido = VALIDADORES[tipo](match)
    
    return tipo, es_valido


def main():
    """Lee códigos de entrada estándar y escribe validación en CSV."""
    print("codigo,tipo,valido")
    
    for linea in sys.stdin:
        codigo = linea.strip()
        
        if not codigo:
            continue
        
        tipo, es_valido = validar_codigo(codigo)
        estado = 'VALIDO' if es_valido else 'INVALIDO'
        
        print(f"{codigo},{tipo},{estado}")


if __name__ == "__main__":
    main()
