#Devolva um conjunto que contenha todos os itens de ambos os conjuntos, exceto itens presentes em ambos:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

#{'cherry', 'banana', 'microsoft', 'google'}