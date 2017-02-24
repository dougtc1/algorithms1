#
# Lab04Ejercicio2.py
# 
# Descripcion: Este programa calcula la suma de todos los elementos de 
# una matriz NxM
#
# Autor: Douglas Torres
# Ultima modificacion: 06/05/2014
#
# Variables:
#    matriz : array // Arreglo que guarda la matriz NxM
#    N : integer // Variable que dice la cantidad de filas de la matriz
#    M : integer // Variable que dice la cantidad de columnas de la matriz
#    suma : integer // Variable que guarda la suma de los elementos de la matriz

# Entrada de datos

N = int(input("Introduzca el numero de filas que desea en su matriz: "))

M = int(input("Introduzca el numero de columnas que desea en su matriz: "))

matriz = [[int(input("matriz[" + str(i) +","+str(j)+"]=")) for i in range (N)] \
			for j in range (M)]
# Precondicion

try:
	assert (N>0 and M>0 and len(matriz)>0)
except AssertionError:
	print ("La precondicion no se cumple.")
	quit()

# Calculo de datos

suma=0

for i in range (N):
	for j in range (M):
		suma = suma + matriz[i][j]

# Postcondicion

try:
	assert (suma>=0)
except AssertionError:
	print ("La postcondicion no se cumple.")
	quit()

# Salida de datos

print ("La suma de todos los elemento de la matriz es =",suma)