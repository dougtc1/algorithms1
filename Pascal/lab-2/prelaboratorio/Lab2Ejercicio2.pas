(*
 * ejercicio2 
 * Descripción: Dado el ancho y el largo de una habitación, este programa
 * calcula su superficie mostrando 4 decimales.
 *
 *  Autores:
 *      Prep. Reinaldo Verdugo 
 *	Prof. Rosseline Rodríguez 
 *
 * Última modificación: 18/02/2014
 *)


PROGRAM ejercicio2;
VAR
   ancho : REAL; // Ancho de la habitación
   largo : REAL; // Largo de la habitación
   superf : REAL; // Superficie de la habitación
   {Precondición : largo > 0 /\ ancho > 0}

BEGIN

   (* Entrada de datos *)

   WRITELN;
   WRITE('Este programa calcula la superficie de una habitación ');
   WRITELN('dado su largo y su ancho.'); 
   WRITELN('Por favor, ingrese la medida del largo de la habitación');
   READLN(largo);
   WRITELN('Por favor, ingrese la medida del ancho de la habitación');
   READLN(ancho);

   (* Cálculo del resultado *)

   superf:= largo * ancho;

   (* Salida de resultados *)
   
   WRITELN('La superficie de la habitación es de: ',superf:4:4);
   WRITELN;
   READLN;

END.
{Postcondición:	superf = largo * ancho}