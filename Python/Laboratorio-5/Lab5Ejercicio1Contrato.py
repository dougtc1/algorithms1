#
# Lab05Ejercicio1.py
# 
# Descripcion: Este programa verifica si una secuencia de enteros no negativos
# ingresada por el usuario esta ordenada de forma creciente.
#
# Autor: Douglas Torres
# Ultima modificacion: 13/05/2014
#
# Variables:
#    N : integer // Variable que guarda el numero maximo de iteraciones
#    C : integer // Arreglo que guarda los numeros ingresados
#    seguir : boolean // Variable que especifica cuando parar una iteracion
#    i : integer // Variable de iteracion
#    creciente : boolean // Variable que especifica si el arreglo es creciente
#    leidos : integer // Variable que guarda la cantidad de datos leidos
#    cota : integer //
#
# Datos iniciales

seguir = True

N = 10

leidos = 0

i = 0

C = [int(i) for i in range (N)]

cota = N-i

creciente = False

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


# Entrada de datos 

for i in range (5):

# Verificacion de invariante en cada iteracion
        
    try:
        assert (0<=i<=N)
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

    leidos = i

# Precondicion

try:            
    assert (2<=len(C)<=N)
except AssertionError:
    print("La precondicion no se cumple")
    quit()



# Calculo de resultados

i=1
seguir = True

while (i<leidos and seguir):


    # Verificacion de invariante en cada iteracion
    
    try:
        assert (0<=i<=N)
    except AssertionError:
        print ("Hubo un error en el invariante.")
        quit()

    # Verificacion de cota decreciente en cada iteracion

    try:
        assert (cota>N-i)
    except AssertionError:
        print ("Error cota no decreciente.")
        quit()
            
    # Verificacion de cota positiva en cada iteracion
                        
    try:
        assert (cota>=0)
    except AssertionError:
        print ("Error cota no positiva.")
        quit()

    
    if (C[i] == [0]):
        seguir = False
    elif (C[i]>C[i-1]):
        i = i+1
        creciente = True
    else:
        seguir = False
        creciente = False
        i = i+1
    
# Postcondicion

try:
    assert (i<=leidos)
except AssertionError:
    print ("La postcondicion no se cumple.")
    quit()

# Salida de datos

print ("La secuencia es creciente =",creciente)
