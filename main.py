import sys
import random
from io import open


# coding: UTF8

class Celda:                                                # creamos el objeto celda

    '''Inicialiazmos las propiedades del objeto celda'''

    def __init__(self):

        self.__valor = " "
        self.__modo = 1
        self.__modoValor = " "

    '''Obtenemos la propiedad valor del objeto'''

    def getValor(self):

        return self.__valor

    '''Fijamos el modo que esta seleccionado'''

    def setMode(self, modo):

        self.__modo = modo

    '''Fijamos la propiedad'''

    def setValor(self, valor):

        self.__valor = valor

    '''Cambiamos el modo que queramos'''

    def getModeValor(self):

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
                self.__modoValor = "**"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic2[self.__valor]
            return self.__modoValor

        dic3 = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256, 10: 512, 11: 1024}

        if self.__modo == 3:
            if self.__valor == "*":
                self.__modoValor = "****"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic3[self.__valor]
            return self.__modoValor

        dic4 = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024, 11: 2048}

        if self.__modo == 4:
            if self.__valor == "*":
                self.__modoValor = "****"
            elif self.__valor == " ":
                self.__modoValor = " "
            else:
                self.__modoValor = dic4[self.__valor]
            return self.__modoValor


'''Te reenvia al menu principal'''


def menu():
    print("--------------------  CLON-3  --------------------\n- Práctica de Paradigmas de Programación 2019-20 ",
          end="")
    print("-\n--------------------------------------------------")
    print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

    select = int(input("\nSelecione una opción: "))
    if select == 3:                                 # si el usuario selecciona 3
        sys.exit(0)                                 # finaliza el programa

    return select


'''Imprime en consola el tablero vacio'''


def imprimirTab(tam, modo, celdas):
    if modo == 3:                       # para conseguir imprimir los 4 huecos vacios
        modo = 4

    for i in range(tam):
        print("+", end="")
        for j in range(tam):
            for k in range(modo):
                print("-", end="")
            print("+", end="")
        print("")
        for l in range(tam):
            print("|", end="")
            for k in range(modo - len(str(celdas[l][i].getModeValor()))):
                print(" ", end="")
            print(celdas[l][i].getModeValor(), end="")
        print("|")
    print("+", end="")
    for j in range(tam):
        for k in range(modo):
            print("-", end="")
        print("+", end="")


'''Guarda el tablero en un archivo .tab'''


def save(tam, celdas):
    fichero = input("Nombre del fichero: ")
    f = open(fichero, "w")                                  # crea y abre el archivo en modo escritura
    f.write(str(moves) + "\n" + str(score))                 # copia los movimientos y la puntuación

    for i in range(tam):                                    # recorre las celdas en eje y
        f.write("\n")
        for j in range(tam):                                # recorre las celdas en eje x
            celdas[j][i].setMode(1)                         # cambia el modo al 1(Alfabético)
            if celdas[j][i].getValor() == " ":
                f.write(".")                                # transforma los espacios en puntos
            else:
                f.write(str(celdas[j][i].getModeValor()))   # Escribe el caracter que haya en cada celda

    f.close()  # Cierra el flujo de datos


'''Carga el tablero de un archivo .tab'''


def load():
    fichero = input("Nombre del fichero: ")
    f = open(fichero, "r")

    moves = f.read(0)
    # print(move)
    f.seek(1)
    score = f.read(1)
    # print(score)
    f.seek(2)

    # for i in range(tam):
    #     for j in range(tam):
    #           if f.read() == ".":
    #             celdas[j][i].setValor(" ")
    #           else:
    #              f.read() = celdas[j][i].setValor()

    f.close()


'''Añade un bloque nuevo de distinto nivel(1 o 2) cada vez que hay movimiento'''


def addCelda(tam, celdas):

    prob = random.choices([1, 2], [0.75, 0.25])             # Probabilidad del 75% de nivel 1 y 25% de nivel 2

    while True:
        randIntX = randInt(tam)                             # Genera una coordenada x random
        randIntY = randInt(tam)                             # Genera una coordenada y random

        if celdas[randIntX][randIntY].getValor() == " ":    # Genera la celda donde haya un hueco libre
            celdas[randIntX][randIntY].setValor(prob[0])
            break

    return celdas


'''Genera un int random generico'''


def randInt(max):

    rand = int(random.random() * max)
    return rand


'''Comprueba si la partida a finalizado'''


def fin(tam, celdas):
    maximo = tam * tam                          # Numero maximo de celdas
    contmax = 0

    for i in range(tam):
        for j in range(tam):
            if celdas[j][i].getValor() != " ":  # Comprueba si todas las celdas están llenas
                contmax += 1

    if contmax == maximo:                       # Si las celdas estan llenas la partida finaliza
        imprimirTab(tam, modo, celdas)          # Imprime el tablero lleno
        print("\n\n---  FIN DEL JUEGO ---\n")
        menu()                                  # Vuelve al menu principal


'''Inicializamos las celdas del tablero'''


def initCelda(tam, obs):
    celdas = [[Celda() for i in range(tam)] for j in range(tam)]    # Crea la lista celdas

    cont = 0
    for i in range(obs):                                            # Creamos los obstaculos

        while cont <= i:
            randIntX = randInt(tam)
            randIntY = randInt(tam)

            if celdas[randIntX][randIntY].getValor() == " ":
                celdas[randIntX][randIntY].setValor("*")
                cont += 1

    contNum = 0
    for i in range(2):
        addCelda(tam, celdas)

    return celdas


'''Mueve hacia la derecha'''


def derecha(tam, celdas, score):
    print("\n--- Derecha ---")
    for k in range(tam):
        for i in range(tam):
            for j in range(tam - 1, 0, -1):
                if celdas[j][i].getValor() == " ":
                    if celdas[j - 1][i].getValor() != "*":
                        celdas[j][i].setValor(celdas[j - 1][i].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j - 1][i].setValor(" ")                      # borra el valor anterior
                elif celdas[j][i].getValor() == celdas[j - 1][i].getValor() and celdas[j][i].getValor() != "*":
                    celdas[j][i].setValor(celdas[j][i].getValor() + 1)
                    celdas[j - 1][i].setValor(" ")
                    score += 1
    return celdas, score


'''Mueve a la izquierda'''


def izquierda(tam, celdas, score):
    print("\n--- Izquierda ---")
    for k in range(tam):
        for i in range(tam):
            for j in range(0, tam - 1, 1):
                if celdas[j][i].getValor() == " ":
                    if celdas[j + 1][i].getValor() != "*":
                        celdas[j][i].setValor(celdas[j + 1][i].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j + 1][i].setValor(" ")
                elif celdas[j][i].getValor() == celdas[j + 1][i].getValor() and celdas[j][i].getValor() != "*":
                    celdas[j][i].setValor(celdas[j][i].getValor() + 1)
                    celdas[j + 1][i].setValor(" ")
                    score += 1
    return celdas, score


'''Mueve hacia arriba'''


def subir(tam, celdas, score):
    print("\n--- Subir ---")
    for k in range(tam):
        for i in range(0, tam - 1, 1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":
                    if celdas[j][i + 1].getValor() != "*":
                        celdas[j][i].setValor(celdas[j][i + 1].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j][i + 1].setValor(" ")
                elif celdas[j][i].getValor() == celdas[j][i + 1].getValor() and celdas[j][i].getValor() != "*":
                    celdas[j][i].setValor(celdas[j][i].getValor() + 1)
                    celdas[j][i + 1].setValor(" ")
                    score += 1
    return celdas, score


'''Mueve hacia abajo'''


def bajar(tam, celdas, score):
    print("\n--- Bajar ---")
    for k in range(tam):
        for i in range(tam - 1, 0, -1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":
                    if celdas[j][i - 1].getValor() != "*":
                        celdas[j][i].setValor(celdas[j][i - 1].getValor())  # mueve lo que hay en tam-1 a tam
                        celdas[j][i - 1].setValor(" ")
                elif celdas[j][i].getValor() == celdas[j][i - 1].getValor() and celdas[j][i].getValor() != "*":
                    celdas[j][i].setValor(celdas[j][i].getValor() + 1)
                    celdas[j][i - 1].setValor(" ")
                    score += 1
    return celdas, score


modo = 1
opcion = menu()                                                 # Llamo a la función menu porque necesito la variable select

while True:                                                     # Bucle principal del juego

    if opcion == 1:                                             # Si selecciona opcion 1
        modo = 1
        tam = int(input("Tamaño del tablero: "))                # Pide dimensiones del tablero
        obs = int(input("Número de obstáculos: "))              # Pide el numero de obstaculos
        celdas = initCelda(tam, obs)                            # Inicializa el tablero
        moves = 0                                               # Inicializa el movimientos
        score = 0                                               # Inicializa la puntacion

        while True:                                             # Acaba cuando el usuario pulsa [F]in o [G]uardar

            fin(tam, celdas)                                    # Comprueba la partida ha finalizado
            imprimirTab(tam, modo, celdas)                      # Imprime el tablero

            print("\n\nMOVIMIENTOS:", moves, "| PUNTUACIÓN:", score)
            letra = input("[S]ubir, [B]ajar, [I]zda, [D]cha | [M]odo, [G]uardar, [F]in: ")
            if letra == "M":
                print("\nMODOS DE VISUALIZACIÓN: \n")
                print("1.Alfabético\n2.Numérico\n3.1024\n4.2048")

                modo = int(input("\nEscoja modo: "))

                for i in range(tam):
                    for j in range(tam):
                        celdas[j][i].setMode(modo)              # Actualiza el modo de todas las celdas

            elif letra == "G":                                  # Guarda la partida
                save(tam, celdas)                               # Genera un fichero .tab con la partida guardada
                menu()                                          # Vuelve al menu principal del juego
                break
            elif letra == "F":                                  # Vuelve al menu del principal del juego
                menu()
                break
            elif letra == "S":                                  # Mueve hacia arriba
                moves += 1                                      # Suma 1 a los movimientos
                celdas, score = subir(tam, celdas, score)       # Actualiza el tablero
                addCelda(tam, celdas)                           # Añade una celda random

            elif letra == "B":                                  # Mueve hacia abajo
                moves += 1                                      # Suma 1 a los movimientos
                celdas, score = bajar(tam, celdas, score)       # Actualiza el tablero
                addCelda(tam, celdas)                           # Añade una celda random

            elif letra == "I":                                  # Mueve hacia la izquierda
                moves += 1                                      # Suma 1 a los movimientos
                celdas, score = izquierda(tam, celdas, score)   # Actualiza el tablero
                addCelda(tam, celdas)                           # Añade una celda random

            elif letra == "D":                                  # Mueve hacia la derecha
                moves += 1                                      # Suma 1 a los movimientos
                celdas, score = derecha(tam, celdas, score)     # Actualiza el tablero
                addCelda(tam, celdas)                           # Añade una celda random

    elif opcion == 2:                                           # Carga una partida guardada
        load()
