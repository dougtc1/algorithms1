(*
 *  Ejercicio 3 del laboratorio 2
 *
 *  Descripcion: El siguiente programa calcula la resta de dos numeros complejos A y B
 *  y la potencia cuadratica de cada uno de ellos.
 *  Autor: Douglas Torres
 *  Ultima modificacion: 28/02/2014
 *)

program Lab2Ejercicio3;

var
   realA     : real;   // Variable que almacena la parte real del numero A
   realB     : real;   // Variable que almacena la parte real del numero B
   imagA     : real;   // Variable que almacena la parte imaginaria del numero A
   imagB     : real;   // Variable que almacena la parte imaginaria del numero B
   restaR    : real;   // Variable que almacena el resultado de la resta real de A y B
   restaI    : real;   // Variable que almacena el resultado de la resta imaginaria de A y B
   potenciaRA : real;   // Variable que almacena la parte real de la potencia cuadratica de A
   potenciaIA : real;   // Variable que almacena la parte imaginaria de la potencia cuadratica de A
   potenciaRB : real;   // Variable que almacena la parte real de la potencia cuadratica de B
   potenciaIB : real;   // Variable que almacena la parte imaginaria de la potencia cuadratica de B

begin

   (* Entrada de datos *)
   
   writeln;
   writeln ('El siguiente programa calcula la resta de dos numeros complejos y la potencia cuadratica de cada uno de ellos.');
   writeln;
   writeln ('Introduzca la parte real e imaginaria del numero A');
   readln (realA, imagA);
   writeln ('Introduzca la parte real e imaginaria del numero B');
   readln (realB, imagB);
   writeln;
   
   {Precondicion: realA, realB, imagA, imagB %in R}

   (* Calculo de resultados *)
   
   restaR := (realA-realB);
   restaI := (imagA-imagB);
   potenciaRA := (sqr(realA)-sqr(imagA));
   potenciaIA := (2*realA*imagA);
   potenciaRB := (sqr(realB)-sqr(imagB));
   potenciaIB := (2*realB*imagB);

   {Postcondicion: restaR, restaI, potenciaRA, potenciaIA, potenciaRB, potenciaIB %in R}

   (* Salida de datos *)

   if restaI > 0 then
      writeln ('La resta es =',restaR:0:2,'+',restaI:0:2,'i')
   else
      writeln ('La resta es =',restaR:0:2, restaI:0:2,'i');

   writeln;

   if potenciaIA > 0 then
      writeln ('La potencia cuadratica del numero A es =',potenciaRA:0:2,'+',potenciaIA:0:2,'i')
   else
      writeln ('La potencia cuadratica del numero A es =',potenciaRA:0:2, potenciaIA:0:2,'i');

   writeln;

   if potenciaIB > 0 then
      writeln ('La potencia cuadratica del numero B es =',potenciaRB:0:2,'+',potenciaIB:0:2,'i')
   else
      writeln ('La potencia cuadratica del numero B es =',potenciaRB:0:2, potenciaIB:0:2,'i');

   writeln;
end.