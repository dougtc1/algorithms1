#
# PrelabEjercicio8.py
#
# Definicion: Este programa lee un archivo llamado input.txt e imprime en un
# archivo output.txt la secuencia de ADN no-factorizada de input.txt
#
# Autor: Douglas Torres
# Ultima modificacion: 04/06/2014
#
# Declaracion e inicializacion de variables
# 

archivo = open('input.txt')

noFactorizada = []

for line in archivo:

	linea = line

	noFactorizada.append(line)

	cantidad = line.split()

	for j in range(1):

		secuencia = ""

		producto = int(cantidad[j])

		secuencia = cantidad[j+1]
		
		print (secuencia*producto)