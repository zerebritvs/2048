import sys
import math

print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

teclado=int(input("\nIndique la opción: "))


if 0<teclado<4:

    if teclado==1:
        tam = int(input("Tamaño de tablero: "))
        obs = int(input("Número de obstáculos: "))

    elif teclado==2:
        print("")

    else:
        sys.exit(0)


#def tablero(tam)
    #for i in







