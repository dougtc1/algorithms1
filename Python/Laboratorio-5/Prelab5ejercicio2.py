# Prelab2Ejercicio2.py
# Descripcion: El siguiente programa calcula las raices de un polinomio
# de la forma Ax^2+BX+C
# Autor:
#       Douglas Torres
#
# Ultima modificacion: 19/04/2014
#
#
# Constantes
# 		A : int // Numero que almacena el coeficiente de grado 2 			
# 		B : int // Numero que almacena el coeficiente de grado 1
# 		C : int // Numero que almacena el coeficiente de grado 0
# Variables
# 		x1 : float // Variable que almacena el valor de la segunda raiz
# 		x2 : float // Variable que almacena el valor de la segunda raiz
# 
# Valores iniciales

A=int(input("Introduzca el valor del coeficiente de grado 2 "))
B=int(input("Introduzca el valor del coeficiente de grado 1 "))
C=int(input("Introduzca el valor del coeficiente de grado 0 "))

# Precondicion
try:
    assert (A!=0 and 4*A*C<B*B)
except:
    print ("La precondicion no se cumple")
    quit()

# Calculo

x1 = (-B+(((B**2)-4*A*C)**(1/2)))/2*A
x2 = (-B-(((B**2)-4*A*C)**(1/2)))/2*A

# Postcondicion
try:
    assert (A*(x1**2)+(B*x1)+C == 0 and A*(x2**2)+(B*x2)+C == 0)
except:
    print("La postcondicion no se cumple")
    quit()

# Salida
print ("Las raices del polinomio especificado son x1 = ",x1," y x2 = ",x2)
