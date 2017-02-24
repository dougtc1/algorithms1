#
# Lab04Ejercicio2.py
# 
# Descripcion: Este programa recibe 9 elementos que conforman una matriz de 3x3
# y calcula si es diagonal.
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
j=0
N=3
cota=N-(i+j)+1

print ("Inserte 9 numeros enteros a la matriz: ")

M = [ [int(input("M[" + str(i) +","+str(j)+"]=")) for i in range (3)] \
	for j in range (3) ]

res="La matriz M=",M,"no es diagonal"
 
# Precondicion

try:
  assert (0<=i<N and 0<=j<N and N==3)
except AssertionError:
  print ("La Precondicion no se cumple.")
  quit()

# Calculo de datos

for i in range (3):
    for j in range (3):
    	if (i!=j and M[i][j]==0):
    		res = "La matriz M=",M,"si es diagonal"
    	
assert (0<=i<N and 0<=j<N and N==3)

# Postcondiciion

try:
	assert ((M[i][j]==0 and i!=j and res=="La matriz M=",M,"si es diagonal") \
	or (M[i][j]==0 and i==j and res=="La matriz M=",M,"no es diagonal."))
except AssertionError:
	print ("La Postcondicion no se cumple.")
	quit()

print (res)