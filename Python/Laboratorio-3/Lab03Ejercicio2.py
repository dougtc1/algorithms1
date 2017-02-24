#
# Lab03Ejercicio2.py
# 
# Descripcion: Este programa calcula si un numero entero positivo es primo
#
# Autor: Douglas Torres
# Ultima modificacion: 30/04/2014
#
# Variables:
# 	n : integer // Variable que almacena un numero n a verificar si es primo
#   esPrimo : string //Variable que almacena el resultado de n si es primo o no
#	i : integer // Variable de iteracion
# 	j : integer // Variable de iteracion
#

# Entrada de datos

i = 2
j = 1

n = int(input("Introduzca un valor n y se le dira si es un numero primo: "))

# Precondicion

try:
  assert (n>0)
except AssertionError:
  print ("La Precondicion no se cumple")
  quit()

# Calculo de datos

if (n==1):
	esPrimo = "es numero primo"
else:
	while (i<=n):
		if (n%i == 0 and n==i):
			esPrimo = "es numero primo"
			i += 1
		elif (n%i == 0 and n!=i):
			esPrimo = "no es numero primo"
			while (j<n):
				if (n%j == 0):
					print ("El numero",j,"es divisor de",n)
				j += 1
			break
		else:
			i += 1

# Postcondicion

try:
  assert (n==1 or (2<=i<=n+1 and 1<=j<=n))
except AssertionError:
  print ("La Postcondicion no se cumple")
  quit()

# Salida de datos

print (n,esPrimo)