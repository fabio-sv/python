def media(lista):
	media = 0
	for aluno in lista:
		media += aluno['nota']
	
	media = media / len(lista) if len(lista) != 0 else 1 #if ternário
	
	print("\nMédia: " + str(media))
	
def leitura():
	lista_alunos = []
	qtde_alunos = int(input("Quantidade de alunos? "))
	
	for i in range(qtde_alunos):
		nome = input("\nnome(" + str(i) + "): ")
		nota = float(input("nota(" + str(i) + "): "))
		
		lista_alunos.append({'nome' : nome, 'nota' : nota})
	
	print(lista_alunos)
	media(lista_alunos)

	
leitura()