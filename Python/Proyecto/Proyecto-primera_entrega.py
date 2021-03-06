# 
# Proyecto-primera_entrega.py
#
# Descripcion: Este es un juego llamado "Connect the dots" en el que dos
# jugadores, bien sea persona vs maquina o persona vs persona, tratan de
# completar la mayor cantidad de cuadros en un tablero de dimensiones
# elegidas por el usuario.
#
# Autores:
# Roberto Camara Carnet:11-10235 Grupo: 46
# Douglas Torres Carnet:11-11027 Grupo:28
#
# Ultima modificacion: ??/06/2014
#


# Importacion de la libreria que permite escoger una posicion a marcar
# al azar a la computadora

#from random import *

# Definicio de funciones

################################################################################
######################## F U N C I O N E S #####################################
################################################################################

# Definicion de funcion que inicializa los datos del programa
#------------------------------------------------------------------------------#

def Inicializacion(filas: int, columnas: int) -> (list,list,list):
#Precondicion: filas>=2 and columnas>=2
#Postcondicion: len(tableroHorizontal)==filas*(columnas-1) and len(tableroVertical)==(filas-1)*columnas and len(tableroCuadrados)==(filas-1)*(columnas-1)

    tableroCuadros = []
    tableroHorizontal = []
    tableroVertical = []
    for i in range(filas):
        tableroHorizontal.append([])
        for j in range(columnas-1):
            tableroHorizontal[i].append("0")

    for i in range(filas-1):
        tableroVertical.append([])
        for j in range(columnas):
            tableroVertical[i].append("0")

    for i in range(filas-1):
        tableroCuadros.append([])
        for j in range(columnas-1):
            tableroCuadros[i].append("0")


    return tableroHorizontal,tableroVertical,tableroCuadros

# Definicion de funcion que imprime el tablero cada vez que se modifica
#------------------------------------------------------------------------------#

def ImprimirTablero(tablero: list) -> (list):
#Precondicion: 
#Postcondicion: 
                    
    for i in tablero:
        print(" ".join(i))
	

# Definicion de funcion que permite al jugador 1 hacer su jugada
#------------------------------------------------------------------------------#

def Jugador1(TH: list,TV: list,TC: list,filas: int,columnas: int) -> (list,list,list):
    
    # Aqui se usa un while para definir el turno de cada jugador
    
    turno = True
    
    while turno:

        print ("Turno jugador 1")

        opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))

        if (opcion == 1):
            TH = MarcarLineaHorizontal(TH)
            
        elif (opcion == 2):
            TV = MarcarLineaVertical(TV)
            
        else:
            quit()
            
        TC,turno = HacerCuadrados(TH,TV,TC,filas,columnas,1,turno)
        
        return TH,TV,TC
        

# Definicion de funcion que permite al jugador 2 hacer su jugada
#------------------------------------------------------------------------------#

def Jugador2(TH: list,TV: list,TC: list,filas: int,columnas: int,TJ: int):
# Precondicion: TJ==1 or TJ==2
# Postcondicion:

    # Aqui se usa un while para definir el turno de cada jugador

    turno = True

    while turno:

        if (TJ == 1):

            print("Es humano","\n")

            print("Turno jugador 2\n")

            opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))

            if (opcion == 1):
                TH = MarcarLineaHorizontal(TH)
            
            elif (opcion == 2):
                TV = MarcarLineaVertical(TV)
                
            else:
                quit()
            
            TC,turno = HacerCuadrados(TH,TV,TC,filas,columnas,2,turno)
                    
        else:

            print("Es computadora","\n")

            print("Turno jugador 2\n")

            if (all (TH[i][j] == 1 and TV[i][j] == 1 and TH[i+1][j] == 1 \
                         for i in range (filas-2) for j in range (columnas-2))):

                TV[i][j+1] = "1"
                
            
            elif(all ((TH[i][j] == 1) and (TV[i][j] == 1) and (TV[i][j+1] == 1) \
                          for i in range (filas-2) for j in range (columnas-2))):
                
                TH[i+1][j] = "1"

            
            elif(all ((TH[i][j] == 1) and (TH[i+1][j] == 1) and (TV[i][j+1] == 1) \
                          for i in range (filas-2) for j in range (columnas-2))):
                
                TV[i][j] = "1"
            
            elif(all ((TV[i][j] == 1) and (TH[i+1][j] == 1) and (TV[i][j+1] == 1) \
                     for i in range (filas-2) for j in range (columnas-2))):
                
                TH[i][j] = "1"
           
            else:
                
                opcion = randint(1,2)

                if (opcion == 1):
                    i,j = randint(0,filas-2),randint(0,columnas-2)
                    TH[i][j] = "1"
            
                elif (opcion == 2):
                    i,j = randint(0,filas-2),randint(0,columnas-2)
                    TV[i][j] = "1"
                
                else:
                    quit()
            
            TC,turno = HacerCuadrados(TH,TV,TC,filas,columnas,2,turno)
                    
        return TH,TV,TC


# Definicion de funcion que imprime las instrucciones
#------------------------------------------------------------------------------#
        
def Instruccion () -> (str):
# Precondicion:
# Postcondicion:x

    print("\n")
    print ("Cada jugador en su turno debe seleccionar entre dos puntos, \
horizontales o verticales, para trazar una raya \n")

    print ("El objetivo del juego es completar la mayor cantidad de cuadrados \n")

    print ("Al marcar una raya en el tablero ocurre un cambio de turno a menos \
que el jugador complete un cuadrado con dicha raya, caso en el que puede volver a jugar \n")

    print ("Al final del juego gana el jugador con mayor cantidad de cuadros marcados \n")


# Definicion de funcion que marca una linea horizontal en el tablero
#------------------------------------------------------------------------------#

def MarcarLineaHorizontal(TH: list) -> (list):
#Precondicion:
#Postcondicion:
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TH[lineafila][lineacolumna] = "1"

    return TH


# Definicion de funcion que marca una linea vertical en el tablero
#------------------------------------------------------------------------------#

def MarcarLineaVertical(TV: list) -> (list):
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TV[lineafila][lineacolumna] = "1"

    return TV


# Definicion de funcion que marca un cuadrado en el tablero y dice de que jugador fue  
#------------------------------------------------------------------------------#

def HacerCuadrados(TH: list, TV: list,TC: list,filas: int,columnas: int,jugador: int,turno: bool) -> (list,bool):

#Precondicion:
#Postcondicion:

    for i in range (filas-2):

        for j in range (columnas-2):

           if ((TH[i][j] == "1") and (TV[i][j] == "1") and (TH[i+1][j] == "1") and (TV[i][j+1] == "1")):

                if (jugador == 1):
                    (TC[i][j]) = "1"
                    turno = True

                else:
                    (TC[i][j]) = "2"
                    turno = True

           else:
               turno = False
    
    return TC,turno


# Definicion de funcion que permite cargar una partida especificada por el usuario
#------------------------------------------------------------------------------#

def CargarPartida(archivo) -> (str):
# Precondicion:
# Postcondicion:

    print("Cargar partida")

# Definicion de funcion que guarda una partida
#------------------------------------------------------------------------------#

def GuardarPartida(archivo) -> (str):
# Precondicion:
# Postcondicion:

    print("Guardar partida")


# Definicion de funcion que imprime el puntaje al momento de la partida
#------------------------------------------------------------------------------#

def Puntaje(TC: list) -> (int,int):
# Precondicion:
# Postcondicion: PuntosJugador1 >= 0 and PuntosJugador2 >= 0

    PuntosJugador1 = 0
    PuntosJugador2 = 0

    for i in range(filas-2):
        for j in range(columnas-2):
            if (TC[i][j] == "1"):
                PuntosJugador1 = PuntosJugador1 + 1
            elif (TC[i][j] == "2"):
                PuntosJugador2 = PuntosJugador2 + 1
            else:
                pass

    return PuntosJugador1,PuntosJugador2


# Definicion de funcion que imprime el puntaje final de la partida
#------------------------------------------------------------------------------#

def PuntajeFinal(PuntosJugador1: int,PuntosJugador2: int) -> (str):
# Precondicion:
# Postcondicion:

    if (PuntosJugador1 > PuntosJugador2):
        print ("Ha ganado el jugador 1")
    elif (PuntosJugador1 < PuntosJugador2):
        print("Ha ganado el jugador 2")
    else:
        print("Ha habido un empate")




# Definicion de funcion que especifica el turno de juego
#------------------------------------------------------------------------------#

def Turno (TJ: list,TH: list,TV: list,TC: list,filas: int,columnas: int,azar: int) -> (list,list):
# Precondicion:
# Postcondicion:
    if (TJ == 1):
        PrimerTurno = Jugador1(TH,TV,TC,filas,columnas)
        SegundoTurno = Jugador2(TH,TV,TC,filas,columnas,TJ)
    elif (TJ == 2):
        PrimerTurno = azar
        SegundoTurno = azar



# Definicion de funcion que imprime el menu del juego y permite escoger el tipo de juego
#------------------------------------------------------------------------------#

def ModoJuego()-> (int,bool):
# Precondicion: True
# Postcondicion: 

    print ("\n\n\tBienvenido a Connect the dots!\n")
    print ("Aqui se le presentan las siguientes opciones: \n")
    print ("1) - Partida de 1 jugador")
    print ("2) - Partida de 2 jugadores")
    print ("3) - Cargar partida")
    print ("4) - Instrucciones")
    print ("5) - Salir \n")
    
    seleccion = int(input("Introduzca una opcion y presione enter: "))

    if (seleccion == 1):

        # Aqui va la inicializacion de datos realizando la llamada a la funcion
        
        filas = int(input('Escribe el numero de filas del tablero: '))
        columnas = int(input('Escribe el nuemro de columnas del tablero: '))
        
        TH,TV,TC = Inicializacion(filas,columnas)
        TJ = 1

        return TH,TV,TC,TJ,filas,columnas

    elif (seleccion == 2):

        # Aqui va la inicializacion de datos realizando la llamada a la funcion
        # Adicionalmente se dice el tipo de jugador que es el jugador 2

        filas = int(input('Escribe el numero de filas del tablero: '))
        columnas = int(input('Escribe el nuemro de columnas del tablero: '))
        
        TH,TV,TC = Inicializacion(filas,columnas)
        TJ = 2
                
        return TH,TV,TC,TJ,filas,columnas

    elif (seleccion == 3):

        # Aqui el programa carga la partida de un archivo
        
        CargarPartida()
        
        # Luego usa los datos del archivo seleccionado y los usa en inicializacion
        # Hay que colocar a inicializacion como una funcion que recibe datos concretos
        # Porque no hay otra forma practica que realice la inicializacion en este caso
        
        # filas = int(input('Escribe el numero de filas del tablero: '))
        # columnas = int(input('Escribe el nuemro de columnas del tablero: '))
        
        Inicializacion()

    elif (seleccion == 4):

        # Aqui se imprimen las instrucciones del juego al llamarse a la funcion instruccion

        Instruccion()
    
    elif (seleccion == 5):
        quit()


####################### PROGRAMA PRINCIPAL #####################################

TH,TV,TC,TJ,filas,columnas = ModoJuego()

"""azar = [1,2]

shuffle(azar)
PrimerTurno = azar.pop()
SegundoTurno = azar.pop()

"""

for i in range((filas)*(columnas)):

    print("***HORIZONTAL***")
    print()
    ImprimirTablero(TH)
    print()
    print("***VERTICAL***")
    print()
    ImprimirTablero(TV)
    print()
    print("***Cuadros***")
    print()
    ImprimirTablero(TC)
    print()
    
    



"""    opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))
    if (opcion == 1):
        TH = MarcarLineaHorizontal(TH)
        
    elif (opcion == 2):
        TV = MarcarLineaVertical(TV)
    
    else:
        quit()

    TC = HacerCuadrados(TH,TV,TC,filas,columnas,jugador)
		
    print()
    print("--------------------")
"""
	
print("***CUADROS***")

ImprimirTablero(TC)


""" Vainas a discutir """

# Discutir randint dentro de marcar linea horizontal y vertical

# Discutir modo de los turnos

# Discutir formato general del programa

# Faltan por crear las estructuras de datos de los jugadores (Necesarias para la funcion de guardar y cargar)

# Crear funcion de finalizar juego
