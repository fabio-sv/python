#Diz-se que um número é o número Harshad se for divisível pela soma de seu dígito.
numero = input("Número: ")

soma = 0
for num in numero:
	soma = soma + int(num)
	
if int(numero) % soma == 0:
	print(numero, "é um número harshad")
else:
	print(numero, "não é um número harshad")