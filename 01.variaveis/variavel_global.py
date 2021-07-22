#Crie uma variável fora de uma função e use-a dentro da função

#Variável Global
x  = "legal"; 

#função
def my_func():
    print("Python é " + x);
#Chamada da função
my_func(); #saída; Python é legal

#Crie uma variável dentro de uma função, com o mesmo nome da variável global
y = "top";

def my_func2():
    y = "fantastico";
    print("Python é " + y); #saída: Python é fantastico
    
my_func2();    

print("Python é " + y); #saída: Python é top

#Para criar uma variável global dentro de uma função, você pode usar a globalpalavra - chave.
def my_func3():
    global z;
    z = "demais";

my_func3();   

print("Python é " + z); #saída: Python é demais

#Para alterar o valor de uma variável global dentro de uma função, consulte a variável usando a globalpalavra-chave:
i = 10;

def my_func4():
    global i;
    i = 20;

my_func4();

print(i); #saída: 20