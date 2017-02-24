#
# Lab03Ejercicio3.py
#
# Descripcion: Este programa da al usuario un menu con 5 opciones diferentes
# dependiendo de los valores dados a la variable m
#
# Autor: Douglas Torres
# Ultima modificacion: 22/04/2014
#
# Variables
#   m : integer // Variable que almacena un valor entero
#   n : integer // Variable que almacena un valor entero
#   resultado : integer // Variable que almacena el resultado de una operacion
#

# Valores iniciales
m=10
n=2

# Calculo de datos

if (m==10):
    resultado = m/n
elif (m==5):
    resultado = m*n
elif (m==3):
    resultado = m+n
elif (m==2):
    resultado = m**n
else:
    resultado = m

# Postcondicion

assert ((m==10 and resultado==m/n) or (m==5 and resultado == m*n) or \
(m==3 and resultado == m+n) or (m==2 and resultado == m**n) or (resultado==m))

# Salidad de datos

print "El resultado es: "
print resultado
