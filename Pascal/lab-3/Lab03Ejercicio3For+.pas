(*
 *  Ejercicio 3 (for creciente) del laboratorio 3
 *
 *  Descripcion: El siguiente programa determina la suma
 *  de los primeros n factoriales
 *  Autor: Douglas Torres
 *  Ultima modificacion: 10/03/2014
 *)

program Lab03Ejercicio3Repeat;

var
   i	: integer; //Variable que almacena las iteraciones
   n	: integer; //Variable que almacena el numero dado
   fact	: integer; //Variable que almacena el factorial de n
   suma	: integer; //Variable que almacena la suma de los n primeros factoriales
	
begin

   (* Entrada de datos *)

   writeln ('Introduzca un numero n para calcular la sumatoria de los primeros n factoriales');
   readln (n);
   writeln;

   {Precondicion: n %in Z /\ n >=0}

   (* Calculo de datos *)

   suma := 0;
   fact := 1;

(* Aqui se usa el comando de control for donde se inicializa una variable que
 *  contara las iteraciones del ciclo hasta igualar el numero dado por el usuario *)
   
   for i := 1 to n do
      begin
      fact := fact*i;
      suma := fact+suma;
      end;
   
{Postcondicion: suma %in Z /\ suma=(%sigma i : 1<=i<=n : n!)}

   (* Salida de datos *)

   writeln;
   writeln ('La suma de los ',n,' primeros factoriales es = ',suma);
   readln;
   
end.