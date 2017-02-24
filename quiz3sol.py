#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# quiz3sol.py
#
# Descripción: Calcula el fibonacci de un número natural n.
#
# Autor: Carlos Gómez
#
# Ultima modificación: 06/05/2014
#
# VARIABLES:
#	n: int          // Entrada
#	fibonacci: int  // Respuesta
#	actual: int     // Fibonacci de la última iteración
#	anterior: int   // Fibonacci de la penúltima iteración


# Valores iniciales:
n = int(input('Valor de n: '))


# Precondición
assert (n >= 0)


# Cálculos:

if n == 0:
    fibonacci = 0
elif n == 1:
    fibonacci = 1
else:
    anterior = 0
    actual = 1
    for i in range(2, n+1):
        fibonacci = anterior + actual
        anterior = actual
        actual = fibonacci


# Postcondición:

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


assert (fibonacci == fib(n))

# Salida:
print('El fibonacci de %d es %d' % (n, fibonacci))
