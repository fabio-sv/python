def print_nomes(lista):
    for nomes in range(len(lista)):
        print(lista[nomes])

def add_nomes ():
    qtde = int(input("Quantidade nomes: "))
    lista_nomes = []

    for i in range(qtde):
        nome = input("\nNomes: ")
        lista_nomes.append(nome)

    lista_nomes.sort() 
    print_nomes(lista_nomes)   
    
add_nomes()