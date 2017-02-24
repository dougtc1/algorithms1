(*
 *  Ejercicio 3 (while) del laboratorio 3
 *
 *  Descripcion: El siguiente programa determina la suma
 *  de los primeros n factoriales
 *  Autor: Douglas Torres
 *  Ultima modificacion: 10/03/2014
 *)

program Lab03Ejercicio3While;

var
   i	: integer; //Variable que almacena las iteraciones
   n	: integer; //Varibale que almacena el numero dado
   fact	: integer; //variable que almacena el factorial de n
   suma	: integer; //variable que almacena la suma de los n factoriales
	
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

(* Aqui se usa el comando de control while que iterara hasta que la i alcance
 *  el valor dado por el usuario *)
   
   while i<=n do
   begin
      fact := fact*i;
      suma := fact+suma;
      i := i+1;
   end;

   {Postcondicion: suma %in Z /\ suma=(%sigma i : 1<=i<=n : n!)}

   (* Salida de datos *)
   writeln ('La suma de los ',n,' factoriales es = ',suma);
   readln;
   
end.