def pares():
    lista_pares = []
    for i in range(0, 101, 2):
        if i % 3 == 0:
            lista_pares.append(i)

    print_lista(lista_pares)    

def print_lista(lista):
    for i in range(len(lista)):
        print(lista[i])


pares();