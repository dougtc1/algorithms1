################################################################################
######################## F U N C I O N E S #####################################
################################################################################

# Definicion de funcion que inicializa los datos del programa
#------------------------------------------------------------------------------#

def inicializacion(filas:int,columnas:int)->(list):
#Precondicion: True
#Postcondicion: filas>=2 and columnas>=2 and len(tablero)==filas*columnas
    
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

def imprimirTablero(tablero: list)-> (list):
#Precondicion: 
#Postcondicion: 
                    
    for i in tablero:
        print(" ".join(i))
        

################################  MarcarLineaHorizontal ##################################

def MarcarLineaHorizontal(TH: list) -> (list):
#Precondicion:
#Postcondicion:
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TH[lineafila][lineacolumna] = "1"

    return TH

#########################  MarcarLineaVertical  ###################################

def MarcarLineaVertical(TV: list) -> (list):
    lineafila = int(input('Escribe la fila donde quieres hacer la linea: '))
    lineacolumna = int(input('Escribe la columna donde quieres hacer la linea: '))
    TV[lineafila][lineacolumna] = "1"

    return TV

####################   HacerCuadrados    #########################################

def HacerCuadrados(TH: list, TV: list,TC: list,filas: int,columnas: int,jugador: int) -> (list):

#Precondicion:
#Postcondicion:

    for i in range (filas-2):
        for j in range (columnas-2):
           print(TH[i][j])
           print(TV[i][j])
           print(TH[i+1][j])
           print(TV[i][j+1])
           print(TC[i][j]) 

           if ((TH[i][j] == "1") and (TV[i][j] == "1") and (TH[i+1][j] == "1") and (TV[i][j+1] == "1")):
                if (jugador == 1):
                    (TC[i][j]) = "1"
                else:
                    (TC[i][j]) = "2"
           else:
               pass
    
    return TC

####################### PROGRAMA PRINCIPAL #####################################

jugador = 2

filas = int(input('Escribe el numero de filas del tablero: '))
columnas = int(input('Escribe el nuemro de columnas del tablero: '))



TH,TV, TC = inicializacion(filas,columnas)

for i in range((filas)*(columnas)):
    print("***HORIZONTAL***")
    print()
    imprimirTablero(TH)
    print()
    print("***VERTICAL***")
    print()
    imprimirTablero(TV)
    print()
    print("***Cuadros***")
    print()
    imprimirTablero(TC)
    print()

    opcion = int(input("Presione 1 para horizontal y 2 para vertical: "))
    if (opcion == 1):
        TH = MarcarLineaHorizontal(TH)
        
    elif (opcion == 2):
        TV = MarcarLineaVertical(TV)
    
    else:
        quit()

    TC = HacerCuadrados(TH,TV,TC,filas,columnas,jugador)
		
    print()
    print("--------------------")
	
print("***CUADROS***")

imprimirTablero(TC)
				

