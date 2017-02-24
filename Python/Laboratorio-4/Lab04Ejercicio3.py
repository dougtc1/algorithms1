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
#	numpromedioparcial1 : integer // Guarda la suma de las notas del parcial 1
#	numpromedioparcial2 : integer // Guarda la suma de las notas del parcial 2
#	numpromedioparcial3 : integer // Guarda la suma de las notas del parcial 3
#	numpromedioparcial4 : integer // Guarda la suma de las notas del parcial 4
#	promedioparc1 : float  // Variable que guarda el promedio del parcial 1
#	promedioparc2 : float  // Variable que guarda el promedio del parcial 2
#	promedioparc3 : float  // Variable que guarda el promedio del parcial 3
#	promedioparc4 : float  // Variable que guarda el promedio del parcial 4
#
# Valores iniciales

numeradored=0
numeradorin=0
numpromedioparcial1 = 0
numpromedioparcial2 = 0
numpromedioparcial3 = 0
numpromedioparcial4 = 0
i=0 

class Estudiante:
	edad = 1
	nombre = ""
	indice = 1.0
	parcial1 = 1
	parcial2 = 1
	parcial3 = 1
	parcial4 = 1
	nota =	1
	notaf = 1
	
# Entrada de datos

N=int(input("Inserte el numero de estudiantes: "))

grupo = [ Estudiante() for x in range(N)]

cota=N-i

for i in range (N):
	print("Estudiante:",i+1)
	grupo[i].edad=int(input("Introduzca la edad: "))
	grupo[i].nombre=str(input("Introduzca el nombre: "))
	grupo[i].indice=float(input("Introduzca el indice: "))
	grupo[i].parcial1=int(input("Introduzca la nota del primer parcial:" ))
	grupo[i].parcial2=int(input("Introduzca la nota del segundo parcial:" ))
	grupo[i].parcial3=int(input("Introduzca la nota del tercer parcial: "))
	grupo[i].parcial4=int(input("Introduzca la nota del cuarto parcial:" ))
	assert (i<N)
 
# Precondicion

for i in range (N):
	try:
		assert (0<grupo[i].edad<=130 and 1.0<=grupo[i].indice<=5.0 and \
				len(grupo[i].nombre)>=1 and 0<=i<N and N>0 and \
				0<=grupo[i].parcial1<=25 and 0<=grupo[i].parcial2<=25 and \
				0<=grupo[i].parcial3<=25 and 0<=grupo[i].parcial4<=25)
	except AssertionError:
  		print ("La Precondicion no se cumple.")
  		quit()

# Calculo de datos

for i in range (N):
	numeradored = numeradored + grupo[i].edad
	
	numeradorin = numeradorin + grupo[i].indice

	numpromedioparcial1 = numpromedioparcial1 + grupo[i].parcial1

	numpromedioparcial2 = numpromedioparcial2 + grupo[i].parcial2
	
	numpromedioparcial3 = numpromedioparcial3 + grupo[i].parcial3

	numpromedioparcial4 = numpromedioparcial4 + grupo[i].parcial4

	grupo[i].nota = grupo[i].parcial1+grupo[i].parcial2+grupo[i].parcial3 + \
					grupo[i].parcial4

	if grupo[i].nota>=85 and grupo[i].nota<=100:
		grupo[i].notaf = 5
	elif grupo[i].nota>=70 and grupo[i].nota<=84:
		grupo[i].notaf = 4
	elif grupo[i].nota>=50 and grupo[i].nota<=69:
		grupo[i].notaf = 3
	elif grupo[i].nota>=30 and grupo[i].nota<=49:
		grupo[i].notaf = 2
	elif grupo[i].nota>=0 and grupo[i].nota<=29:
		grupo[i].nota = 1


	assert (0<=i<N and N>0 and 1<=grupo[i].notaf<=5)


promedioed = numeradored/N

promedioin = numeradorin/N

promedioparc1 = numpromedioparcial1/N

promedioparc2 = numpromedioparcial2/N

promedioparc3 = numpromedioparcial3/N

promedioparc4 = numpromedioparcial4/N



# Postcondicion

try:
	assert (promedioed==numeradored/N and promedioin==numeradorin/N and \
			promedioed>0 and promedioin>0 and \
			promedioparc1==numpromedioparcial1/N and \
			promedioparc2==numpromedioparcial2/N and \
			promedioparc3==numpromedioparcial3/N and \
			promedioparc4==numpromedioparcial4/N)
except AssertionError:
	print ("La Postcondicion no se cumple.")
	quit()

# Salida de datos

print ("El promedio de edad es =",promedioed,"\n"
		"El promedio de indice es =",promedioin,"\n"
		"El promedio del parcial 1 es =",promedioparc1, "\n"
		"El promedio del parcial 2 es =",promedioparc2, "\n"
		"El promedio del parcial 3 es =",promedioparc3, "\n"
		"El promedio del parcial 4 es =",promedioparc4, "\n")

for i in range(N):
	print ("La nota final del estudiante",i+1,"es =",grupo[i].notaf, "\n")
