#
# Sol_Quiz2.py
#
# DESCRIPCION: solucion del problema planteado para el quiz 2
#
# Autor:  Prof.  Luis Landaeta

# declaracion de variables
# para evitar problemas las inicializo
A,B,C = 0, 0, 0      # float
disc = 0.0           # float
E_lineal = False     # bool
R_reales = False     # bool

# lectura de datos
A = float(input('Coeficiente termino cuadratico y presione Enter: '))
B = float(input('Coeficiente termino lineal y presione Enter: '))
C = float(input('Coeficiente termino independiente y presione Enter: '))

################
# PRECONDICION: #
################################################################################
# Evitaremos ecuacion degenerada
assert( not(A==0 and B==0 and C!=0) )
################################################################################

# Calculos
# calcularemos el discriminante
disc = B*B - 4*A*C

# inicializacion
E_lineal = False
R_reales = True     

#Salidas
if A==0:
   print('Ecuacion Lineal')
   E_lineal = True;
elif disc==0:
   print('Solucion unica de multiplicidad 2')
elif disc>0:
   print('Raices distintas y reales')
elif disc<0:
   print('Raices distintas y complejas')
   R_reales = False

#################
# POSTCONDICION: #
assert( E_lineal == (A==0) and (B*B - 4*A*C >= 0) == R_reales )
################################################################################


