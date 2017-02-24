(*
 *  Ejercicio 5 del laboratorio 3
 *
 *  Descripcion: El siguiente programa da al usuario 3 opciones
 *  a escoger para que se calcule la superficie de una habitacion
 * el area de una circunferencia o una suma de cuadrados
 *  Autor: Douglas Torres
 *  Ultima modificacion: 16/03/2014
 *)

program Lab03Ejercicio5;

type
   Calculo = (superficie,area,suma);

const
   pi = 3.1416;

var
   entrada   : Calculo; //Variable que almacena el valor a usar del tipo
   largo     : real; //Variable que almacena el largo de una habitacion
   ancho     : real; //Variable que almacena el ancho de una habitacion
   resultado : real; //Variable que almacena el resultado
   radio     : real; //Variable que almacena el radio de una circunferencia
   n	     : integer; //Variable que almacena un numero n
   i	     : integer; //Variable que almacena el i usado para iterar
   intentos  : integer; //Variable que almacena la cantidad de intentos
	     
begin

   (* Entrada de datos *)

   writeln ('Seleccione una de las siguientes opciones:');
   writeln ('Calculo de una superficie (superficie)');
   writeln ('Calculo del area de una circunferencia (area)');
   writeln ('Calculo del cuadrado de un numero n (suma)');
   readln (entrada);
   writeln;

   {Precondicion: entrada %in Calculo}

   (* Calculo de datos *)

   intentos := 0;

   (* Aqui usamos un while que cuenta los intentos que lleve
    *  el usuario (maximo 3 intentos) y un case para el menu de opciones *)

    while (intentos<3) do

   begin

      case entrada of

      superficie : begin
		      writeln ('Introduzca largo y ancho');
		      readln (largo,ancho);
		      resultado := largo*ancho;
		      write ('La superficie es: ');
		      intentos := 4;
		   end;

      area	 : begin
		      writeln ('Introduzca un radio');
		      readln (radio);
		      resultado := pi*sqr(radio);
		      write ('El area especificada es: ');
		      intentos := 4;
		   end;

      suma	 : begin
		      writeln ('Introduzca un numero n');
		      readln (n);
		      resultado := 0;
		      (* Aqui usamos un for para que itere desde 1
		       *  hasta el numero dado *)
		      for i:=1 to n do
		      begin
			 resultado := sqr(i)+resultado;
		      end;
		      write ('La suma es: ');
		      intentos := 4;
		   end;
      else
      begin
	 writeln ('Debe elegir entre "superficie", "area" y "suma"');
	 readln (entrada);
	 intentos   := intentos+1
      end;
      end { case }
   end;
   
   {Postcondicion: resultado %in R /\ resultado>0}

   (* Salida de datos *)

   (* Aqui usamos un if para verificar si el usuario consumio
    *  sus intentos o si efectivamente se calculo lo deseado *)

    if (intentos=3) then
      writeln('Ha llegado al limite de intentos, intente nuevamente.')
   else
   begin
      write (resultado:0:2);
      writeln;
      readln
   end;
end.