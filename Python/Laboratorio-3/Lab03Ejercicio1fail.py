#
# Lab03Ejercicio1.py
# 
# Descripcion: Este programa permite al usuario escoger una opcion de un menu
# de tres opciones
# Autor: Douglas Torres
# Ultima modificacion: 29/04/2014
#
# Variables:
#     seleccion : integer // 
#     resultado : float // 
#     largo : float // 
#     ancho : float // 
#     radio : string // 
#     n : boolean //
#

# Entrada de datos

resultado = 0

seleccion = int(input("Se le presentan 3 opciones: \n" \
                      "Opcion 1: Superficie de una habitacion \n" \
                      "Opcion 2: Area de una circunferencia \n" \
                      "opcion 3: Suma de cuadrados \n"))

if (seleccion == 1):
    largo = float(input("Introduzca el largo de la habitacion: "))
    ancho = float(input("Introduzca el ancho de la habitacion: "))
elif (seleccion == 2):
    radio = float(input("Introduzca el radio de la circunferencia: "))
elif (seleccion == 3):
    n = int(input("Introduzca un numero natural: "))

# Precondicion

try:
  assert ((((seleccion == 1) and largo >= 0 and ancho >=0) or \
          ((seleccion == 2) and radio >= 0) or \
          ((seleccion == 3) and n > 0)))
except AssertionError:
  print ("La Precondicion no se cumple")


# Calculo de datos

if (seleccion == 1):
     resultado = largo*ancho
elif (seleccion == 2):
    resultado = radio*radio*3,1416
elif (seleccion == 3):
    resultado = sum(x**2 for x in range (1,n+1))

# Postcondicion

assert (((seleccion==1) and resultado==largo*ancho and resultado>=0) or \
            ((seleccion==2) and resultado==radio*radio*3,1416 and resultado>=0) or \
            ((seleccion == 3) and resultado==sum(x*x for x in range (1,n+1))))
# Salida de datos
print("El resultado de la opcion escogida es:",resultado)
