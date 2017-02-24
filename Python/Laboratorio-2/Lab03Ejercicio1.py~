#
# Lab03Ejercicio1.py
#
# Descripcion: Este programa determina si un anyo es bisiesto
#
# Autor: Douglas Torres
# Ultima modificacion: 22/04/2014
#
# 
# Variables
#       anyo : integer // Variable que almacena el valor del anyo
#       esBisiesto : bool // Variable que verifica si es bisiesto o no el anyo
#

# Valores iniciales
anyo = 1600
esBisiesto = True

# Precondicion

assert (anyo > 0)

# Calculo de datos

if (anyo % 4 != 0):
        esBisiesto = False
elif (anyo % 100 != 0 or anyo % 400 == 0):
        pass
elif (anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 != 0):
        esBisiesto = False

# Postcondicion

assert ((esBisiesto == ((anyo % 4 != 0) or (anyo % 4 == 0 and \
anyo % 100 == 0 and anyo % 400 != 0))) or (esBisiesto == ((anyo % 100 != 0 \
or anyo % 400 == 0))))

# Salida de datos

print "La verificacion del anyo si es bisiesto o no es: "
print esBisiesto
