#
# Lab04Ejercicio1.py
# 
# Descripcion: Este programa recibe 10 numeros enteros, los coloca en un 
# arreglo y verifica su suma.
#
# Autor: Douglas Torres
# Ultima modificacion: 02/05/2014
#
# Constantes:
#   N = 10
#
# Variables:
# 	suma : integer // Variable que gurada la suma de los numeros del arreglo 
# 	i : string //Variable de iteracion que se usa en el invariante
# 	cota : integer // Variable que guarda la cota
#

# Entrada de datos

suma = 0
i=0
N=10
cota=N-i

print ("Inserte 10 numeros enteros al arreglo: ")
A = [int(input("A[" + str(i) + "]=")) for i in range (N)]

# Precondicion

try:
  assert (0<=i<N and N==10)
except AssertionError:
  print ("La Precondicion no se cumple")
  quit()

# Calculo de datos

for x in range (N):
    suma = suma+A[x]

    assert (0<=i<N)

# Postcondiciion

try:
    assert (suma==sum(x for x in A))
except AssertionError:
    print("La postcondicion no se cumple.")
    quit()


print ("La suma de los elementos del arreglo es =",suma)