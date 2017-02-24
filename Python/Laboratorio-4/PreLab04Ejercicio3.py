#
# Lab04Ejercicio2.py
# 
# Descripcion: Este programa recibe N los nombres, indices y edades de
# N estudiantes, luego se calcula el promedio de edad y el promedio de indice
# 
# Autor: Douglas Torres
# Ultima modificacion: 05/05/2014
#
#
# Variables:
# 	numeradored : integer // Variable que gurada la suma de las edades 
# 	numeradorin : float // Variable de almacena la suma de los indices
# 	i : integer // Variable de iteracion
#	cota : integer // Variable que establece la cantidad de veces a iterar
#	nombre : string // Objeto de una clase que guarda el nombre de un estudiante
#	edad : integer // Objeto de una clase que guarda la edad de un estudiante
#	indice : float // Objeto de una clase que guarda el indice de un estudiante
#	promedioed : float // Variable que almacena el promedio de edades
#	promedioin : float // Variable que almacena el promedio de indice
#
# Entrada de datos

numeradored=0
numeradorin=0
i=0

class Estudiante:
	edad = 1
	nombre = ""
	indice = 1.0
	

N=int(input("Inserte el numero de estudiantes: "))

grupo = [ Estudiante() for x in range(N)]

cota=N-i

for i in range (N):
	print("Estudiante:",i+1)
	grupo[i].edad=int(input("Introduzca la edad: "))
	grupo[i].nombre=str(input("Introduzca el nombre: "))
	grupo[i].indice=float(input("Introduzca el indice: "))
	assert (i<N)
 
# Precondicion

for i in range (N):
	try:
		assert (0<grupo[i].edad<=130 and 1.0<=grupo[i].indice<=5.0 and \
				len(grupo[i].nombre)>=1 and 0<=i<N and N>0)
	except AssertionError:
  		print ("La Precondicion no se cumple.")
  		quit()

# Calculo de datos

for i in range (N):
	numeradored = numeradored + grupo[i].edad
	
	numeradorin = numeradorin + grupo[i].indice

	assert (0<=i<N and N>0)

promedioed = numeradored/N

promedioin = numeradorin/N

# Postcondicion

try:
	assert (promedioed==numeradored/N and promedioin==numeradorin/N and \
			promedioed>0 and promedioin>0)
except AssertionError:
	print ("La Postcondicion no se cumple.")
	quit()

# Salida de datos

print ("El promedio de edad es =",promedioed,"\n"
		"y el promedio de indice es =",promedioin)
