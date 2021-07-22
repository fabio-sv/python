#Converta a tupla em uma lista, adicione "porsche", e converta-a de volta em uma tupla:
tuble1 = ("bmw", "volvo", "vw");

list1 = list(tuble1);
list1.append("porsche");

tuble1 = tuple(list1);
print(tuble1); #('bmw', 'volvo', 'vw', 'porsche')

#Crie uma nova tupla com o valor "laranja", e adicione essa tupla
tuple2 = ("banana", "laranja", "uva");
tuple3 = ("kiwi",); #add a vírgula

tuple2 += tuple3
print(tuple2); #('banana', 'laranja', 'uva', 'kiwi')