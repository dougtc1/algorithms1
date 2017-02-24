#
# Quiz2.py
# 
# Descripcion: Este programa especifica el tipo de solucion de un polinomio
# dado por el usuario.
#
# Autor: Douglas Torres
# carnet: 11-11027
# Ultima modificacion: 29/04/2014
#
# Variables:
# 	A : float // Variable que almacena el coeficiente de grado 2
# 	B : float // Variable que almacena el coeficiente de grado 1
# 	C : float // Variable que almacena el coeficiente de grado 0
#	discriminante : float // Variable que almacena el valor del discriminante
#	resultado : string // Variable que almacena el tipo de raices y polinomio
#	EsLineal : boolean // Variable que dice si se da una ecuacion lineal
#	R_reales : boolean // Variable que dice si el polinomio tiene raices reales
#	R_comp : boolean //Variable que dice si el polinomio tiene raices complejas
#
# Valores iniciales

# Se dan estos valores iniciales que se usaran para ver si se cumple 
# la postcondicion ya que deberian cambiar a True si pasa alguna de estas
# por alguna de las condiciones

EsLineal = False
R_reales = False
R_comp = False

# Entrada de datos

A = float(input("Introduzca un valor para el coeficiente de segundo grado: "))
B = float(input("Introduzca un valor para el coeficiente de primer grado: "))
C = float(input("Introduzca un valor para el coeficiente de grado cero: "))

# Precondicion

assert ((A == 0 and B == 0 and C != 0)==False )

# Calculo de datos

discriminante = B*B-(4*A*C)

if (A == 0):
	resultado = "El polinomio dado es una ecuacion lineal"
	EsLineal = True
elif (discriminante == 0):
	resultado = "El polinomio tiene una sola raiz real con multiplicidad 2"
	R_reales = True
elif (discriminante < 0):
	resultado = "Las raices del polinomio son complejas"
	R_comp = True
else:
	resultado = "El polinomio tiene 2 raices reales distintas"
	R_reales = True

# Postcondicion

assert (EsLineal or R_reales or R_comp)

# Salida de datos

print(resultado)


