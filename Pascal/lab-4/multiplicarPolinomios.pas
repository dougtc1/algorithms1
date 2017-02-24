(*
  * mutiplicarPolinomios
  * Programa para ilustrar el uso de arreglos, se implementan operaciones de polinomios
  * Autor: Prof. Leonid TINEO y Prof. Rosseline Rodriguez
  * Fecha �ltima modificaci�n: 14/03/2014
  *)

program mutiplicarPolinomios;

const
	MAX = 10; // m�ximo tama�o del polinomio de salida
	N = 5;	  // grado m�ximo de los polinomios a usar
type
	polinomio = array [0..MAX] of real; // polinomios reales
	
var
	p1	: polinomio; // primer operando
	p2	: polinomio; // segundo operando
	p3	: polinomio; // resultado
	i,j	: integer;	 // indice
	
BEGIN
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
	
    {PRE:(%forall i : 0<=i<=N : p1[i] /\ p2[i] %in R)}

    (* Calculo *)
	
	// Se inicializa los elementos del polinomio de salida con el
	// neutro de la suma
	for i:= 0 to N+N do begin 
		p3[i] := 0;
	end;
	
	for i:= 0 to N do begin
		for j:= 0 to N do begin
			p3[i+j] := p3[i+j] + p1[i]*p2[j];
		end;
	end;

   { Post:(%forall i : 0<=i<=N :
   (%forall j : 0<=j<=N : p3[i+j]=p3[i+j]+p1[i]*p2[j] %in R))}
   
    (* Salida de datos *)
	
	writeln;
	writeln('El polinomio P3 = P1 * P2 es:');
	for i:= 0 to N+N do begin 
		write('Coeficiente de grado ',i:3,' = ');
		writeln(p3[i]:7:2);
	end;
	writeln;
	
end.