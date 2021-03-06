(*
 *  Ejercicio 2 del laboratorio 3
 *
 *  Descripcion: El siguiente programa calcula, dados 2 numeros
 *  enteros m y n y devuelva ciertos resultados de operaciones
 *  aritmeticas dependiendo de los valores de m y n
 *  Autor: Douglas Torres
 *  Ultima modificacion: 10/03/2014
 *)

program Lab03Ejercicio2;

Uses math;

var
   m	: integer; //Variable que almacena el numero m dado
   n	: integer; //Variable que almacena el numero n dado
   div1	: real; //Variable que almacena el resultado de una division de enteros
   op1	: integer; //Variable que almacena una operacion matematica

begin

   (* Entrada de datos *)

   writeln;
   writeln ('Introduzca 2 valores m y n y se le daran unos resultados');
   readln (m,n);
   writeln;

   {Precondicion: m,n %in Z}

   (* Calculo y salida de datos *)

(* Aqui se usa el comando de control case donde dependiendo del numero
 *  ingresado por el usuario tendra distintas impresiones en pantalla *)
   
   case m of
     10	: begin
	     div1 := m/n;
	     writeln ('m=10 por lo que se le da el valor de m/n=',div1:0:2);
	  end;
     5	: begin
	     op1 := m*n;
	     writeln ('m=5 por lo que se le da el valor de m*n=',op1);
	  end;
     3	: begin
	     op1 := m+n;
	     writeln ('m=3 por lo que se le da el valor de m+n=',op1);
	  end;
     2	:  begin
	      op1 := m**n;
	      writeln ('m=2 por lo que se le da el valor de m^n=',op1);
	   end;
   else
      writeln ('Se imprime el valor de m=',m);
     writeln;
   end; { case }

   readln;
   
end.