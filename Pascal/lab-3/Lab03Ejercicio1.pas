(*
 *  Ejercicio 1 del laboratorio 3
 *
 *  Descripcion: El siguiente programa calcula el maximo
 *  numero entre 3 valores enteros diferentes A, B y C
 *  Autor: Douglas Torres
 *  Ultima modificacion: 10/03/2014
 *)

program Lab03Ejercicio1;

var
   A   : integer; //Variable que almacena el primer numero dado 
   B   : integer; //Variable que almacena el segundo numero dado 
   C   : integer; //Variable que almacena el tercer numero dado 
   max : integer; //Variable que almacena el max numero de los dados 

begin

   (* Entrada de datos *)

   writeln;
   writeln ('Introduzca 3 valores enteros y se le dira cual es el mayor');
   readln (A, B, C);
   writeln;
   
   {Precondicion: A,B,C %in Z /\ A!=B /\ A!=C /\ B!=C}

   (* Calculo de resultados *)

   (* Aqui se usa el comando de control if donde se verifica cada caso posible *)
   
   if (A>B) and (A>C) then
      max := A
   else if (B>C) and (B>C) then
      max := B
   else
      max := C;
   
   {Precondicion: maximo %in Z /\ (((max>B)/\(max>C)) \/
   ((max>A)/\(max>C)) \/ ((max>A)/\(max>B)))}
   
   (* Salida de datos *)

   writeln ('El maximo de los numeros dados es:',max);
   writeln;

end.