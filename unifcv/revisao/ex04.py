def cadastrar():
    pessoa = []

    nome = input("\nNome: ")
    cpf = input("CPF: ")
    idade = input("Idade: ")
    cidade = input("Cidade: ")

    pessoa.append(
        {
            'nome': nome,
            'cpf': cpf,
            'idade': idade,
            'cidade': cidade
        }
    )
    return pessoa

def listar(lista):

    if len(lista) > 0:
        for indice in lista:
            for pessoa in indice:
                print(
                    "Nome:", pessoa['nome'], "-",
                    "CPF:", pessoa['cpf'], "-",
                    "Idade:", pessoa['idade'], "-",
                    "Cidade:", pessoa['cidade']
                )

    else:
        print("\nLista vazia")        
   

def remover(lista):
    if len(lista) > 0:
        nome = input("\nInforme o nome a ser removido: ")

        for arrIndex in lista:
            for pessoa in arrIndex:
                if pessoa['nome'] == nome:
                    remove = lista.index(arrIndex)
                    lista.pop(remove)

    else:
        print("\nLista vazia")  

def fechar():
    return 4
                           
def main():
    pessoas_lista = []
    escolha  = 0

    while escolha != 4:
        print("\n### MENU ###")
        print("# 1 - cadastrar #")
        print("# 2 - listar #")
        print("# 3 - remover #")
        print("# 4 - fechar #")

        escolha = int(input("\nOpção: "))

        if escolha == 1:
            pessoas_lista.append(cadastrar())

        if escolha == 2:
            listar(pessoas_lista)   

        if escolha == 3:
             remover(pessoas_lista)

        if escolha == 4:
            print("Finalizado.")
            escolha = int(fechar())    
                  
main()    




 
