(*
 *  Ejercicio 2 del laboratorio 4
 *
 *  Descripcion: El siguiente programa pide al usuario los coeficientes
 *  de un polinomio y el valor de la X y se imprime la evaluacion
 *  Autor: Douglas Torres
 *  Ultima modificacion: 21/03/2014
 *)

program Lab04Ejercicio2;

const
   N = 5;
   
type
   polinomio = array [0..N] of real;

var
   C	     : polinomio;
   resultado : real;
   i	     : integer;
   x	     : real;
   expp	     : real;
	     
begin

   (* Entrada de datos*)

   writeln;
   writeln ('Introduzca los coeficientes de un polinomio');
   for i := 0 to N do
   begin
      write ('Coeficiente de grado ',i:2, ' = ');
      readln (C[i])
   end;
   writeln ('De un valor de X para calcular el valor del polinomio');
   readln (x);

   {Precondicion: N,C %in Z /\ x %in R /\ (%forall i : 0<=i<=N : C[i])}

   (* Calculo de datos *)
   resultado := 0;

   for i := 0 to N do
   begin
      expp := Exp(LN(x)*i);
      resultado := resultado+(C[i]*expp);
   end;
   
   {Postcondicion: resultado in R}
   
   (* Salida de resultados *)

   writeln;
   writeln ('El resultado es');
   writeln ('P(',x:0:2,') = ',resultado:0:2);
   readln;
end.