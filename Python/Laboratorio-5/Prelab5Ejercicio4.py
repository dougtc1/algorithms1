# Prelab3Ejercicio2.py
# Descripcion:El siguiente programa calcula los divisores de un numero entero N
# Autor:
#       Douglas Torres
#
# Ultima modificacion: 28/04/2014
#
# Constantes
# 	N : int // Numero que almacena el numero a calcularle sus divisores
#
# Variables
# 	cuenta : int // Variable que cuenta la cantidad de divisores
# 	i : int // Variable de iteracion	
#	cota : int // Variable que almacena la cantidad de iteraciones
#
# Valores iniciales
#

N = int(input("Introduzca un valor para N."))
cuenta,i = 0,1
cota = N-i+1

# Precondicion

try:
	assert (N>0)
except:
	print("La precondicion no se cumple")
	quit()


# Calculo

	# Verificacion de invariante al inicio
try:
	assert (0<i<=N and cuenta == (sum (1 for j in range (1,i) if N%j == 0 )))
except:
	print("El invariante no se cumple")
	quit()

	# Verificacion de cota al inicio
try:
	assert (cota>=0)
except:
	print ("La cota no es positiva")
	quit()


while (i<=N):
	if (N % i == 0):
		cuenta = cuenta + 1
	i = i+1
	
	# Verificacion de invariante en cada iteracion

	try:
		assert (0<i<=N+1 and cuenta == (sum (1 for j in range (1,i) if N%j ==  0)))
	except:
		print ("El invariante no se cumple")
		quit()
	
	# Verificacion de cota positiva en cada iteracion

	try:
		assert (cota>=0)
	except:
		print ("La cota no es positiva")
		quit()

	# Verificacion de cota decreciente en cada iteracion

	try:
		assert (cota>N-i+1)
	except:
		print ("La cota no es decreciente")
		quit()

# Postcondicion
try:
	assert (cuenta == (sum (1 for j in range (1,i) if N%j ==  0)))
except:
	print("La postcondicion no se cumple")
	quit()

# Salida de datos
print ("La cantidad de divisores enteros que tiene",N,"es",cuenta)
