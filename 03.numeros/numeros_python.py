#Existem três tipos numéricos em Python:

x = 1;
y = 2.8;
z = 1j; 

print(type(x)); #<class 'int'>
print(type(y)); #<class 'float'>
print(type(z)); #<class 'complex'>

#inteiro
x1 =  1;
x2 =  35656222554887711;
x3 = -337636464;

print(type(x1)); #<class 'int'> 
print(type(x2)); #<class 'int'> 
print(type(x3)); #<class 'int'> 

#flutuante
y1 =  1.10;
y2 =  1.0;
y3 = -33.76;

print(type(y1)); #<class 'float'> 
print(type(y2)); #<class 'float'> 
print(type(y3)); #<class 'float'> 

#float cientifico
z1 =  35e10;
print(z1); #350000000000.0

#numeros comlexos são escritos com um "j" como a parte imaginária:
num_complexo = 3 + 5j;
print(num_complexo); #saída: (3+5j)