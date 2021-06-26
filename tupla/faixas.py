tuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango");
print(tuple1[2:5]); #('cherry', 'orange', 'kiwi')

#Este exemplo retorna tos itens anteriores ao "kiwi":
print(tuple1[:4]); #('apple', 'banana', 'cherry', 'orange')

#Este exemplo retorna todos itens de "cherry" em diante:
print(tuple1[2:]); #('cherry', 'orange', 'kiwi', 'melon', 'mango')

#Este exemplo retorna os índices entre -4 e -1: 
print(tuple1[-4:-1]); #('orange', 'kiwi', 'melon')

#Verifique se "apple" está presente na tupla:
if("apple" in tuple1):
    print("existe"); #existe

