#
# Lab06Ejercicio3.py
# 
# Descripcion: Este programa imprime la lista de los factores primos de M que
# son menores o iguales a N.
#
# Autor: Douglas Torres
# Ultima modificacion: 31/05/2014
#

################################################################################
########################## Declaracion de funciones ############################
################################################################################


# Declaracion de funcion que verifica si un numero es primo

def primo (M: int,i: int,N: int) -> (int):

    if (M==1):
      factor = 1
      return factor
    elif (M%i  == 0 and M == i and i<=N):
      factor = i
      return factor
    else:
      pass

# Declaracion de funcion que verifica si un numero divide a otro

def divisibilidad (M: int,factor :int,N: int) -> (list):
   
  if (M%factor == 0 and factor<=N):
    resultado = factor
    return resultado
  else:
    pass


################################################################################
########################## Programa principal ##################################
################################################################################

# Inicializacion de variables

lista = [1]

# Entrada de datos

M = int(input("Introduzca un numero al que se le buscaran los factores primos: "))

N = int(input("Introduzca un numero natural que sera mayor o igual a los factores primos: "))

# Precondicion

try:
  assert (M>=N and N>0)
except AssertionError:
  print ("La Precondicion no se cumple")
  quit()

# Calculo de datos

for i in range(2,N):
  factor = primo(M,i,N)
  div = divisibilidad (M,factor,N)
  lista.append(div)

# Postcondicion

try:
  assert (len(div)>=1 and len(factprimos)>=1)
except AssertionError:
  print ("La Postcondicion no se cumple")
  quit()

# Salida de datos

print ("Los divisores primos de",M," son:",div)
