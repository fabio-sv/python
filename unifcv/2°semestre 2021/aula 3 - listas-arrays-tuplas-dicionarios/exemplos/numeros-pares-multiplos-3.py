def multiplos_3(lista):
	lista_multiplos_3 = []
	
	for numero in lista:
		if numero % 3 == 0:
			lista_multiplos_3.append(numero)
	
	print(lista_multiplos_3)

def numeros_pares():
	valor_limite = int(input("Valor limite: "))
	lista_numeros_pares = range(0, valor_limite, 2)
	
	for numero in lista_numeros_pares:
		print(numero)
	
	multiplos_3(lista_numeros_pares)

numeros_pares()