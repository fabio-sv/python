#O número deficiente pode ser definido como o número para o qual a soma dos divisores
# apropriados é menor que o próprio número.
numero = 6

soma = 0
for i in range(1, numero):
		if numero % i == 0:
			soma = soma + i
		if soma == numero and i == numero - 1:
			print(numero, "é um número perfeito")
		elif soma != numero and i == numero - 1:
			print(numero, "é um número deficiênte")	