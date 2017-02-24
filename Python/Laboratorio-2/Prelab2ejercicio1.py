#
# Prelab2Ejercicio1.py
# Descripcion: El siguiente programa calcula el valor absoluto de a
# Autor:
#       Douglas Torres
#
# Ultima modificacion: 19/04/2014
#
#
# Constantes
# 		a : int // Numero al que se le va a calcular el valor absoluto 			
# Variables
# 		b: int // Variable que almacena el valor absoluto de a

# Valores iniciales

a = int(input("De un valor para a y se le dara el valor absoluto. "))


# Precondicion
try:
	assert (True)
except:
	print ("La precondicion no se cumple")
	quit()

# Calculo

if a >= 0:
	b = a
else: 
	b = -1*a

# Postcondicion
try:
	assert (b == abs(a))
except:
	print("La postcondicion no se cumple")
	quit()
# Salida
print ("El valor absoluto de ",a," es ",b)
