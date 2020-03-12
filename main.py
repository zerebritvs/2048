import sys
import random
#coding: UTF8

class Celda:  # creamos el objeto celda

        def __init__(self):

            '''Inicialiazmos las propiedades del objeto celda'''

            self.__valor = " "

        def getValor(self):

            '''Obtenemos la propiedad valor del objeto'''

            return self.__valor


        def setValor(self, valor):

            '''Fijamos la propiedad'''

            self.__valor = valor

def menu():

    '''Te reenvia al menu principal'''

    print("----------------------------------------\n-Práctica de Paradigmas de Programación-\n----------------------------------------")
    print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

    select = int(input("\nSelecione una opción: "))
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

    '''Inicializamos las celdas del tablero'''

    celdas = [[Celda() for i in range(tam)]for j in range(tam)]

    cont = 0
    for i in range(obs): #Creamos los obstaculos

        while cont <= i:
            randIntX = randInt(tam)
            randIntY = randInt(tam)


            if celdas[randIntX][randIntY].getValor() == " ":

                celdas[randIntX][randIntY].setValor("*")
                cont += 1

    contNum = 0
    for i in range(2):

        while contNum <= i:
            randInt1 = randInt(tam)
            randInt2 = randInt(tam)


            if celdas[randInt1][randInt2].getValor() == " ":
                celdas[randInt1][randInt2].setValor("1")
                contNum += 1

    return celdas


def derecha(tam):
    print("\n---Derecha---")

    long = tam

    for i in range(tam):
        if celdas[tam][i+1].getValor() != " ":
            celdas[tam+1][i]







modo = 1
opcion = menu()  #llamo a la función menu porque necesito la variable select
while True:

    if opcion == 1:
        modo = 1
        tam = int(input("Tamaño del tablero: "))
        obs = int(input("Número de obstáculos: "))
        celdas = initCelda(tam, obs)

        while True:

            ImprimirTab(tam, modo, celdas)
            print("\n\nMOVIMIENTOS:  | PUNTUACIÓN: ")
            letra = input("[S]ubir, [B]ajar, [I]zda, [D]cha | [M]odo, [G]uardar, [F]in: ")
            if letra == "M":
                print("\nMODOS DE VISUALIZACION: \n")
                print("1.Alfabético\n2.Numérico\n3.1024\n4.2048")

                modo = int(input("\nEscoja modo: "))
                if modo == 3:
                    modo = 4

            elif letra == "G":  # guarda la partida
                pass
            elif letra == "F":  # vuelve al menu del juego
                menu()
                break
            elif letra == "S":  # mueve hacia arriba
                pass
            elif letra == "B":  # mueve hacia abajo
                pass
            elif letra == "I":  # mueve hacia la izquierda
                pass
            elif letra == "D":  # mueve hacia la derecha
                derecha(tam)


    elif opcion == 2:  # carga una partida guardada
        fichero = input("Nombre del fichero: ")
        break















