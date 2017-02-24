(*
 *  Ejercicio 3 del laboratorio 4
 *
 *  Descripcion: El siguiente programa pide al usuario los coeficientes
 *  de una matriz NxM y calcula la suma de toso sus elementos
 *  Autor: Douglas Torres
 *  Ultima modificacion: 22/03/2014
 *)

program Lab04Ejercicio3;

const
   N = 5; // grado máximo de los polinomios a usar
   M = 5; // grado máximo de los polinomios a usar

type 
   matriz = array [0..N,0..M] of real; // matriz
	
var
   a   : matriz;  // matriz 
   sum : real; // suma de 
   i,j : integer; // indices

begin

   (* Entrada de datos *)
   writeln;
   writeln ('El siguiente programa calcula la suma de todos',
	    ' los coeficientes de una matriz'); 
   writeln ('Introduzca los coeficientes de la matriz ',N,'x',M);
   for i:=1 to N do begin
      for j:=1 to M do begin
	 write ('Coeficiente a[',i,',',j,'] = ');
	 readln (a[i,j]);
      end;
   end;

   {Precondicion: (%forall i : 1<=i<=N : (%forall j : 1<=j<=M : a[i,j]))}

   (* Calculo de resultados *)

   sum := 0;
   for i:=0 to N do begin
      for j:=0 to M do begin
	 sum := sum+a[i,j];
      end;
   end;

   {Postcondicion: sum %in R /\ (%forall i : 1<=i<=N : (%forall j > 1<=j<M : sum=sum+a[i,j]))}

   (* Salida de datos *)

   writeln;
   write ('El resultado de la suma de todos los coeficientes dados es = ');
   writeln (sum:2:2);
   readln
end.