# 
# Proyecto-primera_entrega.py
#
# Descripcion: Este es un juego llamado "Connect TableroHorizontale dots" en el que dos
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

######TKINTER#####
from tkinter import *
from tkinter import ttk


# Importacion de la libreria que permite escoger una posicion a marcar
# al azar a la computadora

from random import *

# Definicion de Clase

class Jugadores:
    NombreJugador1 = ""
    NombreJugador2 = ""

grupo = Jugadores()

# Definicio de funciones

################################################################################
######################## F U N C I O N E S #####################################
################################################################################

# Definicion de funcion que inicializa los datos del programa
#------------------------------------------------------------------------------#

def Inicializacion (filas: int, columnas: int) -> (list,list,list):

# Precondicion: filas>=2 and columnas>=2

# Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and\
# len(TableroVertical)==(filas-1)*columnas and\
# len(TableroCuadros)==(filas-1)*(columnas-1) and\
# all((TableroHorizontal[i][j] == "0") for i in range(filas)\ 
# for j in range(columnas-1))and\ ((TableroVertical[i][j] == "0")\
# for i in range(filas-1) for j in range(columnas) and\
# ((TableroCuadros[i][j] == "0") for i in range(filas-1)\
# for j in range(columnas-1)))

    TableroCuadros = []
    TableroHorizontal = []
    TableroVertical = []

    for i in range(filas):
        TableroHorizontal.append([])
        for j in range(columnas-1):
            TableroHorizontal[i].append("0")

    for i in range(filas-1):
        TableroVertical.append([])
        for j in range(columnas):
            TableroVertical[i].append("0")

    for i in range(filas-1):
        TableroCuadros.append([])
        for j in range(columnas-1):
            TableroCuadros[i].append("0")


    return TableroHorizontal,TableroVertical,TableroCuadros

# Definicion de funcion que imprime el tablero cada vez que se modifica
#------------------------------------------------------------------------------#

def ImprimirTablero(TableroHorizontal: list, TableroVertical: list,\
 TableroCuadros:list) -> (list,list,list):

# Precondicion: len(TableroHorizontal) >=2 and len(TableroVertical) >=2 and\
# len(TableroCuadros) >=2

# Postcondicion: True // Esta funcion no modifica ninguna variable que recibe,\
# solo imprime los tableros en un formato mas amigable para el usuario

    print("***HORIZONTAL***")
    print()

    for i in TableroHorizontal:
        print(" ".join(i))

    print("***VERTICAL***")
    print()

    for i in TableroVertical:
        print(" ".join(i))

    print("***CUADROS***")
    print()

    for i in TableroCuadros:
        print(" ".join(i))


# Definicion de funcion que permite al jugador 1 hacer su jugada
#------------------------------------------------------------------------------#

def Jugador1(TableroHorizontal: list,TableroVertical: list,TableroCuadros: list,\
filas: int,columnas: int,TurnoActual: int) -> (list,list,list,int):

# Precondicion: len(TableroHorizontal)==filas*(columnas-1) and\
# len(TableroVertical)==(filas-1)*columnas and\
# len(TableroCuadros)==(filas-1)*(columnas-1) and\
# filas>=2 and columnas>=2 and (TurnoActual==2)

# Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and \
# len(TableroVertical)==(filas-1)*columnas and\
# len(TableroCuadros)==(filas-1)*(columnas-1)"""

    turno = True  # Variable que se usa para especificar si un jugador\
                  # puede seguir jugando

    opcion = 0    # Variable que especifica el tipo de raya que desea marcar\
                  # el usuario

    TurnoActual = 1    # Variable que especifica el turno de quien juega

    while (turno):

        print ("Turno jugador 1")

        opcion = int(input("Presione 1 para horizontal, 2 para vertical,\
 3 para guardar o cualquier otra tecla para salir: "))

        if (opcion == 1):
            TableroHorizontal = MarcarLineaHorizontal(TableroHorizontal)

        elif (opcion == 2):
            TableroVertical = MarcarLineaVertical(TableroVertical)

        elif (opcion == 3):
            GuardarPartida("archivo.txt")
            break
        
        else:
            quit()

        TableroCuadros,turno = HacerCuadros(TableroHorizontal,TableroVertical,\
                                                TableroCuadros,filas,columnas,1,\
                                                turno)

#print(turno)

        ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)

    return TableroHorizontal,TableroVertical,TableroCuadros,TurnoActual


# Definicion de funcion que permite al jugador 2 hacer su jugada
#------------------------------------------------------------------------------#

def Jugador2(TableroHorizontal: list,TableroVertical: list,TableroCuadros: list,\
filas: int,columnas: int,TipoJugador: int,TurnoActual: int) -> (list,list,\
list,int):

# Precondicion: (TipoJugador==1 or TipoJugador==2) and\
# len(TableroHorizontal)==filas*(columnas-1) and \
# len(TableroVertical)==(filas-1)*columnas and\
# len(TableroCuadros)==(filas-1)*(columnas-1) and \
# filas>=2 and columnas>=2 and TurnoActual==1

# Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and\
# len(TableroVertical)==(filas-1)*columnas and \
# len(TableroCuadros)==(filas-1)*(columnas-1)

# Aqui se usa un while para definir el turno de cada jugador

    turno = True    # Variable que se usa para espeecificar si un jugador puede\
                    # seguir jugando

    TurnoActual = 2    # Variable que especifica el turno del jugador que esta\
                       # jugando
    
    opcion = 0    # Variable que especifica el tipo de raya que desea marcar el\
                  # usuario
    
    N = filas-1
    
    M = columnas-1

    while (turno):

        if (TipoJugador == 2):

            print("Es humano","\n")

            print("Turno jugador 2\n")

            opcion = int(input("Presione 1 para horizontal, 2 para vertical,\
 3 para guardar o cualquier otra tecla para salir: "))

            if (opcion == 1):
                TableroHorizontal = MarcarLineaHorizontal(TableroHorizontal)

            elif (opcion == 2):
                TableroVertical = MarcarLineaVertical(TableroVertical)

            elif (opcion == 3):
                GuardarPartida("archivo.txt")
                break
           
            else:
                quit()

            TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                    TableroVertical,\
                                                    TableroCuadros,filas,\
                                                    columnas,2,turno)

            print (turno)

            ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)

        else:

            print("Es computadora","\n")

            print("Turno jugador 2\n")

            for i in range (N):
                for j in range (M):

                    if ((TableroHorizontal[i][j] == "1") and\
                            (TableroVertical[i][j] == "1") and\
                            (TableroHorizontal[i+1][j] == "1") and\
                            (TableroVertical[i][j+1] != "1")):

                        TableroVertical[i][j+1] = "1"
                        TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                                TableroVertical,\
                                                                TableroCuadros,\
                                                                filas,columnas,\
                                                                2,turno)

                        
                    elif((TableroHorizontal[i][j] == "1") and\
                             (TableroVertical[i][j] == "1") and\
                             (TableroVertical[i][j+1] == "1") and\
                             (TableroHorizontal[i+1][j] != "1")):

                        TableroHorizontal[i+1][j] = "1"
                        TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                                TableroVertical,\
                                                                TableroCuadros,\
                                                                filas,columnas,\
                                                                2,turno)


                    elif((TableroHorizontal[i][j] == "1") and\
                             (TableroHorizontal[i+1][j] == "1") and\
                             (TableroVertical[i][j+1] == "1") and\
                             (TableroVertical[i][j] != "1")):
                        
                        TableroVertical[i][j] = "1"
                        TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                                TableroVertical,\
                                                                TableroCuadros,\
                                                                filas,columnas,\
                                                                2,turno)

                    elif((TableroVertical[i][j] == "1") and\
                         (TableroHorizontal[i+1][j] == "1") and\
                         (TableroVertical[i][j+1] == "1") and\
                         (TableroHorizontal[i][j] != "1")):
                    
                        TableroHorizontal[i][j] = "1"
                        TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                                TableroVertical,\
                                                                TableroCuadros,\
                                                                filas,columnas,\
                                                                2,turno)
            # Aqui deberia haber una verificacion de que todavia se puede seguir jugando, es decir que hay cuadros sin completar

            opcion = randint(1,2)
                
            if (opcion == 1):
                i,j = randint(0,N),randint(0,M-1)
                TableroHorizontal[i][j] = "1"
                TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                        TableroVertical,\
                                                        TableroCuadros,filas,\
                                                        columnas,2,turno)
                
            elif (opcion == 2):
                i,j = randint(0,N-1),randint(0,M)
                TableroVertical[i][j] = "1"
                TableroCuadros,turno = HacerCuadros(TableroHorizontal,\
                                                        TableroVertical,\
                                                        TableroCuadros,filas,\
                                                        columnas,2,turno)
                
            else:
                quit()

        ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)

    return TableroHorizontal,TableroVertical,TableroCuadros,TurnoActual


# Definicion de funcion que imprime las instrucciones
#------------------------------------------------------------------------------#

def Instrucciones () -> (str):

# Precondicion: True 

# Postcondicion: True // Esta funcion imprime las instrucciones del juego
                        
# y no modifica ninguna varriable del juego


    print("\n")
    print ("Cada jugador en su turno debe seleccionar entre dos puntos, \
horizontales o verticales, para trazar una raya \n")

    print ("El objetivo del juego es completar la mayor cantidad de cuadrados \n")
    
    print ("Al marcar una raya en el tablero ocurre un cambio de turno a menos \
que el jugador complete un cuadrado con dicha raya, caso en el que puede volver a jugar \n")

    print ("Al final del juego gana el jugador con mayor cantidad de cuadros marcados \n")


# Definicion de funcion que marca una linea horizontal en el tablero
#------------------------------------------------------------------------------#

def MarcarLineaHorizontal(TableroHorizontal: list) -> (list):

# Precondicion: len(TableroHorizontal) >=2

# Postcondicion: TableroHorizontal[lineafila][lineacolumna] == "1"

    lineafila = 0    # Esta variable especifica la fila en donde va a marcar\
                     # una linea el jugador que este jugando
                     
    lineacolumna = 0 # Esta variable especifica la columna en donde va a marcar\
                     # una linea el jugador que este jugando



    


    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))

    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))

    TableroHorizontal[lineafila][lineacolumna] = "1"

    return TableroHorizontal


# Definicion de funcion que marca una linea vertical en el tablero
#------------------------------------------------------------------------------#

def MarcarLineaVertical(TableroVertical: list) -> (list):

# Precondicion: len(TableroVertical) >=2

# Postcondicion: TableroVertical[lineafila][lineacolumna] == "1"

    lineafila = 0    # Esta variable especifica la fila en donde va a marcar\
                     # una linea el jugador que este jugando
                     
    lineacolumna = 0 # Esta variable especifica la columna en donde va a marcar\
                     # una linea el jugador que este jugando

    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    
    TableroVertical[lineafila][lineacolumna] = "1"

    return TableroVertical


# Definicion de funcion que marca un cuadrado en el tablero y dice de que jugador fue  
#------------------------------------------------------------------------------#

def HacerCuadros(TableroHorizontal: list, TableroVertical: list,TableroCuadros:\
list,filas: int,columnas: int,jugador: int,turno: bool) -> (list,bool):

# Precondicion:len(TableroHorizontal)==filas*(columnas-1) and\
# len(TableroVertical)==(filas-1)*columnas and\
# len(TableroCuadros)==(filas-1)*(columnas-1) and\
# filas>=2 and columnas >=2 and (jugador == 1 or jugador == 2) and turno

# Postcondicion: any((TableroCuadros[i][j] == 1) for i in range(filas-1)\
# for j in range(columnas-1) \  if jugador == 1 and\
# ((TableroHorizontal[i][j] == "1") and (TableroVertical[i][j] == "1") and\
# (TableroHorizontal[i+1][j] == "1") and (TableroVertical[i][j+1] == "1") and\
# (TableroCuadros[i][j] != "1") and (TableroCuadros[i][j] != "2"))) or\ 
# (any((TableroCuadros[i][j] == 2) for i in range(filas-1)\
# for j in range(columnas-1) if jugador == 2 and\
# ((TableroHorizontal[i][j] == "1") and (TableroVertical[i][j] == "1") and\
# (TableroHorizontal[i+1][j] == "1") and (TableroVertical[i][j+1] == "1") and\
# (TableroCuadros[i][j] != "1") and (TableroCuadros[i][j] != "2")))

    N = filas-1
    
    M = columnas-1

    for i in range (N): 
        
        for j in range (M): 

            if ((TableroHorizontal[i][j] == "1") and \
                        (TableroVertical[i][j] == "1") and \
                        (TableroHorizontal[i+1][j] == "1") and\
                        (TableroVertical[i][j+1] == "1") and \
                        (TableroCuadros[i][j] == "0")):

                if (jugador == 1):
                    TableroCuadros[i][j] = "1"
                    turno = True
                    return TableroCuadros,turno
                elif (jugador == 2):
                    TableroCuadros[i][j] = "2"
                    turno = True
                    return TableroCuadros,turno
                else:
                    quit()
            else:
                turno = False

    return TableroCuadros,turno


# Definicion de funcion que permite cargar una partida especificada por el usuario
#------------------------------------------------------------------------------#

def CargarPartida(archivo: str) -> (list,list,list,int,int,int,int,int,int,str,str):

# Precondicion: archivo == "partida1.txt"

# Postcondicion: filas>=2 and columnas>=2

    Atributos = []
    
    Partida = open("archivo.txt")
    
    Atributos = Partida.readlines()
    
    print (Atributos)
    
    filas = Atributos[0]
    
    columnas = Atributos[1]

    CantidadDeJugadores = Atributos[2]

    TurnoActual = Atributos[3]
    
    NombreJugador1 = Atributos[4]
    
    if ("CPU" == Atributos[5]):

        NombreJugador2 = Atributos[5]
        TipoJugador = 1
    else:
        NombreJugador2 = Atributos[5]
        TipoJugador = 2
        
    for i in range(7,filas+7):
        TableroHorizontal[i-7] = Atributos[i]
    
    for i in range(filas+8,columnas+filas+7):
        TableroVertical[i-filas-8] = Atributos[i]
        
    for i in range(columnas+filas+8,(filas-1)+columnas+filas+8):
        TableroCuadros[i-columnas-filas-8] = Atributos[i]

    return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,\
        columnas,PuntajeJugador1,PuntajeJugador2,TurnoActual,NombreJugador1,\
        NombreJugador2

        
# Definicion de funcion que guarda una partida
#------------------------------------------------------------------------------#

def GuardarPartida(archivo) -> (str):

# Precondicion: filas>=2 and columnas>=2

# Postcondicion: archivo == "partida1.txt"

    print("La partida ha sido guardada!")


# Definicion de funcion que imprime el puntaje al momento de la partida
#------------------------------------------------------------------------------#

def Puntaje(TableroCuadros: list, PuntajeJugador1: int, PuntajeJugador2: int)\
 -> (int,int):

# Precondicion: len(TableroCuadros)>=2 and PuntajeJugador1>=0 and\
# PuntajeJugador2>=0

# Postcondicion: (PuntajeJugador1 == (sum( 1 for i in range (filas-1)\
# for j in range (columnas-1) \
# if TableroCuadros[i][j]=="1"))) and\
# (PuntajeJugador2 == (sum( 1 for i in range (filas-1) \
# for j in range (columnas-1) if TableroCuadros[i][j]=="2")) 
    for i in range(filas-1):
        for j in range(columnas-1):
            if (TableroCuadros[i][j] == "1"):
                PuntajeJugador1 = PuntajeJugador1 + 1
            elif (TableroCuadros[i][j] == "2"):
                PuntajeJugador2 = PuntajeJugador2 + 1
            else:
                pass

    return PuntajeJugador1,PuntajeJugador2


# Definicion de funcion que imprime el puntaje final de la partida
#------------------------------------------------------------------------------#

def PuntajeFinal(PuntajeJugador1: int,PuntajeJugador2: int,filas: int,\
columnas: int) -> (str):

# Precondicion:PuntajeJugador1 + PuntajeJugador2 == (filas-1)*(columnas-1)

# Postcondicion: (resultado == PuntajeJugador1>PuntajeJugador2) or \
# (resultado == PuntajeJugador1<PuntajeJugador2) or\
# (resultado == PuntajeJugador1=PuntajeJugador2)

    resultado = ""

    if (PuntajeJugador1 > PuntajeJugador2):
        resultado = "Ha ganado el jugador 1"
    elif (PuntajeJugador1 < PuntajeJugador2):
        resultado = "Ha ganado el jugador 2"
    else:
        resultado = "Ha habido un empate"

    print (resultado)




# Definicion de funcion que especifica el turno de juego
#------------------------------------------------------------------------------#

def Turno (TipoJugador: list,TableroHorizontal: list,TableroVertical: list,\
TableroCuadros: list,filas: int,columnas: int,azar: int) -> (list,list,list) :

# Precondicion: (TipoJugador==1 or TipoJugador==2) and\
# len(TableroHorizontal)==filas*(columnas-1) and \
# len(TableroVertical)==(filas-1)*columnas and
# len(TableroCuadros)==(filas-1)*(columnas-1) and filas>=2 and \
# columnas>=2 and (azar==1 or azar==2)

# Postcondicion: (PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,\
#TableroCuadros,filas,columnas,TurnoActual) and\
# SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,\
# filas,columnas,TipoJugador,TurnoActual)) or\
# (PrimerTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,\
# filas,columnas,TipoJugador,TurnoActual) and\
# SegundoTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,\
# filas,columnas,TurnoActual))


    PrimerTurno = Jugador1    # Variable que hace el llamado al jugador x al\
                              # que le corresponde jugar de primero
                              
    SegundoTurno = Jugador2   # Variable que hace el llamado al jugador y al\
                              # que le corresponde jugar de segundo
        	
# Nota: 'x' e 'y' vienen dados por el azar si se escoge el modo de juego\
# de dos personas
    
    if (TipoJugador == 1):
        PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,\
                                   filas,columnas,TurnoActual)
        SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,\
                                    filas,columnas,TipoJugador,TurnoActual)
    elif (TipoJugador == 2):
        if (azar == 1):
            PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,\
                                       TableroCuadros,filas,columnas,TurnoActual)
            SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,\
                                        TableroCuadros,filas,columnas,\
                                        TipoJugador,TurnoActual)
        elif (azar == 2):
            PrimerTurno = Jugador2(TableroHorizontal,TableroVertical,\
                                       TableroCuadros,filas,columnas,\
                                       TipoJugador,TurnoActual)
            SegundoTurno = Jugador1(TableroHorizontal,TableroVertical,\
                                        TableroCuadros,filas,columnas,\
                                        TurnoActual)

    return PrimerTurno,SegundoTurno





#####################
def MarcarLinea(event):
    
    TOL = 8
    CELLSIZE = 50
    OFFSET = 50
    CIRCLERAD = 2
    DOTOFFSET = 50
    GAME_H = 400
    GAME_W = 400

    
    x,y = event.x,event.y

    startx = CELLSIZE * ((x-OFFSET)//CELLSIZE) + DOTOFFSET
    starty = CELLSIZE * ((y-OFFSET)//CELLSIZE) + DOTOFFSET
    tmpx = (x-OFFSET)//CELLSIZE
    tmpy = (y-OFFSET)//CELLSIZE

    dx = ((x-OFFSET)-(x-OFFSET//CELLSIZE)*CELLSIZE)
    dy = ((y-OFFSET)-(y-OFFSET//CELLSIZE)*CELLSIZE)

    orient = orientacion(dx,dy,TOL)

    if orient == HORIZONTAL:
        endx = startx + CELLSIZE
        endy = starty
    else:
        endx = startx
        endy = starty + CELLSIZE
        #print "line drawn: %d,%d to %d,%d" % (startx,starty,endx,endy)
    
    canvas.create_line(startx,starty,endx,endy)
    

def orientacion(dx,dy,TOL):
    if abs(dx) < TOL:
        if abs(dy) < TOL:
            return None  # mouse in corner of box; ignore
        else:
            orient = VERTICAL
    elif abs(dy) < TOL:
        orient = HORIZONTAL
    else:
        return None


def mostrar_coordenadas(event):
    x, y = event.x, event.y
    mensaje = 'Clic en la posición (%d, %d)' % (x, y)
    #canvas.create_line(x,x2,y,y2, width=2)
    print(mensaje)
    return x,y

######################




# Definicion de funcion que imprime el menu del juego y permite escoger el tipo de juego
#------------------------------------------------------------------------------#

def ModoJuego()-> (int,bool):

# Precondicion: True

# Postcondicion: ((seleccion== 1) or (seleccion == 2) or (seleccion == 3) or\
# (seleccion == 4) or (seleccion == 5)) and filas>=2 and columnas>=2 and\
# len(TableroHorizontal) >=2 and len(TableroVertical) >=2 and\
# len(TableroCuadros) >=2

    seleccion = 0   # Variable que especifica la seleccion del menu hecha\
                    # por el usuario

    filas = 0    # Variable que guarda la cantidad de filas que quiere el\
                # usuario en el tablero
   
    columnas = 0    # Variable que guarda la cantidad de columnas que quiere el\ 
                   # usuario en el tablero


    print ("\n\n\tBienvenido a Connect TableroHorizontale dots!\n")
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
        root = Tk()
        root.geometry("600x480")
        canvas = Canvas(root, bg='white',width = 400, height = 400)

        for i in range (filas):
        	for j in range (columnas):
        		canvas.create_oval(40*i+10,40*j+10,40*i+10+2*2,40*j+10+2*2,fill="black")
        		canvas.pack()


        TableroHorizontal,TableroVertical,\
            TableroCuadros = Inicializacion(filas,columnas)
        TipoJugador = 1
        PuntajeJugador1 = 0
        PuntajeJugador2 = 0
        TurnoActual = 1
        NombreJugador1 = ""
        NombreJugador2 = ""

        return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,\
            filas,columnas,PuntajeJugador1,PuntajeJugador2,TurnoActual,\
            NombreJugador1,NombreJugador2

    elif (seleccion == 2):

        # Aqui va la inicializacion de datos realizando la llamada a la funcion
        # Adicionalmente se dice el tipo de jugador que es el jugador 2
        
        filas = int(input('Escribe el numero de filas del tablero: '))
        columnas = int(input('Escribe el nuemro de columnas del tablero: '))
        root = Tk()
        root.title = ("Connect the dots")
        root.configure(background='white')
        root.geometry("800x800")
       
        canvas = Canvas(root, bg='white',width = 800, height = 800)
        

        salir = Button(canvas, text="Salir",command = Salir,font= ("Agency FB",14),\
                           width=10).place(x=150,y=535)

        guardar = Button(canvas,text="Guardar",command = GuardarPartida("archivo.txt"),\
                             font= ("Agency FB",14),width=10).place(x= 500,y=535)

        x = 150-(filas*10)
        y = 100-(columnas*10)
        
        for i in range (filas):
            for j in range (columnas):
                canvas.create_oval(50 +(50*i+x*2.5),50 +(50*j+y*2.5),\
                                       (x*2.5)+(50*i+50+2*2),\
                                       (y*2.5)+(50*j+50+2*2),fill="black")
                canvas.pack()

        canvas.bind("<Button-1>",mostrar_coordenadas)
        
        NombreJugador1 = "Douglas"
        NombreJugador2 = "Roberto"
        TableroHorizontal,TableroVertical,\
            TableroCuadros = Inicializacion(filas,columnas)
        TipoJugador = 2
        PuntajeJugador1 = 0
        PuntajeJugador2 = 0
        TurnoActual = 0
        #NombreJugador1 = ""
        #NombreJugador2 = ""
        
        nombre1 = Label(canvas, text=NombreJugador1,font= ("Agency FB",14),\
                           width=10).place(x=25,y=150)

        nombre2 = Label(canvas, text=NombreJugador2,font= ("Agency FB",14),\
                           width=10).place(x=665,y=150)


        return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,\
            filas,columnas,PuntajeJugador1,PuntajeJugador2,TurnoActual,\
            NombreJugador1,NombreJugador2

    elif (seleccion == 3):

        # Aqui el programa carga la partida de un archivo

       TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,\
           columnas,PuntajeJugador1,PuntajeJugador2,TurnoActual,\
           NombreJugador1,NombreJugador2 = CargarPartida("archivo.txt")
       
       return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,\
           filas,columnas,PuntajeJugador1,PuntajeJugador2,TurnoActual,\
           NombreJugador1,NombreJugador2

    elif (seleccion == 4):

        # Aqui se imprimen las instrucciones del juego al llamarse a la funcion instruccion

        Instrucciones()

    elif (seleccion == 5):
        quit()


# Definicion de funcion que permite salir del juego en cualquier momento
#------------------------------------------------------------------------------#
def Salir() -> ():

# Precondicion: True // No recibe parametros de entrada

# Postcondicion: (seleccion == 1) or (seleccion == 2)

    #seleccion = 0    # Variable que especifica la eleccion del usuario si\
                     # desea salir
    quit()

   # print ("Esta funcion te permite salir del juego en cualquier momento")



####################### PROGRAMA PRINCIPAL #####################################


TableroHorizontal = []   # Lista que guarda la matriz del tablero de rayas\
                         # horizontales

TableroVertical = []    # Lista que guarda la matriz del tablero de rayas\
                        # verticales

TableroCuadros = []    # Lista que guarda la matriz del tablero de cuadros

TipoJugador = 0    # Variable entera que almacena el tipo de jugador que es\
                   # jugador 2, si es humano o maquina

filas = 0    # Variable entera que especifica la cantidad de filas que se\
             # usaran en los tableros

columnas = 0    # Variable entera que especifica la cantidad de columnas\
                # que se usaran en los tableros

azar = 0    # Variable entera que especifica el jugador que empieza a jugar\
            # de primero en caso de ser humano vs humano

TurnoActual = 0    # Variable entera que especifica cual jugador esta\
                   # jugando al momento

PuntajeJugador1 = 0    # Variable entera que almacena la puntuacion del\
                       # jugador 1

PuntajeJugador2 = 0     # Variable entera que almacena la puntuacion del\
                        # jugador 2

MovimientosMaximos = 0    # Variable entera que almacena la cantidad maxima\
                          # de rayas posibles


# Precondicion: True // Como toda la interaccion del usuario es con las\
# funciones, las precondiciones de estas seran las que especifiquen todos los\
# datos validos en el programa


TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,columnas,\
    PuntajeJugador1,PuntajeJugador2,TurnoActual,NombreJugador1,\
    NombreJugador2 = ModoJuego()


"""nombre1=StringVar()
nombre2=StringVar()
nombre1.set(grupo.NombreJugador1)
nombre2.set(grupo.NombreJugador2)
label1 = Label(root, textvariable=nombre1, anchor = NE, fg = 'black')
label2 = Label(root, textvariable=nombre2, anchor = NW, fg = 'black')
label1.pack()
label2.pack()
"""

azar = randint(1,2)

print (azar)

MovimientosMaximos = ((((filas-1)*(columnas)) + ((filas)*(columnas-1)))//2)

ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)

for i in range(MovimientosMaximos):

    print()

    print ("Esta es la puntuacion de:",grupo.NombreJugador1,":",PuntajeJugador1)
    
    print ("Esta es la puntuacion de:",grupo.NombreJugador2,":",PuntajeJugador2)
    
    print()
    
    PrimerTurno,SegundoTurno = Turno(TipoJugador,TableroHorizontal,\
                                         TableroVertical,TableroCuadros,filas,\
                                         columnas,azar)
    
    PuntajeJugador1,PuntajeJugador2 = Puntaje(TableroCuadros,PuntajeJugador1,\
                                                  PuntajeJugador2)
    
PuntajeFinal(PuntajeJugador1,PuntajeJugador2,filas,columnas)

root.mainloop()

# Postcondicion: all((TableroCuadros[i][j] != "0") for i in range(filas-1)\
# for j in range(columnas-1))


################################################################################
#############################COMENTARIOS########################################
################################################################################

# Discutir uso de funcion Puntaje o agregarlo a la clase Estudiante

# Instrucciones va fuera de modo de juego, colocar instrucciones como una pestaña de ayuda

# Lo que diga el puntaje debe ir llamado en HacerCuadros para evitar que sume 1 punto cada turno por cada cuadro que ya se haya marcado (Parece ser mas util usarlo como clase en este modo)

# Hay que usar un while para el ciclo principal

# El booleano del while se va a verificar con TableroCuadros en cada funcion de cada jugador

# En caso de que se convierta en falso, debe salirse del ciclo

# Aun no se me ocurre ninguna forma en el caso de que se finalice el juego con el jugador que jugo de primero en el turno

# MovimientosMaximos es la cota

# En Jugador2 donde juega la maquina, no se esta usando la funcion de marcar linea y para evitar que randint escoga una posicion ya marcada habria que agregarle ese "atributo" a las funciones de marcar linea para que cada jugador tenga esa verificacion
