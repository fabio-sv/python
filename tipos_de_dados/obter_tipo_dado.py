#Em Python, o tipo de dados é definido quando você atribui um valor a uma variável:
x1  = 5 ;
print(type(x1)); #saída: <class 'int'>

x2  = "ola Python";
print(type(x2));

x3 = 20.5;
print(type(x3));

x4 =  1j;
print(type(x4));

x5 = ["banana", "laranja", "uva"];
print(type(x5));

x6 = ("banana", "laranja", "uva");
print(type(x6));

x7 = range(6);
print(type(x7));

x8 = {"name" : "John", "idade" : 36}
print(type(x8));

x9 = {"banana", "laranja", "uva"};
print(type(x9));

x10 = frozenset({"banana", "laranja", "uva"});
print(type(x10));

x11 =  True;
print(type(x11));

x12 = b"hello";
print(type(x12));

x13 = bytearray(5);
print(type(x13));

x14 = memoryview(bytes(5));
print(type(x14));