def print_lista(lista):
	print('\n ### Lista de nomes em ordem alfabética ###')
	for nome in lista:
		print(nome)

def leitura_nomes():
	qtde = int(input("Quantos nomes serão inseridos? "))
	lista_nomes = []
	
	for i in range(qtde):
		nome = input("Nome " + str(i) + ": ")
		lista_nomes.append(nome)
	
	lista_nomes.sort()
	#print(lista_nomes)
	
	print_lista(lista_nomes)

leitura_nomes()