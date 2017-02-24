program ejercicio5;
var
   a : integer;
   b : integer;
   c : integer;
   d : real;
//a,b,c %in Z /\ a!=b /\ a!=c /\ b!=c
begin
   writeln ('Introduzca tres valores enteros para a, b y c');
   read (a);
   read (b);
   read (c);
   d := (sqr(a)/(b-c));
   writeln ('El valor de d es');
   writeln (d);
end.
//d %in R