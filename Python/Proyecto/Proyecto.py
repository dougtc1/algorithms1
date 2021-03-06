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

# Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and \
# len(TableroCuadros)==(filas-1)*(columnas-1) and all((TableroHorizontal[i][j] == 0) for i in range(filas) \
# for j in range(columnas-1))and ((TableroVertical[i][j] == 0) for i in range(filas-1) \
# for j in range(columnas) ((TableroCuadros[i][j] == 0) for i in range(filas-1) for j in range(columnas-1)))

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

def ImprimirTablero(TableroHorizontal: list, TableroVertical: list, TableroCuadros:list) -> (list,list,list):
#Precondicion: len(TableroHorizontal) >=2 and len(TableroVertical) >=2 and len(TableroCuadros) >=2
#Postcondicion: True // Esta funcion no modifica ninguna variable que recibe, solo imprime los tableros en un formato mas amigable para el usuario
     
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

def Jugador1(TableroHorizontal: list,TableroVertical: list,TableroCuadros: list,filas: int,columnas: int,TurnoActual: int) -> (list,list,list,int):
# Precondicion: len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1) and filas>=2 and columnas>=2 and (TurnoActual==2)

#Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1)
    
    # Aqui se usa un while para definir el turno de cada jugador
    
    turno = True
    
    TurnoActual = 1
    
    while (turno):

        print ("Turno jugador 1")

        opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))

        if (opcion == 1):
            TableroHorizontal = MarcarLineaHorizontal(TableroHorizontal)
            
        elif (opcion == 2):
            TableroVertical = MarcarLineaVertical(TableroVertical)
            
        else:
            quit()
        
 #       print (HacerCuadros(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,1,turno))
    
        TableroCuadros,turno = HacerCuadros(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,1,turno)
        
#        print(turno)

        ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)
    
    return TableroHorizontal,TableroVertical,TableroCuadros,TurnoActual
        

# Definicion de funcion que permite al jugador 2 hacer su jugada
#------------------------------------------------------------------------------#

def Jugador2(TableroHorizontal: list,TableroVertical: list,TableroCuadros: list,filas: int,columnas: int,TipoJugador: int,TurnoActual: int) -> (list,list,list,int):
# Precondicion: (TipoJugador==1 or TipoJugador==2) and len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1) and filas>=2 and columnas>=2 and TurnoActual==1

#Postcondicion: len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1)

    # Aqui se usa un while para definir el turno de cada jugador

    turno = True
    TurnoActual = 2

    while (turno):

        if (TipoJugador == 2):

            print("Es humano","\n")

            print("Turno jugador 2\n")

            opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))

            if (opcion == 1):
                TableroHorizontal = MarcarLineaHorizontal(TableroHorizontal)
            
            elif (opcion == 2):
                TableroVertical = MarcarLineaVertical(TableroVertical)
                
            else:
                quit()
            
            TableroCuadros,turno = HacerCuadros(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,2,turno)
            
            print (turno)

            ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)
        
        else:

            print("Es computadora","\n")

            print("Turno jugador 2\n")
            
            if (all (TableroHorizontal[i][j] == 1 and TableroVertical[i][j] == 1 and TableroHorizontal[i+1][j] == 1 \
                         for i in range (filas-2) for j in range (columnas-2))):
                
                TableroVertical[i][j+1] = "1"
                
                
            elif(all ((TableroHorizontal[i][j] == 1) and (TableroVertical[i][j] == 1) and (TableroVertical[i][j+1] == 1) \
                          for i in range (filas-2) for j in range (columnas-2))):
                
                TableroHorizontal[i+1][j] = "1"

            
            elif(all ((TableroHorizontal[i][j] == 1) and (TableroHorizontal[i+1][j] == 1) and (TableroVertical[i][j+1] == 1) \
                          for i in range (filas-2) for j in range (columnas-2))):
                
                TableroVertical[i][j] = "1"
            
            elif(all ((TableroVertical[i][j] == 1) and (TableroHorizontal[i+1][j] == 1) and (TableroVertical[i][j+1] == 1) \
                     for i in range (filas-2) for j in range (columnas-2))):
                
                TableroHorizontal[i][j] = "1"
           
            else:
                
                opcion = randint(1,2)

                if (opcion == 1):
                    i,j = randint(0,filas-2),randint(0,columnas-2)
                    TableroHorizontal[i][j] = "1"
            
                elif (opcion == 2):
                    i,j = randint(0,filas-2),randint(0,columnas-2)
                    TableroVertical[i][j] = "1"
                
                else:
                    quit()
            
            TableroCuadros,turno = HacerCuadros(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,2,turno)
            ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)
            
    return TableroHorizontal,TableroVertical,TableroCuadros,TurnoActual


# Definicion de funcion que imprime las instrucciones
#------------------------------------------------------------------------------#
        
def Instrucciones () -> (str):
# Precondicion: True
#Postcondicion: True

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
#Precondicion: len(TableroHorizontal) >=2
#Postcondicion: TableroHorizontal[lineafila][lineacolumna] == "1"
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TableroHorizontal[lineafila][lineacolumna] = "1"

    return TableroHorizontal


# Definicion de funcion que marca una linea vertical en el tablero
#------------------------------------------------------------------------------#

def MarcarLineaVertical(TableroVertical: list) -> (list):
#Precondicion: len(TableroVertical) >=2
#Postcondicion: TableroVertical[lineafila][lineacolumna] == "1"
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TableroVertical[lineafila][lineacolumna] = "1"

    return TableroVertical


# Definicion de funcion que marca un cuadrado en el tablero y dice de que jugador fue  
#------------------------------------------------------------------------------#

def HacerCuadros(TableroHorizontal: list, TableroVertical: list,TableroCuadros: list,filas: int,columnas: int,jugador: int,turno: bool) -> (list,bool):

#Precondicion:len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1) and filas>=2 and columnas >=2 and (jugador == 1 or jugador == 2) and turno
#Postcondicion: all((TableroCuadros[i][j] == 1) for i in range(filas-1) for j in range(columnas-1) if jugador == 1) or all((TableroCuadros[i][j] == 2) for i in range(filas-1) for j in range(columnas-1) if jugador == 2)

# for i in range (filas-2) and for j in range (columnas-2) and if ((TableroHorizontal[i][j] == "1") and (TableroVertical[i][j] == "1") and (TableroHorizontal[i+1][j] == "1") and (TableroVertical[i][j+1] == "1") and (TableroCuadros[i][j] != "1") and (TableroCuadros[i][j] != "2")):

    if (any((TableroHorizontal[i][j] == "1") and \
        (TableroVertical[i][j] == "1") and \
        (TableroHorizontal[i+1][j] == "1") and \
        (TableroVertical[i][j+1] == "1") and \
        (TableroCuadros[i][j] == "0") for i in range(filas-2) for j in range(columnas-2))):

        if (jugador == 1):
            (TableroCuadros[i][j]) = "1"
            turno = True
            return TableroCuadros,turno
        else:
            (TableroCuadros[i][j]) = "2"
            turno = True
            return TableroCuadros,turno
    else:
        turno = False

    return TableroCuadros,turno


# Definicion de funcion que permite cargar una partida especificada por el usuario
#------------------------------------------------------------------------------#

def CargarPartida(archivo: str) -> ():

# Precondicion: archivo == "partida1.txt"
# Postcondicion: filas

    Atributos = []
    Partida = open("archivo")
    Atributos = Partida.readlines()
    filas = Atributos[0]
    columnas = Atributos[1]

# Preguntar sobre 3era linea de cantidad de jugadores

    TurnoActual = Atributos[3]
    grupo.NombreJugador1 = Atributos[4]
    grupo.NombreJugador1 = Atributos[5]
    for i in range(7,filas+7):
        TableroHorizontal = Atributos[i]
    Inicializacion(filas,columnas)
    print("Cargar partida")

# Definicion de funcion que guarda una partida
#------------------------------------------------------------------------------#

def GuardarPartida(archivo) -> (str):
# Precondicion:
#Postcondicion:

    print("Guardar partida")


# Definicion de funcion que imprime el puntaje al momento de la partida
#------------------------------------------------------------------------------#

def Puntaje(TableroCuadros: list, PuntajeJugador1: int, PuntajeJugador2: int) -> (int,int):
# Precondicion: len(TableroCuadros)>=2 and PuntajeJugador1>=0 and PuntajeJugador2>=0
# Postcondicion: (PuntajeJugador1 == (sum( 1 for i in range (filas-1) for j in range (columnas-1) if TableroCuadros[i][j]=="1"))) and (PuntajeJugador2 == (sum( 1 for i in range (filas-1) for j in range (columnas-1) if TableroCuadros[i][j]=="2")) 

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

def PuntajeFinal(PuntajeJugador1: int,PuntajeJugador2: int,filas: int,columnas: int) -> (str):
# Precondicion:PuntajeJugador1 + PuntajeJugador2 == (filas-1)*(columnas-1)
# Postcondicion: (resultado == PuntajeJugador1>PuntajeJugador2) or (resultado == PuntajeJugador1<PuntajeJugador2) or (resultado == PuntajeJugador1=PuntajeJugador2)

    if (PuntajeJugador1 > PuntajeJugador2):
        resultado = "Ha ganado el jugador 1"
    elif (PuntajeJugador1 < PuntajeJugador2):
        resultado = "Ha ganado el jugador 2"
    else:
        resultado = "Ha habido un empate"
        
    print (resultado)




# Definicion de funcion que especifica el turno de juego
#------------------------------------------------------------------------------#

def Turno (TipoJugador: list,TableroHorizontal: list,TableroVertical: list,TableroCuadros: list,filas: int,columnas: int,azar: int) -> (list,list,list) :
# Precondicion: (TipoJugador==1 or TipoJugador==2) and len(TableroHorizontal)==filas*(columnas-1) and len(TableroVertical)==(filas-1)*columnas and len(TableroCuadros)==(filas-1)*(columnas-1) and filas>=2 and columnas>=2 and (azar==1 or azar==2)
#Postcondicion: (PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TurnoActual) and SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TipoJugador,TurnoActual)) or (PrimerTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TipoJugador,TurnoActual) and SegundoTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TurnoActual))
    if (TipoJugador == 1):
        PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TurnoActual)
        SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TipoJugador,TurnoActual)
    elif (TipoJugador == 2):
    	if (azar == 1):
    		PrimerTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TurnoActual)
    		SegundoTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TipoJugador,TurnoActual)
    	elif (azar == 2):
    		PrimerTurno = Jugador2(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TipoJugador,TurnoActual)
    		SegundoTurno = Jugador1(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,TurnoActual)
    	
    return PrimerTurno,SegundoTurno


# Definicion de funcion que imprime el menu del juego y permite escoger el tipo de juego
#------------------------------------------------------------------------------#

def ModoJuego()-> (int,bool):
# Precondicion: True
#Postcondicion: (seleccion== 1) or (seleccion == 2) or (seleccion == 3) or (seleccion == 4) or (seleccion == 5)

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
        
        TableroHorizontal,TableroVertical,TableroCuadros = Inicializacion(filas,columnas)
        TipoJugador = 1

        return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,columnas

    elif (seleccion == 2):

        # Aqui va la inicializacion de datos realizando la llamada a la funcion
        # Adicionalmente se dice el tipo de jugador que es el jugador 2

        filas = int(input('Escribe el numero de filas del tablero: '))
        columnas = int(input('Escribe el nuemro de columnas del tablero: '))
        
        TableroHorizontal,TableroVertical,TableroCuadros = Inicializacion(filas,columnas)
        TipoJugador = 2
                
        return TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,columnas

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

TableroHorizontal,TableroVertical,TableroCuadros,TipoJugador,filas,columnas = ModoJuego()

azar = randint(1,2)

print (azar)

MovimientosMaximos = (((filas-1)*(columnas)) + ((filas)*(columnas-1)))//2

TurnoActual = 0
PuntajeJugador1=0
PuntajeJugador2=0
i = 0
ImprimirTablero(TableroHorizontal,TableroVertical,TableroCuadros)
for i in range(MovimientosMaximos):
    PuntajeJugador1,PuntajeJugador2 = Puntaje(TableroCuadros,PuntajeJugador1,PuntajeJugador2)
    print()
    print ("Esta es la puntuacion de:",grupo.NombreJugador1,":",PuntajeJugador1)
    print ("Esta es la puntuacion de:",grupo.NombreJugador2,":",PuntajeJugador2)
    print()
    PrimerTurno,SegundoTurno = Turno(TipoJugador,TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,azar)
    PuntajeJugador1,PuntajeJugador2 = Puntaje(TableroCuadros,PuntajeJugador1,PuntajeJugador2)

	
PuntajeFinal(PuntajeJugador1,PuntajeJugador2,filas,columnas)



"""    opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))
    if (opcion == 1):
        TableroHorizontal = MarcarLineaHorizontal(TableroHorizontal)
        
    elif (opcion == 2):
        TableroVertical = MarcarLineaVertical(TableroVertical)
    
    else:
        quit()

    TableroCuadros = HacerCuadros(TableroHorizontal,TableroVertical,TableroCuadros,filas,columnas,jugador)
		
    print()
    print("--------------------")

	
print("***CUADROS***")

ImprimirTablero(TableroCuadros)




# Discutir randint dentro de marcar linea horizontal y vertical

# Discutir modo de los turnos

# Discutir formato general del programa

# Faltan por crear las estructuras de datos de los jugadores (Necesarias para la funcion de guardar y cargar)
# Instrucciones va fuera de modo de juego, colocar instrucciones como una pestaña de ayuda"""
