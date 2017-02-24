#
# Lab03Ejercicio2.py
# 
# Descripcion: Este programa verifica si un numero entero positivo es perfecto
#
# Autor: Douglas Torres
# Ultima modificacion: 30/04/2014
#
# Variables:
# 	n : integer // Variable que almacena un numero a verificar si es perfecto 
# 	esPerfecto : string //Variable que almacena el resultado de la verificacion
# 	i : integer // Variable de iteracion
# 	suma : integer // Variable que almacena la suma de los divisores de n
#

# Entrada de datos


i = 1
suma = 0
esPerfecto = "no es un numero perfecto"

n = int(input("Introduzca un valor n y se le dira si es un numero perfecto: "))

# Precondicion

try:
  assert (n>=2)
except AssertionError:
  print ("La Precondicion no se cumple")
  quit()

# Calculo de datos

while (i<n):
	if (n%i == 0 and n!=i):
		suma += i
		if (suma==n):
			esPerfecto = "es un numero perfecto"
	i += 1

# Postcondicion

try:
  assert (n==2 or (1<=i<=n and suma>0))
except AssertionError:
  print ("La Postcondicion no se cumple")
  quit()

# Salida de datos

print (n,esPerfecto)