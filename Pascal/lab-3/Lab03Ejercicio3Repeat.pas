
   i	: integer; //Variable que almacena las iteraciones
   n	: integer; //Variable que almacena el numero dadoo
   fact	: integer; //Variable que almacena el factorial de n
   suma	: integer; //Variable que almacena la suma de los n primeros factoriales
	
begin

   (* Entrada de datos *)

   writeln ('Introduzca un numero n para calcular la sumatoria de los primeros n factoriales');
   readln (n);
   writeln;

   {Precondicion: n %in Z /\ n >=0}

   (* Calculo de datos *)

   i := 1;
   suma := 0;
   fact := 1;

(* Aqui se usa el comando de contro repeat donde iterara hasta alcanzar
 *  el valor dado por el usuario inclusive*)
   
   repeat
      fact := fact*i;
      suma := fact+suma;
      i := i+1;
   until (i=(n+1));

{Postcondicion: suma %in Z /\ suma=(%sigma i : 1<=i<=n : n!)}
   
   (* Salida de datos *)

   writeln;
   writeln ('La suma de los ',n,' factoriales es = ',suma);
   readln;
   
end.