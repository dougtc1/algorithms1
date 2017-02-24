(*
 * ejercicio1
 *
 * Descripción: El siguiente programa define tipos para los días de la semana
 * y muestra los ordinales y nombres de cada uno de los tres tipos.
 *
 * Autores:
 *	Prep. Reinaldo Verdugo
 *	Prof. Rosseline Rodríguez
 *
 * Última modificación: 23/01/2013
 *)


PROGRAM ejercicio1;

TYPE
	
	Dias = (lunes,martes,miercoles,jueves,viernes,sabado,domingo);
	
	Dias_fin = sabado .. domingo;

	Fin_Dias = (saturday,sunday);

VAR

    dia     : Dias;    // Variable que almacena el nombre de un dia
    ordinal : INTEGER; // Variable que muestra el ordinal de cada dia

BEGIN

    (* Entrada de datos *)

    WRITELN;
    WRITELN('Introduzca un dia de la semana');
    READLN(dia);
    WRITELN;

	{Precondición: TRUE}

    (* Calculo de resultados *)

    ordinal:= ord(dia);

	{Postcondición:
	             (dia = lunes ==> ordinal = 0) /\
                        (dia = martes ==> ordinal = 1) /\
                        (dia = miercoles ==> ordinal = 2) /\
                        (dia = jueves ==> ordinal = 3) /\
                        (dia = viernes ==> ordinal = 4) /\
                        (dia = sabado ==> ordinal = 5) /\
                        (dia = domingo ==> ordinal = 6)
        }

	(* Salida de datos *)

    WRITELN('El ordinal de ',dia,' es',ordinal:3);
    READLN;
END.