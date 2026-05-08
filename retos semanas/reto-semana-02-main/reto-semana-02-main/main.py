import sys


def fahrenheit_a_celsius(f):
   
    return (f - 32) * 5 / 9


def clasificar(celsius):
   
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"


def main():
    
    lineas = sys.stdin.readlines()

    
    print("ciudad,temperatura_celsius,clasificacion")

    
    for linea in lineas[1:]:
        linea = linea.strip()

      
        if not linea:
            continue

        partes = [p.strip() for p in linea.split(",")]

       
        if len(partes) != 3:
            continue

        ciudad, temperatura_str, unidad = partes

      
        try:
            temperatura = float(temperatura_str)
        except ValueError:
            continue

       
        unidad = unidad.upper()
        if unidad not in ("C", "F"):
            continue

      
        if unidad == "F":
            celsius = fahrenheit_a_celsius(temperatura)
        else:
            celsius = temperatura

       
        clasificacion = clasificar(celsius)
        print(f"{ciudad},{celsius:.1f},{clasificacion}")


if __name__ == "__main__":
    main()
