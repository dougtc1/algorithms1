(*
 *  Ejercicio 6 del laboratorio 2
 *
 *  Descripcion: El siguiente programa incluye la especificacion necesaria para determinar la mayor fecha de dos dados
 *  Autor: Douglas Torres
 *  Ultima modificacion: 01/03/2014
 *)

program Lab2Ejercicio6;

type
   Dias	= 1..31;
   Mes	= 1..12;
   Anio	= 1..3000;

var
   dia1	 : Dias;
   dia2	 : Dias;
   mes1	 : Mes;
   mes2	 : Mes;
   anio1 : Anio;
   anio2 : Anio;

begin

   (* Entrada de datos*)

   writeln;
   writeln ('Este programa determina, dadas dos fechas, si la primera fecha es menor que la segunda fecha'); 
   writeln ('Introduzca una primera fecha en el formato dia, mes, anio')
   readln (dia, mes, anio);
   writeln ('Introduzca una segunda fecha en el formato dia, mes, anio')

   {Precondicion: dia1,dia2,mes1,mes2,anio1,anio2 %in N /\ (1<=mes1<=12)
   /\ (1<=anio1<=3000) /\ ((mes1 == 2)==>(1<=dia1<=28))
   /\ ((mes1==1 \/ mes1==3 \/ mes1==5 \/ mes1==7 \/ mes1==8 \/ mes1==10 \/ mes1==12)
   ==>(1<=dia1<=31))
   /\ ((mes1==4 \/ mes1==6 \/ mes1==9 \/ mes1==11)==>(1<=dia1<=30))
   /\ (1<=mes2<=12) /\ (1<=anio2<=3000) /\ ((mes2 == 2)==>(1<=dia2<=28))
   /\ ((mes2==1 \/ mes2==3 \/ mes2==5 \/ mes2==7 \/ mes2==8 \/ mes2==10 \/ mes2==12)
   ==>(1<=dia2<=31))
   /\ ((mes2==4 \/ mes2==6 \/ mes2==9 \/ mes2==11)==>(1<=dia2<=30))}

   (* Calculo de resultados *)

   {Postcondicion: (anio1<anio2)==>((mes1<mes2)==>(dia1<dia2))}

   if anio1<anio2 and mes1<mes2 and dia1<dia2 then
      writeln ('La fecha ',dia1,'/',mes1,'/',anio1,' es menor que la fecha ',dia2,'/',mes2,'/',anio2)
   else
      writeln ('La fecha ',dia1,'/',mes1,'/',anio1,' no es menor que la fecha ',dia2,'/',mes2,'/',anio2);
   writeln;
end.