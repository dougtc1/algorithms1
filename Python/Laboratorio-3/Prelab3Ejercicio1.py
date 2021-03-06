# Prelab3Ejercicio1.py
# Descripcion: El siguiente programa calcula la suma de los factoriales desde
# 0 hasta N.
# Autor:
#       Douglas Torres
#
# Ultima modificacion: 28/04/2014
#
# Constantes
# 	N : int // Numero que almacena el numero maximo del factorial
# 	p : int // Numero que almacena el resultado de la productoria		
#
# Variables
# 	suma : int // Variable que almacena el valor de la suma de los factoriales
# 	fact : int // Variable que almacena el valor del factorial
# 	cota : int // Variable que establece la cantidad de veces a iterar
# 	k : int //	Variable de iteracion
#
# Valores iniciales
#

N  = int(input("Introduzca un numero y se le calculara su factorial: "))
suma,fact,k = 0,1,1
cota = N-k+1

def prod (i):
	p=1
	for n in i:
		p *= n
	return p

# Precondicion

try:
	assert (N>=0)
except:
	print("La precondicion no se cumple")
	quit()

# Calculo de datos

	# Verificacion del invariante al inicio
try:
	assert (0<=k<=N and suma == sum (prod (j for j in range (1,x))) for x in range (0,k))
except:
	print("El invariante no se cumple")
	quit()

	# Verificacion de la cota al inicio

while (k<=N):
	if (k>0):
		fact = fact*k
	suma = suma+fact
	

	# Verificacion del invariante en cada iteracion

	try:
		assert (0<=k<=N and \
			suma == sum (prod (j for j in range (1,x))) for x in range (0,k))
	except:
		print("El invariante no se cumple")
		quit()

	# Verificacion de la cota positiva en cada iteracion

	try:
		assert (cota>=0)
	except:
		print ("La cota no es positiva")
		quit()

	# Verificacion de la cota decreciente en cada iteracion

	try:
		assert (cota>n-k+1)
	except:
		print ("La cota no es decreciente")
		quit()

# Postcondicion
try:
	assert (suma==sum (prod (j for j in range (1,x))) for x in range (0,k))
except:
	print ("La postcondicion no se cumple")
	quit()

# Salida
print ("La suma de los factoriales del numero",N,"es",suma)
