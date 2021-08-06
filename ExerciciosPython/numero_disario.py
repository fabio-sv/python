# Verifica se o número é disário
numero = input("Número: ");

soma = 0
expo = 1

for i in numero:
	soma = soma + pow(int(i), expo)
	expo = expo + 1

if soma == int(numero):
	print(numero, "é um número disário")
else:
	print(numero, "não é um número disário")