#
# Lab1Ejercicio2.py
# Descripcion: El siguiente programa, dados 3 valores enteros a,b,c
# que cumplen a>=b>=c, intercambia los valores de tal manera que
# cumplan a<=b<=c
#
# Autor:
#       Douglas Torres
#
# Ultima modificacion: 8/04/2014
#

# Variables
#        a: int // Valor que almacena un valor
#        b: int // Valor que almacena un valor
#        c: int // Valor que almacena un valor

# Valores iniciales
a=30
b=20
c=10

# Precondicion
assert (a>=b>c)

print "Valores iniciales"
print a,b,c

# Calculo
a,b,c=c,b,a

# Postcondicion
assert (c>=b>=a)

# Salida
print a,b,c
