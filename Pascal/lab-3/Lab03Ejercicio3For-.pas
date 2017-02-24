(*
 *  Ejercicio 3 (for decreciente) del laboratorio 3
 *
 *  Descripcion: El siguiente programa determina la suma
 *  de los primeros n factoriales
 *  Autor: Douglas Torres
 *  Ultima modificacion: 10/03/2014
 *)

program Lab03Ejercicio3Repeat;

var
   i	: integer;
   n	: integer;
   fact	: integer;
   suma	: integer;
	
begin

   (* Entrada de datos *)

   writeln ('Introduzca un numero n para calcular la sumatoria de los primeros n factoriales');
   readln (n);
   writeln;

   {Precondicion: n %in Z /\ n >=0}

   (* Calculo de datos *)

   suma := 0;
   fact := 1;

   for i:=n downto 1 do
      begin
      fact := (n-i+1)*fact;
      suma := suma+fact;
      end;
   
{Postcondicion: suma %in Z /\ suma=(%sigma i : 1<=i<=n : n!)}

   (* Salida de datos *)

   writeln;
   writeln ('La suma de los ',n,' factoriales es = ',suma);
   readln;
   
end.