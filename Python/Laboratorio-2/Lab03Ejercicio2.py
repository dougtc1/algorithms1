#
# Lab03Ejercicio2.py
#
# Descripcion: Este programa determina si un ciudadano puede votar o no dentro
# de un sistema electoral
#
# Autor: Douglas Torres
# Ultima modificacion: 22/04/2014
#
# Variables
# esDecendienteExtranjero : bool // Variable que especifica la nacionalidad
# edad : integer // Variable que almacena la edad del ciudadano
# puedeVotar : bool // Variable que especifica la posibilidad de votar
#

# Valores iniciales

esDecendienteExtranjero = True
puedeVotar = True
edad = 35

# Precondicion

assert (0 < edad < 120)

# Calculo de datos

if (esDecendienteExtranjero):
        if (edad >= 25):
                pass
        else:
                puedeVotar = False

if (not esDecendienteExtranjero):
        if (edad >= 18):
                pass
        else:
                puedeVotar = False

# Postcondicion

assert (((esDecendienteExtranjero and edad >= 25) == puedeVotar) or \
((not esDecendienteExtranjero and edad >= 18) == puedeVotar))

# Salida de datos
print "Puede votar: "
print puedeVotar
