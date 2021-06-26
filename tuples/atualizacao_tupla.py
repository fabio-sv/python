'''As tuplas são imutáveis, o que significa que você não pode alterar, adicionar ou remover itens uma 
vez que a tupla é criada.

Mas há uma solução. Você pode converter a tupla em uma lista, alterar a lista e converter a lista de 
volta em uma tupla.'''

#Converta a tupla em uma lista para poder alterá-la:
tuple1 = ("apple", "banana", "cherry");

list1 = list(tuple1);
list1[2] = "kiwi";
tuple1 = tuple(list1);

print(tuple1); #('apple', 'banana', 'kiwi')