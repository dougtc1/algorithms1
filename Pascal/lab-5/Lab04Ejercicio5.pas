(*
  * Ejercicio 5 Laboratorio 4
  * Este programa calcula la nota de 10 estudiantes de la materia CI2611
  * Autor: Douglas Torres
  * Fecha: 22/03/2014
  *)
  
program Lab04Ejercicio5;

const
   MAX_EST   = 10;

type
   nota		    = 1..25;
   total	    = array [1..4] of nota;
   parciales	    = array [1..4] of nota ;
   listaNotas	    = array [parciales] of nota;
   estudiante	    = record	
			 nombre	  : string;	
			 carnet	  : longint;		
			 notas	  : listaNotas;
			 total	  : integer;
			 promedio : real;
		      end;	  
   listaEstudiantes = array [1..MAX_EST] of estudiante;
   	
var
   estudiantes : listaEstudiantes;
   i	       : integer;
   parcial     : parciales;
     
begin

   for i:=1 to MAX_EST do begin
      with estudiantes[i] do begin
	 for parcial:=1 to 4 do begin
	    notas[parcial] = parcial+i+1;
	 end;
      end;
   end;
   
   for i := 1 to MAX_EST do begin
      writeln('Introduzca datos del estudiante ',i:3);
      with estudiantes[i] do begin
	 write('nombre : ');
	 readln(nombre);
	 write('carnet : ');
	 readln(carnet);
	 for parcial := 1 to parciales do begin
	    write('nota en parcial ',parcial,);
	 end;
      end;
      writeln;
   end;
   
   {PRE: nota,carnet %in Z /\ nombre %in string /\ 1<=nota<=25 /\ carnet>0}
   
      
   for i:= 1 to MAX_EST do begin
      
      with estudiantes[i] do begin

	 total := 0;
	 promedio := 0;
	 	      
	 for parcial :=1 to parciales do begin
	    total := total+notas[parcial];
	 end;
	 promedio := total/parciales;
      end;
   end;
	      
   {POST: promedio %in R /\ total %in Z}
   
   for i := 1 to MAX_EST do begin
      writeln('Datos del estudiante ',i:3);
      with estudiantes[i] do begin
	 writeln('nombre : ',nombre);
	 writeln('carnet : ',carnet);
	 writeln('El total acumulado de la materia es : ',total);
	 writeln('El promedio de notas es : ',promedio:0:2);
      end;
      readln;
   end;
end.