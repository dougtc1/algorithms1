(*
 *  Ejercicio 4 del laboratorio 2
 *
 *  Descripcion: El siguiente programa calcula la pendiente de
 *  la recta que pasa por dos puntos.
 *  El usuario dara dos coordenadas correspondientes a
 *  los dos puntos requeridos
 *  Autor: Douglas Torres
 *  Ultima modificacion: 01/03/2014
 *)

program Lab2Ejercicio4;

var
   ordenada1 : integer; //Variable que almacena la ordenada de la primera coordenada
   ordenada2 : integer; //Variable que almacena la ordenada de la segunda coordenada
   abscisa1  : integer; //Variable que almacena la ordenada de la primera coordenada
   abscisa2  : integer; //Variable que almacena la ordenada de la segunda coordenada
   pendiente : real; //Variable que almacena la pendiente de la recta que pasa por los puntos

begin

   (* Entrada de datos *)

   writeln;
   writeln ('Este programa calcula la pendiente de la recta que pasa por dos puntos.');
   writeln ('Escriba la primera coordenada (abscisa,ordenada)');
   readln (abscisa1, ordenada1);
   writeln ('Escriba la segunda coordenada (abscisa,ordenada)');
   readln (abscisa2, ordenada2);
   writeln;

   {Precondicion: ordenada1,abscisa1,ordenada2,abscisa2 %in Z
   /\ abscisa1 != abscisa2}

   (*Calculo de resultados*)

   pendiente := ((ordenada2 - ordenada1)/(abscisa2 - abscisa1));

   {postcondicion: pendiente %in R}

   writeln ('La pendiente de la recta que pasa los puntos ','(',
	    abscisa1,',', ordenada1,')',' y ','(',abscisa2,',',
	    ordenada2,')', ' es =', pendiente:0:2);
   writeln;

end.