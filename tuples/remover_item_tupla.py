#Converta a tupla em uma lista, remova "mizuno", e converta-a de volta em uma tupla:
marcas = ("nike", "adidas", "mizuno");

list1 = list(marcas);
list1.remove("mizuno");

marcas = tuple(list1);
print(marcas); #('nike', 'adidas')

#A palavra-chave pode excluir completamente a tupla:del:
del marcas;
print(marcas); #NameError: name 'marcas' is not defined