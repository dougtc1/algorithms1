######################## INICIALIZACION ########################################
def inicializacion():
#Precondicion: True
#Postcondicion: 
	matriz = [] 
	filas = int(input('Escribe el numero de filas: '))
	columnas = int(input('Escribe el nuemro de columnas: '))



######################## TABLERO ########################################
def tablero(N:int, M:int,matriz: list):
#Precondicion: 
#Postcondicion: 
	
	for i in range(N):
		matriz.append([])
		for j in range(M):
			matriz[i].append("0")

	for i in matriz:
		print(" ".join(i))
	
		
########################  #######################################

matriz = []

tablero(5,6,matriz)
