import sys
import re

def limpiar_valor(valor_str):
    
    valor_limpio = re.sub(r'[^0-9\.\-]', '', valor_str)
    
    if not valor_limpio:
        return 0.0
        
    try:
        
        return float(valor_limpio)
    except ValueError:
        return 0.0

def procesar_linea(linea):
    
    linea = linea.strip()
    if not linea:
        return 0
        

    elementos = linea.split(',')
    total = 0.0
    for elemento in elementos:
        total += limpiar_valor(elemento)
        
    
    return int(total)

def main():
    
    for linea in sys.stdin:
        resultado = procesar_linea(linea)
        print(resultado)

if __name__ == '__main__':
    main()
