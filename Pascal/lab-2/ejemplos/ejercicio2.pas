(* 
 * Autores:
 *
 *
 *
 *)
	ancho	: REAL; // Ancho de la habitación
	READLN(ancho);
BEGIN
	(* Cálculo del resultado *)
 * Descripción: Dado el ancho y el largo de una habitación, este programa
 *              calcula su superficie mostrando 4 decimales.
END.
	(* Entrada de datos *)

 * ejercicio2
	WRITELN;
	WRITE('Este programa calcula la superficie de una habitación ');
	WRITELN('dado su largo y su ancho.');
	largo	: REAL; // Largo de la habitación
	READLN(largo);
	WRITELN('La superficie de la habitación es de: ',superf:4:4);
	{Postcondición:
		superf = largo * ancho
	}
	{Precondición: largo > 0 /\ ancho > 0}
 *	Prep. Reinaldo Verdugo
        READLN;
 *	Prof. Rosseline Rodríguez
PROGRAM ejercicio2;
	(* Salida de resultados *)
	superf : REAL;	// Superficie de la habitación
	superf:= largo * ancho;
 *
 * Última modificación: 18/02/2014

	WRITELN('Por favor, ingrese la medida del largo de la habitación');
VAR

	WRITELN('Por favor, ingrese la medida del ancho de la habitación');
	WRITELN;

