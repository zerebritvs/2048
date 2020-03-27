import sys
import random
from io import open


# coding: UTF8

class Celda:  # creamos el objeto celda

    def __init__(self):
        '''Inicialiazmos las propiedades del objeto celda'''

        self.__valor = " "
        self.__modo = 1
        self.__modoValor = " "

    def getValor(self):
        '''Obtenemos la propiedad valor del objeto'''

        return self.__valor

    def setMode(self, modo):
        '''Fijamos el modo que esta seleccionado'''

        self.__modo = modo

    def setValor(self, valor):
        '''Fijamos la propiedad'''

        self.__valor = valor

    def getModeValor(self):

        '''Cambiamos el modo que queramos'''

        dic1 = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K"}

        if self.__modo == 1:
            if self.__valor == "*":
                self.__modoValor = "*"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic1[self.__valor]
            return self.__modoValor

        dic2 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}

        if self.__modo == 2:
            if self.__valor == "*":
                self.__modoValor = "*"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic2[self.__valor]
            return self.__modoValor

        dic3 = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024, 11: 2048}

        if self.__modo == 3:
            if self.__valor == "*":
                self.__modoValor = "*"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic3[self.__valor]
            return self.__modoValor

        dic4 = {1: 4, 2: 8, 3: 16, 4: 32, 5: 64, 6: 128, 7: 256, 8: 512, 9: 1024, 10: 2048, 11: 4096}

        if self.__modo == 4:
            if self.__valor == "*":
                self.__modoValor = "*"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic4[self.__valor]
            return self.__modoValor



def menu():
    '''Te reenvia al menu principal'''

    print(
        "----------------------------------------\n-Práctica de Paradigmas de Programación-\n----------------------------------------")
    print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

    select = int(input("\nSelecione una opción: "))
    if select == 3:
        sys.exit(0)
    return select


def ImprimirTab(tam, modo, celdas):
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
                print(celdas[l][i].getModeValor(), end="")
        print("|")
    print("+", end="")
    for j in range(tam):
        for k in range(modo):
            print("-", end="")
        print("+", end="")


def save(tam, celdas):
    '''Guarda el tablero en un archivo .tab'''

    fichero = input("Nombre del fichero: ")
    f = open(fichero, "w")
    f.write(str(move) + "\n" + str(score))

    for i in range(tam):
        f.write("\n")
        for j in range(tam):
            if celdas[j][i].getValor() == " ":
               f.write(".")
            else:
                f.write(str(celdas[j][i].getModeValor()))

    f.close()




def randInt(max):
    '''Genera un int random generico'''
    rand = int(random.random() * max)
    return rand


def initCelda(tam, obs):
    '''Inicializamos las celdas del tablero'''

    celdas = [[Celda() for i in range(tam)] for j in range(tam)]

    cont = 0
    for i in range(obs):  # Creamos los obstaculos

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
                celdas[randInt1][randInt2].setValor(1)
                contNum += 1

    return celdas


def derecha(tam,celdas):
    print("\n---Derecha---")
    for k in range(tam):
        for i in range(tam):
            for j in range(tam-1, 0, -1):
                if celdas[j][i].getValor() == " ":
                    if celdas[j-1][i].getValor() != "*":
                        celdas[j][i].setValor(celdas[j - 1][i].getValor())   #mueve lo que hay en tam-1 a tam
                        celdas[j-1][i].setValor(" ")    #borra el valor anterior
                #elif celdas[j][i].getValor() == "1"
    return celdas

def izquierda(tam,celdas):
    print("\n---Izquierda---")
    for k in range(tam):
        for i in range(tam):
            for j in range(0, tam-1, 1):
                if celdas[j][i].getValor() == " ":
                    if celdas[j + 1][i].getValor() != "*":
                        celdas[j][i].setValor(celdas[j + 1][i].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j + 1][i].setValor(" ")
    return celdas

def subir(tam,celdas):
    print("\n---Subir---")
    for k in range(tam):
        for i in range(0, tam-1, 1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":
                    if celdas[j][i+1].getValor() != "*":
                        celdas[j][i].setValor(celdas[j][i+1].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j][i+1].setValor(" ")
    return celdas


def bajar(tam,celdas):
    print("\n---Bajar---")
    for k in range(tam):
        for i in range(tam-1, 0, -1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":
                    if celdas[j][i-1].getValor() != "*":
                        celdas[j][i].setValor(celdas[j][i-1].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j][i-1].setValor(" ")
    return celdas



modo = 1
opcion = menu()  # llamo a la función menu porque necesito la variable select
while True:

    if opcion == 1:
        modo = 1
        tam = int(input("Tamaño del tablero: "))
        obs = int(input("Número de obstáculos: "))
        celdas = initCelda(tam, obs)
        move = 0
        score = 0

        while True:

            ImprimirTab(tam, modo, celdas)

            print("\n\nMOVIMIENTOS:", move,  "| PUNTUACIÓN:", score)
            letra = input("[S]ubir, [B]ajar, [I]zda, [D]cha | [M]odo, [G]uardar, [F]in: ")
            if letra == "M":
                print("\nMODOS DE VISUALIZACIÓN: \n")
                print("1.Alfabético\n2.Numérico\n3.1024\n4.2048")

                modo = int(input("\nEscoja modo: "))

                for i in range(tam):
                    for j in range(tam):
                        celdas[j][i].setMode(modo) #actualiza el modo de todas las celdas

            elif letra == "G":  # guarda la partida
                save(tam, celdas)
                menu()
                break
            elif letra == "F":  # vuelve al menu del juego
                menu()
                break
            elif letra == "S":  # mueve hacia arriba
                move += 1
                celdas = subir(tam, celdas)

            elif letra == "B":  # mueve hacia abajo
                move += 1
                celdas = bajar(tam, celdas)

            elif letra == "I":  # mueve hacia la izquierda
                move += 1
                celdas = izquierda(tam, celdas)

            elif letra == "D":  # mueve hacia la derecha
                move += 1
                celdas = derecha(tam, celdas)



    elif opcion == 2:  # carga una partida guardada
        fichero = input("Nombre del fichero: ")
        f = open(fichero, "r")
        partida = f.read()
        print(partida)
        f.close()
        break


