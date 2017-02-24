(*
  * ejemploEstudiantes
  * Programa para ilustrar el uso combinado de registros y arreglos
  * se mplementan operaciones con notas de estudiantes
  * Autor: Douglas Torres
  * Fecha: 22/11/2013
  *)
  
program ejemploEstudiantes;

const
	MAX_EST	= 3;

type
   materia = (ci2511,ci2525,ci2526,ci2611,ci2691);
	   
nota		 = 1..5; 
	
listaNotas	 = array [materia] of nota; 
   
credito		 = 0..9; 
	
listaCreditos	 = array [materia] of credito; 
	
estudiante	 = record	
		      nombre : string;	
		      carnet : longint;		
		      indice : real;		
		      notas  : listaNotas	
		   end;	     

listaEstudiantes = array [1..MAX_EST] of estudiante; 
	
var
   estudiantes : listaEstudiantes;
   creditos    : listaCreditos;
   i	       : integer;
   codigo      : materia;
   numerador   : integer;
   denominador : integer;
   
begin
   //  Se inicializa la lista de creditos
   creditos[ci2511] := 4;
   creditos[ci2525] := 4;
   creditos[ci2526] := 4;
   creditos[ci2611] := 3;
   creditos[ci2691] := 2;	
   
   for i := 1 to MAX_EST do begin
      writeln('Introduzca datos del estudiante ',i:3);
      with estudiantes[i] do begin
	 write('nombre : ');
	 readln(nombre);
	 write('carnet : ');
	 readln(carnet);
	 for codigo:= ci2511 to ci2691 do begin
	    write('nota en ',codigo,' : ');
	    readln(notas[codigo]);
	 end;
      end;
      writeln;
   end;
   
   {PRE: nota,carnet %in Z /\ nombre %in string /\ nota>0 /\ carnet>0}
   
   
   for i:= 1 to MAX_EST do begin
      
      with estudiantes[i] do begin

	 numerador := 0;
	 denominador := 0;
	 indice := 0;
	 
	 for codigo:= ci2511 to ci2691 do begin
	      
	    numerador := numerador+(notas[codigo]*creditos[codigo]);

	    denominador := denominador+creditos[codigo];

	 end;
	 indice := numerador/denominador;
      end;
   end;

   {POST: indice %in R /\ numerador,denominador %in Z /\ indice=numerador/denominador}
   
   for i := 1 to MAX_EST do begin
      writeln('Datos del estudiante ',i:3);
      with estudiantes[i] do begin
	 writeln('nombre : ',nombre);
	 writeln('carnet : ',carnet);
	 writeln('El indice es: ',indice:7:4);
      end;
      writeln;
   end;
end.