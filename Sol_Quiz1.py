#
# quiz01.py
#
# Descripcion: Dados el centro (a,b) y el radio r que definen una circunferencia 
# la cual se encuentra inmensa dentro del primer cuadrante del plano, verifica 
# que un punto (x1,y1) pertenece al borde de la circunferencia.
#
# Autores:  Prof. Rosseline Rodriguez
#
# Ultima modificacion: 21/04/2014
#
# VARIABLES:
#	a,b: float          // Entrada: centro de la circunferencia
#	r: float            // Entrada: radio de la circunferencia
#	x1,y1: float        // Entrada: punto a verificar
#   enElBorde: boolean  // Salida: dice si (x1,y1) está en el borde

# Valores iniciales:
a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
r = float(input("Valor del radio: "))

x1 = float(input("Valor de x1: "))
y1 = float(input("Valor de y1: "))
	
# Precondicion: La circunferencia está en el cuadrante 1
assert(a > 0 and b > 0 and r <= a and r <= b)

# Precondicion: (x1,y1) también está en el cuadrante 1
assert(x1 > 0 and y1 > 0)

# Calculos:
enElBorde = ( (x1-a)**2 + (y1-b)**2 == r**2 )

# Postcondicion: 
assert( enElBorde == ( (x1-a)**2 + (y1-b)**2 == r**2 ) )

# Salida:
print("("+str(x1) + "," + str(y1) + ") esta en el borde ? " + str(enElBorde))

