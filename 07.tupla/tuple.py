my_tuple =  ("maçã", "uva", "banana");
print(my_tuple); #('maçã', 'uva', 'banana')

#As tuplas permitem valores duplicados:
tuple1 = ("bmw", "volvo", "ford", "vw", "vw", "bmw");
print(tuple1); #('bmw', 'volvo', 'ford', 'vw', 'vw', 'bmw')

#Imprima o número de itens na tupla:
print(len(tuple1)); #6

#Um item tuple precisa de virgula:
tuple2 = ("banana",);
print(type(tuple2)); #<class 'tuple'>

#Tipos de dados int, string e boolean:
tuple3 = (1, 2, 3, 4, 5, 6, 7);
tuple4 = (True, False, False, True);
print(tuple3, tuple4); #(1, 2, 3, 4, 5, 6, 7) (True, False, False, True)

#Uma tupla pode conter diferentes tipos de dados:
tuple5 = ("abc", 345, True, 49, "male");
print(tuple5); #('abc', 345, True, 49, 'male')