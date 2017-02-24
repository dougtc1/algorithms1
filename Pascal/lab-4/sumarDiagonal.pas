 (*
  * sumarDiagonal
  * Programa para ilustrar el uso de arreglos multidimensionales
  * Autor: Prof. Rosseline Rodriguez
  * Fecha: 20/11/2012
  *)

program sumarDiagonal;

const
	N = 3;	// grado máximo de los polinomios a usar
type
	matriz = array [0..N,0..N] of real; // polinomios reales
	
var
	m  : matriz;  // matriz para calcular la suma de diagonal principal
	sum : real; // suma de la diagonal principal
	i,j : integer;	// indices
	
BEGIN
	(* Entrada de datos *)
    writeln;
	writeln('Introduzca la matriz M');
	for i:= 1 to N do begin
		for j:= 1 to N do begin
			write('Coeficiente de grado ',i:2,j:2,' = ');
			readln(m[i,j]);
		end;
	end;
	
    {PRE: i,j %in Z /\ 0<=i<=N /\ 0<=j<=N}
	
    (* Calculo *)

	sum := 0;
	for i:= 0 to N do begin
		sum := sum + m[i,i];
	end;

	{ Post: sum %in R /\ sum=sum+m[i,j]}
	
    (* Salida de datos *)
	
	writeln;
	writeln('La suma de la diagonal principal es:',sum:7:2);
	writeln;
	
end.