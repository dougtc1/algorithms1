#
# Lab05Ejercicio2.py
# 
# Descripcion: Este programa verifica si una secuencia de enteros no negativos
# ingresada por el usuario esta ordenada de forma creciente.
#
# Autor: Douglas Torres
# Ultima modificacion: 13/05/2014
#
# Variables:
#    N : integer //
#    i : integer // 
#    cota : integer //
#   
# Datos iniciales


i = 0

# Entrada de datos

N  = int(input("Introduzca un numero natural: ")) 

# Precondicion

try:
    assert (N>0 and N!=4)
except:
    print ("La precondicion no se cumple")
    quit()



# Verificacion del invariante al inicio

try:
    assert (N!=4 and i==sum(i for i in range(i) if N!=4))
except:
    print("La verificacion del invariante fallo.")
    quit()

# Calculo de datos

while (N != 4):

    # Verificacion del invariante en cada iteracion
    try:
        assert (N!=4 and i==sum(1 for i in range(i) if N!=4))
    except:
        print("La verificacion del invariante fallo.")
        quit()

    if (N % 2 == 0):
        N = N//2
        i = i + 1
        print ("El numero actual es :",N,"\n")
        print ("Numero de intento :",i,"\n")
    else:
        N = (N*3)+1
        i = i + 1
        print ("El numero actual es :",N,"\n")
        print ("Numero de intento :",i,"\n")

# Postcondicion

try:
    assert (N==4)
except:
    print ("La postcondicion fallo.")
    quit()

# Salida de datos

print ("Se llego al 4, que comienza la serie: 4,2,1 en",i,"pasos","\n")
