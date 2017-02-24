# Lab1Ejercicio1.py
#
# DESCRIPCION: Programa que calcula el area de una circunferencia
#
# Autor: 
#	Douglas Torres
#
# Ultima modificacion: 8/04/2014
#
# CONSTANTES
#       pi=3.1415
#        
# VARIABLES:
#	radio: real // Valor del radio de la circunferencia
#       area: real //Valor del area de la circunferencia
#

radio = 8
pi=3.1415

# Precondicion: 
assert(radio > 0)

# Calculos:

area = pi*radio**2
	
# Postcondicion: 

assert(area == pi*radio**2)

# Salida:
print("El resultado es ")
print(area)
