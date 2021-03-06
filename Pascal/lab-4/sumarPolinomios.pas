(*
  * sumarPolinomios
  * Programa para ilustrar el uso de arreglos, se implementan operaciones de polinomios
  * Autores: Prof. Leonid TINEO y Prof. Rosseline Rodriguez
  * Fecha �ltima modificaci�n: 13/03/2014
  *)

program sumarPolinomios;

const
	N = 5;	// grado m�ximo de los polinomios a usar

type
	polinomio = array [0..N] of real; // polinomios reales

var
	p1	: polinomio; // primer operando
	p2	: polinomio; // segundo operando
	p3	: polinomio; // resultado
	i	: integer;	// indice
begin

	(* Entrada de datos *)
    writeln;
	writeln('Introduzca el polinomio P1');
	for i:= 0 to N do begin
		write('Coeficiente de grado ',i:3,' = ');
		readln(p1[i]);
	end;
	
	writeln;
	writeln('Introduzca el polinomio P2');
	for i:= 0 to N do begin
		write('Coeficiente de grado ',i:3,' = ');
		readln(p2[i]);
	end;
	
   {PRE: %forall i : 0<=i<=5 : p1[i] /\ p2[i] %in R}

    
    (* Calculo *)
	for i:= 0 to N do begin
		p3[i] := p1[i]+p2[i];
	end;

	{ Post: %forall i : 0<=i<=5 : p3[i]=p1[i]+p2[i] %in R}
	             
    (* Salida de datos *)
	
	writeln;
	writeln('El polinomio P3 = P1 + P2 es:');
	for i:= 0 to N do begin 
		write('Coeficiente de grado ',i:3,' = ');
		writeln(p3[i]:7:2);
	end;
	writeln;
	
end.