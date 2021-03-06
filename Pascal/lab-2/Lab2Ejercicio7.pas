(*
 *  Ejercicio 7 del laboratorio 2
 *
 *  Descripcion: El siguiente programa incluye la especificacion necesaria para determinar la diferencia entre dos horas dadas
 *  Autor: Douglas Torres
 *  Ultima modificacion: 01/03/2014
 *)

program Lab2Ejercicio7;

type
   Horas    = 1..24;
   Minutos  = 1..60;
   Segundos = 1..60;

var
   hora1     : Horas;
   hora2     : Horas;
   minuto1   : Minutos;
   minuto2   : Minutos;
   segundo1  : Segundos;
   segundo2  : Segundos;
   restaHora : integer;
   restaMin  : integer;
   restaSeg  : integer;

begin

   (* Entrada de datos*)

   writeln;
   writeln ('Este programa determina la diferencia entre dos horas dadas.');
   writeln ('Introduzca una hora en el formato de 24 horas (hora minuto segundo');
   readln (hora1, minuto1, segundo1);
   writeln ('Introduzca otra hora en el formato de 24 horas (hora minuto segundo');
   readln (hora2, minuto2, segundo2);

   {Precondicion: hora1,hora2,minuto1,minuto2,segundo1,segundo2 %in N
   /\ (1<=hora1<=24) /\ (1<=hora2<=24) /\ (1<=minuto1<=60) /\ (1<=minuto2<=60)
   /\ (1<=segundo1<=60) /\ (1<=segundo2<=60)}

   (* Calculo de resultados *)

   {Postcondicion: restaHora,restaMin,restaSeg %in N /\ (1<=restaHora<=24) /\ (1<=restaMin<=60) /\ (1<=restaSeg<=60)}

   (* Salida de resultados *)
   writeln ('La diferencia de horas es: ',restaHora,':',restaMin,':',restaSeg);
   writeln;
end.