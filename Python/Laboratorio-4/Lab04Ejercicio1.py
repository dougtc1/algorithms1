#
# Lab04Ejercicio1.py
# 
# Descripcion: Este programa muestra en pantalla el grado de un polinomio
# dado por el usuario e imprime la notacion polinomial
#
# Autor: Douglas Torres
# Ultima modificacion: 06/05/2014
#
# Variables:
#    M : integer // Variable que guarda el numero maximo de grado
#    C : integer // Arreglo que guarda los coeficientes del polinomio
#    N : integer // Grado del polinomio ingresado
#    seguir : boolean // Variable que especifica cuando parar el arreglo

# Entrada de datos

seguir = True

i = 0

M = int(input("Introduzca el numero maximo de grado del polinomio: "))

C = [int(i) for i in range (M+1)]


while (i<=M and seguir):
    C[i] = [int(input("C[" + str(i) + "]="))]
    if (C[i] == [0]):
        seguir = False
        i=i+1
    else:
        i=i+1
        
# Precondicion

try:
    assert (M>=0 and len(C)<=M+1)
except AssertionError:
    print ("La precondicion no se cumple.")
    quit()

# Calculo de resultados

i=0

for i in range (M+1):
    if (C[i]==[0]):
        grado = i
        i = M+1
    else:
        grado=M
    
# Postcondicion

try:
    assert (M>=grado)
except AssertionError:
    print ("La postcondicion no se cumple.")
    quit()

# Salida de datos

print (C[0])
print (C[1])

print ("El grado del polinomio es:",grado,"y el polinomio es P(x):" "\n")
print (str(C[0]), end=" ")
for i in range (1,M+1):
    print ("+ "+str(C[i]) + "X^" + str(i), end=" ")

print ("\n")
