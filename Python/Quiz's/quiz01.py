#
# quiz01.py
# 
# Descripcion: Este programa pide al usuario la coordenada del centro de una
# circunferencia en el formato (x,y) y el valor del radio ademas de un punto
# que se verifica si pertenece al borde de la circunferencia
#
# Autor: Douglas Torres
# Carnet: 11-11027
# Ultima modificacion: 22/04/2014
#
# Variables
#       a : real // Variable que almacena la coordenada X del centro
#       b : real // Variable que almacena la coordenada Y del centro
#       r : real // Variable que almacena el radio de la circunferencia
#       x1 : real // Variable que almacena la coordenada X del pto a verificar
#       y1 : real // Variable que almacena la coordenada Y del pto a verificar
#       verificar : bool // Variable que almacena el valor de la verificacion
#

# Valores de entrada
a=float(input("Introduzca la coordenada X del centro de la circunferencia: "))
b=float(input("Introduzca la coordenada Y del centro de la circunferencia: "))
r=float(input("Introduzca el radio de la circunferencia: "))
x1=float(input("Introduzca la coordenada X del punto a verificar: "))
y1=float(input("Introduzca la coordenada Y del punto a verificar: "))

# Precondicion

assert (r > 0 and a > 0 and b > 0 and x1 > 0 and y1 > 0)

# Calculo

if ((x1-a)**2+(y1-b)**2 == r**2):
        verificar = True
else:
        verificar = False

# Postcondicion

assert (verificar == ((x1-a)**2+(y1-b)**2 == r**2))

# Salida de Datos

print "El resultado de la verificacion del punto es: "
print verificar
