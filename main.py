import sys
import random
#coding: UTF8

class Celda:  # creamos el objeto celda
        def __init__(self):
            self.__valor = " "

        def getValor(self):
            return self.__valor

        def setValor(self, valor):
            self.__valor = valor

def menu():

    ''' Te reenvia al menu principal '''

    print("----------------------------------------\n-Práctica de Paradigmas de Programación-\n----------------------------------------")
    print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

    select = int(input("Selecione una opción: "))
    if select == 3:
        sys.exit(0)
    return select



def ImprimirTab(tam,modo,celdas):
    '''Imprime en consola el tablero vacio'''
    for i in range(tam):
        print("+", end="")
        for j in range(tam):
            for k in range(modo):
                print("-", end="")
            print("+", end="")
        print("")
        for l in range(tam):
            print("|", end="")
            for k in range(modo):
                print(celdas[l][i].getValor(), end="")
        print("|")
    print("+", end="")
    for j in range(tam):
        for k in range (modo):
            print("-", end="")
        print("+", end="")


def randInt(max):
    '''Genera un int random generico'''
    rand = int(random.random()*max)
    return rand

def initCelda(tam,obs):
    celdas = [[Celda() for i in range(tam)]for j in range(tam)]

    cont = 0
    for i in range(obs):

        while cont <= i:
            randIntX = randInt(tam)
            randIntY = randInt(tam)


            if celdas[randIntX][randIntY].getValor() == " ":
                celdas[randIntX][randIntY].setValor("*")
                cont += 1

    return celdas







modo = 1
opcion = menu()  # llamo a la función menu porque necesito la variable select
while True:

    if 0 < opcion < 4:

        if opcion == 1:
            modo = 1
            tam = int(input("Tamaño del tablero: "))
            obs = int(input("Número de obstáculos: "))
            celdas = initCelda(tam, obs)

            while True:

                ImprimirTab(tam, modo, celdas)
                print("\n\nMOVIMIENTOS:  | PUNTUACIÓN: ")
                letra = input("[S]ubir, [B]ajar, [I]zda, [D]cha | [M]odo, [G]uardar, [F]in: ")
                if letra=="M":
                    print("\nMODOS DE VISUALIZACION: \n")
                    print("1.Alfabético\n2.Numérico\n3.1024\n4.2048")

                    modo = int(input("Escoja modo: "))

                elif letra == "G":
                    pass
                elif letra == "F":
                    menu()
                    break
                elif letra == "S":
                    pass
                elif letra == "B":
                    pass
                elif letra == "I":
                    pass
                elif letra == "D":
                    pass


        elif opcion == 2:
            fichero = input("Nombre del fichero: ")


    else:
        print("Entrada no válida")












