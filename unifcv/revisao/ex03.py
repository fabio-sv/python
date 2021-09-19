def media(lista):
    soma = 0
    for aluno in lista:
        soma += aluno['nota']

    media = soma / len(lista)    

    print("Media: ", media)


def print_alunos(lista):
    for i in range(len(lista)):
        print(lista[i])
        
    media(lista)    

def notas():
    alunos = []

    qtde = int(input("Quantidade alunos: "))

    for i in range(qtde):
        nome = str(input("\nNome: "))
        nota = float(input("Nota: "))

        alunos.append({'nome':nome, 'nota':nota})

    print_alunos(alunos)    

notas()