#
# Lab06Ejercicio2.py
# 
# Descripcion: Este programa recibe una secuencia de N numeros naturales y
# calcula la serie de fibonacci de todos los numeros de la secuencia.
#
# Autor: Douglas Torres
# Ultima modificacion: 21/05/2014
#

################################################################################
########################## Declaracion de funciones ############################
################################################################################

# Declaracion de funcion que crea la secuencia de numeros ingresada por el usuario

def leer (N : int) -> (list):
    
    # Precondicion: N>=0
    # Postcondicion: len(C)>=0
     
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
    
    for i in range (N):
        
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
            
        C[i] = int(input("C[" + str(i) + "]="))

    return C



# Declaracion de funcion que calcula el numero de fibonacci de un numero

def fib (lista: int) -> (int):

    # Precondicion: lista>=0
    # Postcondicion: x>=0

    if (lista == 0):
        x = 0
    elif (lista == 1):
        x = 1
    else:
        x = fib(lista-1)+fib(lista-2)

    return x

def imprimir (resultado: list) -> (list):
    
    # Precondicion: len(resultado)>0
    # Postcondicion: len(resultado)>0
    print (resultado,"\n")


################################################################################
########################## Programa principal ##################################
################################################################################

# Declaracion de variables

N = 0    # N:integer // Tamanio arreglo

C = []    # lista:lista [0..N) de enteros // Secuencia de numeros ingresados

# Entrada de datos

N = int(input("Introduzca la cantidad de numeros de la secuencia: "))

# Precondicion

try:            
    assert (2<=N)
except AssertionError:
    print("La precondicion no se cumple")
    quit()

i = 0           # i:int // Variable de iteracion

cota = N-i      # cota:int // Cantidad maxima de iteraciones

resultado=[int(i) for i in range (N)]    #resultado:array of int//Fibonacci calculado

lista = leer(N)

# Calculo de datos

for i in range (N):
    # Verificacion de invariante en cada iteracion
    try:
        assert (0<=i<N)
    except AssertionError:
        print ("Hubo un error en el invariante final.")
        quit()
        
    # Verificacion de cota positiva en cada iteracion
        
    try:
        assert (cota>=0)
    except AssertionError:
        print ("Error cota no positiva.")
        quit()
    
    resultado[i] = fib(lista[i])

# Postcondicion

try:
    assert (0<=len(resultado)<=N)
except AssertionError:
    print ("La postcondicion no se cumple.")
    quit()

# Salida de datos

imprimir (resultado)
