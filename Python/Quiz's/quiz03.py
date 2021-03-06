#
# Quiz3.py
# 
# Descripcion: Este programa calcula la serie de Fibonacci de un numero N dado
# por el usuario.
#
# Autor: Douglas Torres
# carnet: 11-11027
# Ultima modificacion: 06/05/2014
#
# Variables:
#    N : integer // Variable que guarda el numero de serie de Fibonacci a calcular
#    fibonacci : integer // Variable que almacena la serie de fibonacci
#    z : integer // Variable que guarda la serie de fibonacci del termino N-2
#

# Entrada de datos

def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

N = int(input("Introduzca un numero N y se le calculara la serie de fibonacci: "))


# Precondicion

try:
    assert (N>=0)
except AssertionError:
    print ("La precondicion no se cumple.")
    quit()

# Calculo de resultados

if N == 0:
    fibonacci=0

elif N==1:
    fibonacci=1

else:
    z=0
    fibonacci=1
    for i in range (2,N+1):
        fibonacci,z=fibonacci+z,fibonacci


# Postcondicion

try:
    assert (fibonacci == fib (N))
except AssertionError:
    print ("La postcondicion no se cumple.")
    quit()

# Salida de datos

print ("El resultado de la serie de fibonacci es =",fibonacci)

