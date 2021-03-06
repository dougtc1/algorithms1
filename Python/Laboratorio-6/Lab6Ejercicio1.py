#
# Lab06Ejercicio1.py
# 
# Descripcion: Este programa verifica si una secuencia de enteros no negativos
# ingresada por el usuario esta ordenada de forma creciente.
#
# Autor: Douglas Torres
# Ultima modificacion: 20/05/2014
#

################################################################################
########################## Declaracion de funciones ############################
################################################################################


# Declaracion de funcion que lee la secuencia de elementos

def leer (N : int) -> (list):
    
    # Precondicion: N>=0
    # Postcondicion: len(C)>0
     
    i = 0    # i:integer // Variable de iteracion 
    cota = N-i    # cota:integer // Cantidad de iteraciones a realizar 
    C = [int(i) for i in range (N)]    # C:array[0..N) de enteros // Secuencia ingresada
    
    # Verificacion del invariante al inicio

    try:
        assert (0<=i<=N)
    except AssertionError:
        print ("Hubo un error en el invariante.")
        quit()

    # Verificacion de cota al inicio

    try:
        assert (cota>=0)
    except AssertionError:
        print ("Hubo un error en la cota.")
        quit()
    
    # Iteracion que se usa para llenar el arreglo con los numeros a verificar
    
    for i in range (0,N):
        
        # Verificacion de invariante en cada iteracion
        
        try:
            assert (0<=i<N)
        except AssertionError:
            print ("Hubo un error en el invariante.")
            quit()
            
        # Verificacion de cota positiva en cada iteracion
            
        try:
            assert (cota>=0)
        except AssertionError:
            print ("Error cota no positiva.")
            quit()
            
        C[i] = [int(input("C[" + str(i) + "]="))]

    return C

# Declaracion de funcion que verifica el ordenamiento de la secuencia dada

def verificar (lista: list, N: int) -> (str):
    
    # Precondicion: len(lista)>=0 and N>=0
    # Postcondicion: len(resultado1)>0
    
    i = 1    # i:integer // Variable de iteracion 
    cota = N-i    # cota:integer // Cantidad de iteraciones a realizar 
    creciente = False    # creciente:boolean // Especifica si es creciente
    orden = True    # orden:boolean // Especifica si esta ordenada
    resultado1 = ""    # resultado:string // Especifica el tipo de secuencia

    # Verificacion del invariante al inicio

    try:
        assert (0<=i<=N)
    except AssertionError:
        print ("Hubo un error en el invariante.")
        quit()

    # Verificacion de cota al inicio

    try:
        assert (cota>=0)
    except AssertionError:
        print ("Hubo un error en la cota.")
        quit()
   
    for i in range (1,N):
        if (lista[i] >= lista[i-1]):
            creciente = True
            if (orden):
                resultado1 = "La lista es creciente"
        else:
            if (creciente):
                resultado1 = "La lista esta en desorden"
                creciente = False
                orden = False
            else:
                resultado1 = "La lista es decreciente"

        # Verificacion de invariante en cada iteracion
        
        try:
            assert (1<=i<=N)
        except AssertionError:
            print ("Hubo un error en el invariante.")
            quit()
            
        # Verificacion de cota positiva en cada iteracion
            
        try:
            assert (cota>=0)
        except AssertionError:
            print ("Error cota no positiva.")
            quit()
    
    return resultado1

# Declaracion de funcion que imprime el resultado de la verificacion

def imprimir (resultado: str) -> (str):
    
    # Precondicion: len(resultado)>0
    # Postcondicion: len(resultado)>0
    print (resultado,"\n")


################################################################################
########################## Programa principal ##################################
################################################################################


# Declaracion de variables

N = 0    # N:integer // Tamanio arreglo

C = []    # lista:lista [0..N) de enteros // Secuencia de numeros ingresados

resultado=""    # resultado:string // Especifica el tipo de secuencia

# Entrada de datos

N = int(input("Introduzca la cantidad de numeros de la secuencia: "))

lista = leer(N)

# Precondicion

try:            
    assert (2<=len(lista)<=N)
except AssertionError:
    print("La precondicion no se cumple")
    quit()

# Calculo de datos

resultado = verificar(lista,N)

# Postcondicion

try:
    assert (resultado=="La lista es creciente" or \
            resultado=="La lista es decreciente" or \
            resultado=="La lista esta en desorden")
except AssertionError:
    print ("La postcondicion no se cumple.")
    quit()

# Salida de datos

imprimir (resultado)
