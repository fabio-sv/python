'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X '''

#lendo os valores 
A = input();
B = input();
C = input();

triangulo = False;

if (A - B < C < (A + B)):
   triangulo = True;
        
if(A - C < B < (A + C)):
    triangulo = True; 

if(B - C < A < (B + C)):
    triangulo = True;

if(triangulo):
    perimetro = float(A + B + C);
    print("Perimetro = ", perimetro)
else:
    area = float(((A + B) * C) / 2);
    print("Area = ", area);


