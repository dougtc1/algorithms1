(*
 *  Ejercicio 1 del laboratorio 4
 *
 *  Descripcion: El siguiente programa pide al usuario el grado
 *  de un polinomio y se le piden sus coeficientes para imprimir
 *  el polinomio especificado
 *  Autor: Douglas Torres
 *  Ultima modificacion: 21/03/2014
 *)

program Lab04Ejercicio1;

const
   N = 5;
   
type
   polinomio = array [0..N] of real;

var
   C : polinomio;
   i : integer;
   
begin

   (* Entrada de datos*)

   writeln;
   writeln ('Introduzca los coeficientes de dicho polinomio');
   for i := 0 to N do
   begin
      write ('Coeficiente de grado ',i:2, ' = ');
      read (C[i])
   end;

   {Precondicion: N,C %in Z /\ (%forall i : 0<=i<=N : C[i])}

   (* Salida de datos *)
   
   write ('El polinomio es = ');

   for i:= 0 to N do
   begin
      write (C[i]:0:2,'X^',i,'+')
   end;
   writeln;
   readln;
end.