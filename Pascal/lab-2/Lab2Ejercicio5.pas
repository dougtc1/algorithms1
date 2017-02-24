(*
 *  Ejercicio 5 del laboratorio 2
 *
 *  Descripcion: El siguiente programa calcula la ecuacion cuadratica correspondiente a dos raices dadas.
 *  Autor: Douglas Torres
 *  Ultima modificacion: 01/03/2014
 *)

program Lab2Ejercicio5;

var
   raiz1 : real; //Variable que almacena la primera raiz de la ecuacion cuadratica
   raiz2 : real; //Variable que almacena la segunda raiz de la ecuacion cuadratica
   b	 : real; //Variable que almacena el coeficiente b de la ecuacion cuadratica 
   c	 : real; //Variable que almacena el coeficiente c de la ecuacion cuadratica

begin

   (* Entrada de datos *)

   writeln;
   writeln (
        'El siguiente programa calcula la ecuacion cuadratica de dos raices dadas.'
	    );
   writeln ('Introduzca dos raices enteras');
   readln (raiz1, raiz2);
   writeln;
   
   {Precondicion: raiz1, raiz2 %in Z}

   (* Calculo de resultados *)
   b := -(raiz1 + raiz2);
   c := (raiz1 * raiz2);

   {Postcondicion: b, c %in Z /\ (b = -(raiz1+raiz2)) /\ (c = (raiz1*raiz2))}

   (* Salida de datos *)

   if b >= 0  then
      writeln ('La ecuacion cuadratica de las raices dadas es = (X^2)+',b:0:2,'X','+',c:0:2)
   else
      writeln ('La ecuacion cuadratica de las raices dadas es = (X^2)',b:0:2,'X','+',c:0:2);
   writeln;
   
end.